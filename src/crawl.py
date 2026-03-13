import asyncio
import json
import os
import re
from collections import deque
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit, urlunsplit

from dotenv import load_dotenv
from crawl4ai import AsyncWebCrawler, CacheMode, CrawlerRunConfig

load_dotenv()

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "data" / "crawled_data"
MANIFEST_PATH = OUTPUT_DIR / "manifest.json"
MIN_CONTENT_CHARS = int(os.getenv("CRAWL_MIN_CONTENT_CHARS", "350"))
MAX_PAGES_PER_SCOPE = int(os.getenv("CRAWL_MAX_PAGES_PER_SCOPE", "250"))
MAX_DEPTH =  3
VERBOSE_CRAWLER = os.getenv("CRAWL_VERBOSE", "false").lower() == "true"
SKIPPED_EXTENSIONS = {
    ".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp", ".ico", ".pdf",
    ".zip", ".tar", ".gz", ".tgz", ".mp4", ".mp3", ".wav", ".mov",
    ".xml", ".rss", ".json", ".txt", ".csv", ".doc", ".docx", ".ppt",
    ".pptx", ".xls", ".xlsx",
}
BLOCKED_PATH_PARTS = (
    "/search/",
    "/archive/",
    "/tags/",
    "/releases/",
    "/releases.xml",
    "/feed/",
)
BOT_CHALLENGE_MARKERS = (
    "performing security verification",
    "checking if the site connection is secure",
    "attention required",
    "just a moment",
    "cf-browser-verification",
    "cloudflare",
)

CRAWL_SCOPES = [
    {
        "name": "engineering_handbook",
        "seed": "https://handbook.gitlab.com/handbook/engineering/",
        "allowed_prefixes": [
            "https://handbook.gitlab.com/handbook/engineering/",
        ],
    },
    {
        "name": "direction_pages",
        "seed": "https://about.gitlab.com/direction/",
        "allowed_prefixes": [
            "https://about.gitlab.com/direction/",
        ],
    },
]


def normalize_url(url: str | None) -> str | None:
    if not url:
        return None

    split = urlsplit(url.strip())
    if split.scheme not in {"http", "https"} or not split.netloc:
        return None

    path = re.sub(r"/+", "/", split.path or "/")
    if not path.startswith("/"):
        path = f"/{path}"

    if "." not in path.rsplit("/", 1)[-1] and not path.endswith("/"):
        path = f"{path}/"

    normalized = urlunsplit(("https", split.netloc.lower(), path, "", ""))
    return normalized


def is_allowed_url(url: str, scope: dict[str, Any]) -> bool:
    if any(url.startswith(prefix) for prefix in scope["allowed_prefixes"]) is False:
        return False

    path = urlsplit(url).path.lower()
    if any(part in path for part in BLOCKED_PATH_PARTS):
        return False

    if any(path.endswith(ext) for ext in SKIPPED_EXTENSIONS):
        return False

    return True


def sanitize_filename(url: str) -> str:
    split = urlsplit(url)
    path = split.path.strip("/") or "root"
    raw_name = f"{split.netloc}_{path}".replace("/", "_")
    safe_name = re.sub(r"[^a-zA-Z0-9._-]+", "_", raw_name).strip("._")
    return f"{safe_name}.md"


def choose_markdown(result: Any) -> str:
    markdown = getattr(result, "markdown", None)
    candidates: list[str] = []

    if markdown is None:
        return ""

    for attribute in ("fit_markdown", "raw_markdown", "markdown_with_citations", "references_markdown"):
        value = getattr(markdown, attribute, None)
        if isinstance(value, str) and value.strip():
            candidates.append(value.strip())

    markdown_string = str(markdown).strip()
    if markdown_string:
        candidates.append(markdown_string)

    if not candidates:
        return ""

    unique_candidates = list(dict.fromkeys(candidates))
    return max(unique_candidates, key=len)


def is_bot_challenge(content: str) -> bool:
    lowered = content.lower()
    return any(marker in lowered for marker in BOT_CHALLENGE_MARKERS)


def extract_title(result: Any) -> str:
    metadata = getattr(result, "metadata", None) or {}
    title = metadata.get("title") or metadata.get("og:title") or metadata.get("twitter:title")
    return title.strip() if isinstance(title, str) else ""


