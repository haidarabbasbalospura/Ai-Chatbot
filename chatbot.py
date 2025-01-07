import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationSummaryMemory
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Initialize LLM
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# Initialize session state variables
if 'buffer_memory' not in st.session_state:
    st.session_state.buffer_memory = ConversationSummaryMemory(llm=llm, return_messages=True)

if "messages" not in st.session_state:  # Initialize chat history
    st.session_state.messages = [
        {"role": "assistant", "content": "How can I help you today?"}
    ]

system_message = """Your name is ZoroBot. Your Creator is Haiderabbas, he is learning about GenAI. You have been created as a learning assistant for MantiQ Infotech's Generative AI Bootcamp. you funnily explain the concept of Anything, using unusual examples.
"""

if "is_generating" not in st.session_state:  # Track if assistant is generating response
    st.session_state.is_generating = False

# Initialize ConversationChain
conversation = ConversationChain(memory=st.session_state.buffer_memory, llm=llm)

# UI Setup
st.title("🗣️ Conversational Chatbot")
st.subheader("㈻ Simple Chat Interface for LLMs by Zoro")

# Display all chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Handle assistant's "Thinking..." state
if st.session_state.is_generating:
    with st.chat_message("assistant"):
        with st.spinner("The assistant is thinking... Please wait."):
            # Construct input with system message and user input as a single string
            full_prompt = f"{system_message}\nUser: {st.session_state.messages[-1]['content']}"
            message = [
                {"role": "system", "content": system_message},
                {"role": "user", "content": st.session_state.messages[-1]['content']}
            ]
            response = conversation.run(message)
    
    # Add assistant response
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.session_state.is_generating = False
    st.rerun()

# User input is only enabled if not generating a response
if not st.session_state.is_generating:
    if prompt := st.chat_input("Your question"):
        # Add user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Lock user input and trigger assistant response
        st.session_state.is_generating = True
        st.rerun()



# import streamlit as st
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain.chains import ConversationChain
# from langchain.chains.conversation.memory import ConversationSummaryMemory
# from dotenv import load_dotenv
# import os

# # Load environment variables
# load_dotenv()
# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# # Initialize LLM
# llm = ChatGoogleGenerativeAI(
#     model="gemini-pro",
#     prefix_messages=[
#         {
#             "role": "system",
#             "content": """You are Zoro, an AI assistant created by Zoro. You are helpful, knowledgeable, and always aim to provide accurate information. 
#             When introducing yourself, make sure to mention that you were created by Zoro.
#             Stay in character throughout the conversation."""
#         }
#     ]
# )

# # Initialize session state variables
# if 'buffer_memory' not in st.session_state:
#     st.session_state.buffer_memory = ConversationSummaryMemory(llm=llm, return_messages=True)

# if "messages" not in st.session_state:  # Initialize chat history
#     st.session_state.messages = [
#         {"role": "assistant", "content": "Hello! I'm Zoro, an AI assistant created by Zoro. How can I help you today?"}
#     ]

# if "is_generating" not in st.session_state:  # Track if assistant is generating response
#     st.session_state.is_generating = False

# # Initialize ConversationChain
# conversation = ConversationChain(memory=st.session_state.buffer_memory, llm=llm)

# # UI Setup
# st.title("🗣️ Conversational Chatbot")
# st.subheader("㈻ Simple Chat Interface for LLMs by Zoro")

# # Display all chat messages
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.write(message["content"])

# # Handle assistant's "Thinking..." state
# if st.session_state.is_generating:
#     with st.chat_message("assistant"):
#         with st.spinner("Zoro is thinking... Please wait."):
#             response = conversation.predict(input=st.session_state.messages[-1]["content"])
    
#     # Add assistant response
#     st.session_state.messages.append({"role": "assistant", "content": response})
#     st.session_state.is_generating = False
#     st.rerun()

# # User input is only enabled if not generating a response
# if not st.session_state.is_generating:
#     if prompt := st.chat_input("Your question"):
#         # Lock user input
#         st.session_state.is_generating = True
#         st.session_state.messages.append({"role": "user", "content": prompt})
#         st.rerun()

# import streamlit as st
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain.chains import ConversationChain
# from langchain.chains.conversation.memory import ConversationSummaryMemory
# from dotenv import load_dotenv
# import os

# # Load environment variables
# load_dotenv()
# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# # Initialize LLM
# llm = ChatGoogleGenerativeAI(model="gemini-pro")

# # Initialize session state variables
# if 'buffer_memory' not in st.session_state:
#     st.session_state.buffer_memory = ConversationSummaryMemory(llm=llm, return_messages=True)

# if "messages" not in st.session_state:  # Initialize chat history
#     st.session_state.messages = [
#         {"role": "assistant", "content": "How can I help you today?"}
#     ]

# # Temporary variable for assistant's pending response
# if "pending_response" not in st.session_state:
#     st.session_state.pending_response = None

# # Temporary variable to manage thinking state
# if "is_thinking" not in st.session_state:
#     st.session_state.is_thinking = False

# # Initialize ConversationChain
# conversation = ConversationChain(memory=st.session_state.buffer_memory, llm=llm)

# # UI Setup
# st.title("🗣️ Conversational Chatbot")
# st.subheader("㈻ Simple Chat Interface for LLMs by Zoro")

# # Display all chat messages
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.write(message["content"])

# # Handle new user input
# if prompt := st.chat_input("Your question"):
#     # Immediately display the user input in the UI
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     st.session_state.is_thinking = True  # Trigger thinking state
#     st.rerun()

# # Display the assistant's "Thinking..." box if is_thinking is True
# if st.session_state.is_thinking:
#     with st.chat_message("assistant"):
#         with st.spinner("Thinking..."):
#             st.session_state.pending_response = conversation.predict(input=st.session_state.messages[-1]["content"])
#     # Update state after response
#     st.session_state.messages.append({"role": "assistant", "content": st.session_state.pending_response})
#     st.session_state.pending_response = None  # Clear pending response
#     st.session_state.is_thinking = False  # End thinking state
#     st.rerun()




