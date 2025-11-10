import streamlit as st
import asyncio
import os
from typing import Dict, Any
from dataclasses import dataclass
from enum import Enum
from dotenv import load_dotenv

# --- Basic Configuration ---
st.set_page_config(
    page_title="Synapse AI",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="expanded"
)

# --- Load Environment Variables for API Key ---
load_dotenv()

# --- CSS Styling ---
st.markdown("""
<style>
    /* ... existing CSS ... */
    .main { background-color: #0E1117; }
    [data-testid="stSidebar"] {
        background-color: #1a1a3a;
        border-right: 2px solid #8A2BE2;
    }
    .st-emotion-cache-16txtl3 h2 {
        color: #ffffff;
        text-shadow: 0 0 5px #00aaff;
    }
    .st-emotion-cache-4oy321 {
        width: 2.5rem;
        height: 2.5rem;
        font-size: 1.5rem;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 50%;
    }
    .stButton>button {
        width: 100%; border-radius: 10px; border: 1px solid #ff4b4b;
        color: #ff4b4b; background-color: transparent; transition: all 0.2s ease-in-out;
    }
    .stButton>button:hover {
        border-color: #ffffff; color: #ffffff; background-color: #ff4b4b;
    }
</style>
""", unsafe_allow_html=True)


# --- API Availability Check ---
try:
    import google.generativeai as genai
    from google.generativeai.types import GenerationConfig
    GEMINI_AVAILABLE = True
except ImportError:
    st.error("The 'google-generativeai' library is not installed. Please run 'pip install google-generativeai'.")
    GEMINI_AVAILABLE = False

# --- Core Agent Logic & Data Structures ---
class AgentRole(Enum):
    COORDINATOR = "coordinator"; RESEARCHER = "researcher"; ANALYZER = "analyzer"; EXECUTOR = "executor"

@dataclass
class Message:
    role: str; content: str

class MCPAgent:
    def __init__(self, role: AgentRole, api_key: str = None):
        self.role = role
        self.model = None
        if GEMINI_AVAILABLE and api_key:
            try:
                genai.configure(api_key=api_key)
                self.model = genai.GenerativeModel(model_name='gemini-1.5-flash', generation_config=GenerationConfig(temperature=0.8))
            except Exception as e:
                st.error(f"Failed to initialize the AI model. Check your API key. Error: {e}")
        
    async def stream_message(self, message: str):
        if not self.model:
            simulated_response = f"This is a simulated stream from the **{self.role.value}** agent."
            for word in simulated_response.split():
                yield word + " "; await asyncio.sleep(0.05)
            return
        
        contextual_prompt = f"You are an advanced AI agent. Your assigned role is: **{self.role.value}**. Provide a helpful and detailed response to the user's request.\n\nUser Request: \"{message}\""
        try:
            response_stream = await self.model.generate_content_async(contextual_prompt, stream=True)
            async for chunk in response_stream:
                if chunk.text: yield chunk.text
        except Exception as e:
            yield f"Sorry, an error occurred: {e}"

# --- Sidebar Controls ---
with st.sidebar:
    st.markdown("## ⚡Synapse AI Controls")
    agent_roles = {
        "RESEARCHER": "Specializes in finding, correlating, and synthesizing information.",
        "ANALYZER": "Focuses on interpreting data, identifying patterns, and generating insights.",
        "COORDINATOR": "Manages complex tasks by breaking them down and orchestrating agents.",
        "EXECUTOR": "Concentrates on performing actions, running code, and validating results."
    }
    selected_role_name = st.selectbox("Select an Agent Role:", options=list(agent_roles.keys()))
    agent_role_enum = AgentRole[selected_role_name]
    st.markdown("---")
    st.markdown(f"**Role Description:**")
    st.info(agent_roles[selected_role_name])
    st.markdown("---")
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()

# --- Main Chat Interface ---
st.title("⚡Synapse AI Chat")
st.write("Interact with a specialized AI agent in real-time.")

# --- Agent Initialization & State Management ---
# Initialize chat history ONCE
if "messages" not in st.session_state:
    st.session_state.messages = []

# Initialize or update the agent based on sidebar selection
API_KEY = os.environ.get("GOOGLE_API_KEY")
st.session_state.agent = MCPAgent(role=agent_role_enum, api_key=API_KEY)

# Display avatars
user_avatar_url = "https://img.icons8.com/ios-glyphs/90/ffffff/user-male-circle.png"
bot_avatar_url = "https://img.icons8.com/fluency-systems-filled/96/ffffff/bot.png"

for message in st.session_state.messages:
    avatar = user_avatar_url if message.role == "user" else bot_avatar_url
    with st.chat_message(message.role, avatar=avatar):
        st.markdown(message.content)

# --- User Input and Streaming Response ---
if prompt := st.chat_input(f"Ask the {agent_role_enum.name} agent..."):
    # Add and display user message
    st.session_state.messages.append(Message(role="user", content=prompt))
    with st.chat_message("user", avatar=user_avatar_url):
        st.markdown(prompt)

    # Display assistant's streaming response
    with st.chat_message("assistant", avatar=bot_avatar_url):
        response = st.write_stream(st.session_state.agent.stream_message(prompt))
    
    # Add complete assistant response to history
    st.session_state.messages.append(Message(role="assistant", content=response))
    
