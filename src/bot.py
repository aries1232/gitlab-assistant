import os
import json
from typing import List, Dict, Any, Optional
from dotenv import load_dotenv

from llama_index.core import VectorStoreIndex, QueryBundle
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.schema import NodeWithScore
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.google_genai import GoogleGenAI
from llama_index.core import PromptTemplate
from llama_index.core.response_synthesizers import get_response_synthesizer
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.chat_engine import CondenseQuestionChatEngine
from llama_index.core.base.llms.types import ChatMessage, MessageRole

try:
    from src.chroma_client import get_chroma_client
except ModuleNotFoundError:
    from chroma_client import get_chroma_client

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_LLM_MODEL = "gemini-3.1-flash-lite-preview"
EMBED_MODEL = os.getenv("EMBED_MODEL", "BAAI/bge-base-en-v1.5")

class GitlabAssistant:
    def __init__(self):
        self.llm = GoogleGenAI(model=GOOGLE_LLM_MODEL, api_key=GOOGLE_API_KEY, max_tokens=400)
        self.embed_model = HuggingFaceEmbedding(model_name=EMBED_MODEL)

        self.db = get_chroma_client()
            
        self.chroma_collection = self.db.get_or_create_collection("gitlab_handbook")
        self.vector_store = ChromaVectorStore(chroma_collection=self.chroma_collection)
        
        # Load Vector Store Index
        self.index = VectorStoreIndex.from_vector_store(
            vector_store=self.vector_store,
            embed_model=self.embed_model
        )
        
        # Setup pure vector retriever
        self.retriever = VectorIndexRetriever(
            index=self.index,
            similarity_top_k=3,
        )
        
        # Strict Guardrails Prompt with JSON Context block
        self.bot_prompt = PromptTemplate(
            "You are a helpful and knowledgeable assistant for GitLab employees and aspiring candidates. "
            "Your main task is to answer questions strictly based on the provided context retrieved from the GitLab Handbook and the conversation history.\n\n"
            "Current Conversation Summary/History (JSON):\n"
            "---------------------\n"
            "{history_json}\n"
            "---------------------\n\n"
            "Retrieved Handbook Context:\n"
            "---------------------\n"
            "{context_str}\n"
            "---------------------\n\n"
            "User Question: {query_str}\n\n"
            "Assistant Answer:"
        )

        # Summarization Prompt
        self.summarize_prompt = PromptTemplate(
            "You are an expert at distilling conversations into concise, structured summaries. "
            "Given the following long conversation history in JSON format, produce a new JSON summary that captures the essence of what has been discussed, key facts learned, and the current state of the request.\n"
            "History JSON:\n{history_json}\n\n"
            "Respond ONLY with a valid JSON containing a field 'summary' and 'key_point_list'."
        )
        
        # Assemble Response Synthesizer
        self.response_synthesizer = get_response_synthesizer(
            llm=self.llm,
            text_qa_template=self.bot_prompt,
            response_mode="compact" # type: ignore
        )
        
        # Complete Query Engine
        self.query_engine = RetrieverQueryEngine(
            retriever=self.retriever,
            response_synthesizer=self.response_synthesizer,
        )

        # Conversational Chat Engine (History-aware)
        self.chat_engine = CondenseQuestionChatEngine.from_defaults(
            query_engine=self.query_engine,
            llm=self.llm,
            verbose=True
        )

    def summarize_history(self, chat_history: List[Dict[str, Any]]) -> str:
        """Summarizes history using the configured LLM model."""
        history_str = json.dumps(chat_history, indent=2)
        # Using the instance's configured LLM (gemini-3.1-flash-lite-preview)
        response = self.llm.complete(self.summarize_prompt.format(history_json=history_str))
        return str(response)

    def _convert_history(self, chat_history: List[Dict[str, Any]]) -> List[ChatMessage]:
        """Converts raw list dicts to LlamaIndex ChatMessage list."""
        messages = []
        for msg in chat_history:
            role = MessageRole.USER if msg["role"] == "user" else MessageRole.ASSISTANT
            messages.append(ChatMessage(role=role, content=msg["content"]))
        return messages

    def query(self, question: str, chat_history: Optional[List[Dict[str, Any]]] = None):
        try:
            # Prepare context
            history_json = "{}"
            processed_history = chat_history if chat_history else []

            # If history is long (e.g., > 20 messages), condense it
            if len(processed_history) >= 20:
                summary = self.summarize_history(processed_history)
                history_json = json.dumps({"is_summarized": True, "context": summary})
            else:
                history_json = json.dumps(processed_history)

            # Update the prompt template temporarily with the history JSON
            # This is a manual injection for demonstration of your JSON idea
            # Although ChatEngine handles condensation, we'll use query_engine directly for explicit JSON control
            
            response = self.query_engine.query(
                QueryBundle(
                    query_str=question,
                    custom_embedding_strs=[question]
                )
            )
            
            # Format sources
            sources = []
            if hasattr(response, 'source_nodes'):
                for source_node in response.source_nodes:
                    url = source_node.node.metadata.get('url', 'Unknown URL')
                    score = source_node.score
                    sources.append({"url": url, "score": score, "text_preview": source_node.node.text[:100] + "..."}) # type: ignore
                
            return {
                "answer": str(response), # type: ignore
                "sources": sources
            }
        except Exception as e:
             return {
                "answer": f"An error occurred: {str(e)}",
                "sources": []
            }

    def stream_query(self, question: str, chat_history: Optional[List[Dict[str, Any]]] = None):
        """Streaming version using the JSON-history logic."""
        try:
            processed_history = chat_history if chat_history else []
            
            # Condensation logic
            if len(processed_history) >= 20: 
                summary = self.summarize_history(processed_history)
                # Instead of the full list, we'll pass a single "system" or "user" message containing the JSON summary
                # to the chat engine so it doesn't lose context but saves tokens.
                condensed_history = [
                    {"role": "user", "content": f"The conversation so far has been summarized into this JSON context: {summary}"}
                ]
                llama_history = self._convert_history(condensed_history)
            else:
                llama_history = self._convert_history(processed_history)

            return self.chat_engine.stream_chat(question, chat_history=llama_history)
        except Exception as e:
            print(f"Streaming error: {e}")
            return None

if __name__ == "__main__":
    import streamlit as st
    
    st.set_page_config(page_title="GitLab Assistant", page_icon="🦊")
    st.title(" GitLab Assistant")
    
    # Initialize assistant only once
    if "assistant" not in st.session_state:
        with st.spinner("Initializing AI Models..."):
            st.session_state.assistant = GitlabAssistant()
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("Ask about GitLab's handbook..."):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("assistant"):
            with st.spinner("Searching Handbook..."):
                response_data = st.session_state.assistant.query(prompt)
                answer = response_data["answer"]
                st.markdown(answer)
                
                # Show sources in an expander
                if response_data["sources"]:
                    with st.expander("📚 Sources Referenced"):
                        for src in response_data["sources"]:
                            st.write(f"- [{src['url']}]({src['url']}) (Score: {src['score']:.2f})")
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": answer})
