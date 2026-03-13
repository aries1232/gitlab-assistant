# GitLab Handbook GenAI Chatbot 🦊

This repository contains a full-stack, transparent Generative AI chatbot built for GitLab employees and aspiring candidates. It interacts directly with the GitLab Handbook and Direction pages, retrieving context natively to prevent LLM hallucinations.

## Key Features
* 🕷 **Crawl4AI Data Pipeline:** Fast, intelligent markdown scraping.
* 🧠 **Google GenAI LLM & Embeddings:** Built with Gemini Flash and Gemini Embeddings via the current Google GenAI SDK.
* 🔍 **Hybrid Retrieval Engine & ChromaDB:** Vectorized search persistence using ChromaDB and Reciprocal Rank Fusion (hybrid semantic + string matching context).
* 🛡 **Strict Guardrails:** Configured LlamaIndex `PromptTemplates` restrict responses to retrieved handbook context exclusively.
* 👁 **Radical Transparency UX:** The UI visibly displays the confidence score & exact sources for every response generated. 

## Project Architecture & Strategy (Write-Up)
Our approach stems from the "build in public" philosophy. Emphasizing **Product Thinking**, the immediate concern with internal knowledge bots is "hallucinations"—LLMs confidently making up employee processes.

1. **Ingestion:** We utilize `crawl4ai` asynchronously processing the GitLab handbook pages, extracting text and metadata.
2. **Indexing:** `LlamaIndex` splits the documents natively, generating dense vectors via Google's `text-embedding-004` (1500 dimensions) and persisting them to disk via `ChromaDB`.
3. **Retrieval & RAG:** When a user queries Streamlit, it routes to `VectorStoreIndex`. We construct strict prompts requiring the `Gemini Flash` model to only answer based on context or politely refuse.
4. **Transparency:** Every fetched chunk is returned natively to Streamlit and parsed via Expanders (`st.expander`), giving users a UI to verify exactly where the bot sourced its answers.

## Local Setup

### Prerequisites
* Python 3.9+
* A Google AI Studio API Key (Gemini)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/gitlab-genai-chatbot.git
   cd gitlab-genai-chatbot
   ```
2. Create and activate a Virtual Environment
   ```bash
   python -m venv venv
   source venv/bin/activate # Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure `.env` file:
   Retrieve your API key from Google AI Studio and place it in the `.env` file.
   ```
   GOOGLE_API_KEY=your_key_here
   GOOGLE_LLM_MODEL=gemini-2.0-flash
   GOOGLE_EMBED_MODEL=gemini-embedding-001
   ```

   To use Chroma Cloud instead of the local persistent database, also set:
   ```
   CHROMA_HOST=api.trychroma.com
   CHROMA_TENANT=your_tenant_id
   CHROMA_DATABASE=your_database_name
   CHROMA_API_KEY=your_chroma_api_key
   ```

### Running the Application
**Step 1:** Ingest Data
Before running the bot, populate the local ChromaDB database by running the crawl script:
```bash
python src/ingest_data.py
```
*(Note: Initial ingestion may take several minutes depending on the quantity of crawled pages. If you use Chroma Cloud, the app now connects through the official cloud client path.)*

**Step 2:** Start the Streamlit Application
```bash
streamlit run app.py
```

## Deployment
This app handles Streamlit Community Cloud out-of-the-box.
1. Push this repository to GitHub. 
2. Go to Steamlit Community Cloud and link this repo (`app.py` as entrypoint).
3. Insert `GOOGLE_API_KEY` into Streamlit's secrets manager.
