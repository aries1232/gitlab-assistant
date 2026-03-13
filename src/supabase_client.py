import os
import uuid
from typing import List, Dict, Any, Optional
from datetime import datetime
from supabase import create_client, Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

class SupabaseChatDB:
    def __init__(self):
        if not SUPABASE_URL or not SUPABASE_KEY:
            self.client = None # type: ignore
            print("Warning: Supabase credentials missing. Persistence disabled.")
        else:
            self.client: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

    def is_connected(self) -> bool:
        return self.client is not None

    def create_session(self) -> str:
        """Creates a new session and returns the session_id (UUID string)."""
        if not self.is_connected():
            return str(uuid.uuid4())
        
        session_id = str(uuid.uuid4())
        try:
            self.client.table("sessions").insert({"id": session_id}).execute()
        except Exception as e:
            print(f"Error creating session in Supabase: {e}")
            # Fallback to local-only if DB write fails
        return session_id

    def save_message(self, session_id: str, role: str, content: str, sources: Optional[List[Dict[str, Any]]] = None):
        """Persists a chat message associated with a session."""
        if not self.is_connected():
            return

        try:
            data = {
                "session_id": session_id,
                "role": role,
                "content": content,
                "sources": sources if sources else []
            }
            self.client.table("messages").insert(data).execute()
        except Exception as e:
            print(f"Error saving message to Supabase: {e}")

    def get_messages(self, session_id: str) -> List[Dict[str, Any]]:
        """Retrieves all messages for a specific session sorted by time."""
        if not self.is_connected():
            return []

        try:
            response = self.client.table("messages") \
                .select("*") \
                .eq("session_id", session_id) \
                .order("created_at") \
                .execute()
            return response.data # type: ignore
        except Exception as e:
            print(f"Error fetching messages from Supabase: {e}")
            return []

# Initialize a global instance for convenience
supabase_db = SupabaseChatDB()
