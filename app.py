import streamlit as st
import os
import time
from datetime import datetime, timedelta
from src.bot import GitlabAssistant
from src.supabase_client import supabase_db

st.set_page_config(
    page_title="GitLab AI Assistant",
    page_icon="",
    layout="centered"
)

# Custom CSS for Hero Text and Animations
st.markdown("""
<style>
    /* Hero Section Styling */
    .hero-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 40px 0px;
        text-align: center;
    }
    .hero-title {
        font-size: 3.5rem !important;
        font-weight: 800 !important;
        background: linear-gradient(90deg, #FC6D26, #E24329, #FCA326);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
    }
    .hero-subtitle {
        font-size: 1.2rem;
        color: #666;
        margin-bottom: 30px;
    }
    
    /* Pulse Animation for Thinking state */
    @keyframes pulse {
        0% { opacity: 0.3; }
        50% { opacity: 0.7; }
        100% { opacity: 0.3; }
    }
    .thinking-box {
        background-color: transparent;
        padding: 5px 0px;
        margin-bottom: 10px;
        animation: pulse 2s infinite ease-in-out;
        display: flex;
        align-items: center;
        gap: 8px;
        font-style: italic;
        font-size: 0.9rem;
        color: #888;
    }
</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
    <div class="hero-container">
        <h1 class="hero-title">GitLab Handbook AI</h1>
        <p class="hero-subtitle">Your intelligent companion for GitLab engineering, culture, and direction.</p>
    </div>
""", unsafe_allow_html=True)

# Initialize the assistant instance (memoized for performance in Streamlit)
@st.cache_resource
def get_assistant():
    return GitlabAssistant()

assistant = get_assistant()

# --- Supabase Session Management ---
if "session_id" not in st.session_state:
    # A new session is created every time the app/tab is first loaded
    st.session_state.session_id = supabase_db.create_session()
    st.session_state.messages = []
    
    # Optional: If you wanted to load existing history from Supabase:
    # st.session_state.messages = supabase_db.get_messages(st.session_state.session_id)

if "messages" not in st.session_state:
    st.session_state.messages = []
# -----------------------------------

# --- Rate Limiting Logic ---
if "query_timestamps" not in st.session_state:
    st.session_state.query_timestamps = []

def get_wait_time():
    now = datetime.now()
    # Keep only timestamps within the last 60 seconds
    st.session_state.query_timestamps = [
        ts for ts in st.session_state.query_timestamps 
        if (now - ts).total_seconds() < 60
    ]
    if len(st.session_state.query_timestamps) >= 5:
        oldest_ts = st.session_state.query_timestamps[0]
        return int(60 - (now - oldest_ts).total_seconds())
    return 0
# ---------------------------

# Quick Start Questions
if not st.session_state.messages:
    st.markdown("#### Ask me anything about GitLab's handbook!")
    suggestions = [
        "What is GitLab's Build in Public philosophy?",
        "How does the engineering team handle architectural design?",
        "What are the core CREDIT values at GitLab?",
        "How does GitLab manage a fully remote workforce?",
        "What is the current product direction for AI-powered features?"
    ]
    for suggestion in suggestions:
        if st.button(suggestion, use_container_width=True):
            st.session_state.quick_query = suggestion
            st.rerun()

# Display existing chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Check for new query
query = st.chat_input("Ask a question...")
if "quick_query" in st.session_state and st.session_state.quick_query:
    query = st.session_state.quick_query
    st.session_state.quick_query = None

if query:
    wait_time = get_wait_time()
    
    if wait_time > 0:
        st.warning(f"*Whoa there, speedy!* You've hit the 5 queries/min limit. Let the hamster in my brain catch its breath for **{wait_time} seconds** before asking again.")
    else:
        # Add timestamp for rate limiting
        st.session_state.query_timestamps.append(datetime.now())

        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": query})
        
        # --- Sync user message with Supabase ---
        supabase_db.save_message(st.session_state.session_id, "user", query)
        # ----------------------------------------
        
        # IMMEDIATELY RERUN to clear suggestions and show the user message in the history loop above
        st.rerun()

# Logic to handle the assistant's response after a rerun
if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
    current_query = st.session_state.messages[-1]["content"]

    # Process response
    with st.chat_message("assistant"):
        # Custom "Thinking" Animation Box
        thinking_placeholder = st.empty()
        with thinking_placeholder:
            st.markdown("""
                <div class="thinking-box">
                    <span>✨</span>
                    <span>Thinking...</span>
                </div>
            """, unsafe_allow_html=True)
            
        full_response = ""
        
        # Stream from Assistant
        # Note: We pass the history excluding the current query to bot
        stream_response = assistant.stream_query(current_query, chat_history=st.session_state.messages[:-1])
        
        # Remove the animated thinking box once the stream starts
        thinking_placeholder.empty()

        response_container = st.empty()
        
        if stream_response:
            # Stream the token stream to front-end
            try:
                for token in stream_response.response_gen:
                    full_response += token
                    response_container.markdown(full_response + "▌")
            except Exception as e:
                # Handle cases where Gemini terminates the stream early (e.g., safety, finish_reason etc.)
                if "Response was terminated early" in str(e):
                    full_response += "\n\n*(Note: The response was partially generated and terminated early by the model, likely due to safety filters or context limits.)*"
                else:
                    full_response += f"\n\n*(Error during streaming: {str(e)})*"
            
            response_container.markdown(full_response)
            
            # For chat_engine, sources are in source_nodes
            sources = []
            if hasattr(stream_response, 'source_nodes'):
                for source_node in stream_response.source_nodes:
                    url = source_node.node.metadata.get('url', 'Unknown URL')
                    score = source_node.score if hasattr(source_node, 'score') else 0.0
                    sources.append({"url": url, "score": score, "text_preview": source_node.node.text[:100] + "..."})
            
            # Guardrail & Transparency feature: Show sources used
            if sources:
                with st.expander("📚 Sources & Confidence"):
                    for src in sources:
                        st.markdown(f"**Relevance:** `{src['score']:.2f}` | **Link:** [{src['url']}]({src['url']})")
                        st.markdown(f"> *{src['text_preview']}*")
            
            # Save assistant message
            st.session_state.messages.append({"role": "assistant", "content": full_response, "sources": sources})
            
            # --- Sync assistant message with Supabase ---
            supabase_db.save_message(st.session_state.session_id, "assistant", full_response, sources)
            # ---------------------------------------------
        else:
            error_msg = "Sorry, I encountered an error generating a response."
            response_container.error(error_msg)
            st.session_state.messages.append({"role": "assistant", "content": error_msg})