def extract_internal_links(result: Any, scope: dict[str, Any]) -> list[str]:
    links = getattr(result, "links", None) or {}
    discovered: list[str] = []

    for link in links.get("internal", []):
        href = normalize_url(link.get("href"))
        if href and is_allowed_url(href, scope):
            discovered.append(href)

    return list(dict.fromkeys(discovered))


def save_markdown(filename: str, content: str) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    file_path = OUTPUT_DIR / filename
    with open(file_path, "w", encoding="utf-8") as file_handle:
        file_handle.write(content)


async def crawl_scope(crawler: AsyncWebCrawler, scope: dict[str, Any], config: CrawlerRunConfig) -> list[dict[str, Any]]:
    seed = normalize_url(scope["seed"])
    if not seed:
        raise ValueError(f"Invalid seed URL: {scope['seed']}")

    queue: deque[tuple[str, int]] = deque([(seed, 0)])
    queued = {seed}
    visited: set[str] = set()
    records: list[dict[str, Any]] = []

    print(f"\n[{scope['name']}] Starting crawl from {seed}")

    while queue and len(records) < MAX_PAGES_PER_SCOPE:
        url, depth = queue.popleft()
        queued.discard(url)

        if url in visited:
            continue

        visited.add(url)
        print(f"[{scope['name']}] Crawling depth={depth}: {url}")

        result: Any = await crawler.arun(url=url, config=config)
        effective_url = normalize_url(getattr(result, "redirected_url", None) or getattr(result, "url", None) or url) or url

        if getattr(result, "success", False) is False:
            error_message = getattr(result, "error_message", None) or "Unknown error"
            print(f"[{scope['name']}] Failed: {effective_url} -> {error_message}")
            records.append(
                {
                    "scope": scope["name"],
                    "url": effective_url,
                    "status": "failed",
                    "error": error_message,
                }
            )
            continue

        content = choose_markdown(result)
        title = extract_title(result)
        content_length = len(content)
        challenge_page = is_bot_challenge(content)
        filename = sanitize_filename(effective_url)

        if challenge_page:
            print(f"[{scope['name']}] Skipped bot challenge page: {effective_url}")
            records.append(
                {
                    "scope": scope["name"],
                    "url": effective_url,
                    "title": title,
                    "filename": filename,
                    "status": "bot_challenge",
                    "content_chars": content_length,
                }
            )
            continue

        if content:
            save_markdown(filename, content)
            status = "saved" if content_length >= MIN_CONTENT_CHARS else "saved_low_content"
            print(f"[{scope['name']}] Saved {content_length} chars -> {filename}")
        else:
            status = "empty"
            print(f"[{scope['name']}] Empty content: {effective_url}")

        records.append(
            {
                "scope": scope["name"],
                "url": effective_url,
                "title": title,
                "filename": filename,
                "status": status,
                "content_chars": content_length,
                "depth": depth,
            }
        )

        if depth >= MAX_DEPTH:
            continue

        for discovered_url in extract_internal_links(result, scope):
            if discovered_url not in visited and discovered_url not in queued:
                queued.add(discovered_url)
                queue.append((discovered_url, depth + 1))

    return records


async def crawl_all_scopes() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        word_count_threshold=0,
        excluded_tags=["nav", "footer", "aside", "script", "style", "header", "iframe"],
        remove_overlay_elements=True,
        process_iframes=False,
        wait_for="body",
    )

    manifest_records: list[dict[str, Any]] = []
    async with AsyncWebCrawler(verbose=VERBOSE_CRAWLER) as crawler:
        for scope in CRAWL_SCOPES:
            manifest_records.extend(await crawl_scope(crawler, scope, config))

    with open(MANIFEST_PATH, "w", encoding="utf-8") as file_handle:
        json.dump(manifest_records, file_handle, indent=2)

    saved_count = sum(1 for record in manifest_records if record["status"].startswith("saved"))
    failed_count = sum(1 for record in manifest_records if record["status"] == "failed")
    challenged_count = sum(1 for record in manifest_records if record["status"] == "bot_challenge")
    print("\nCrawl complete.")
    print(f"Saved pages: {saved_count}")
    print(f"Failed pages: {failed_count}")
    print(f"Bot-challenge pages: {challenged_count}")
    print(f"Manifest: {MANIFEST_PATH}")


if __name__ == "__main__":
    asyncio.run(crawl_all_scopes())
