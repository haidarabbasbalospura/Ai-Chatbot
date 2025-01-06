import streamlit as st
from streamlit_chat import message
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory, ConversationSummaryMemory
from dotenv import load_dotenv
load_dotenv()
import os

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(model = "gemini-pro")

# Initialize session state variables
if 'buffer_memory' not in st.session_state:
    # st.session_state.buffer_memory = ConversationBufferWindowMemory(k=3, return_messages=True)
    st.session_state.buffer_memory = ConversationSummaryMemory(llm=llm, return_messages=True)

if "messages" not in st.session_state.keys(): # Initialize the chat message history
    st.session_state.messages = [
        {"role": "assistant", "content": "How can I help you today?"}
    ]

# Initialize ChatOpenAI and ConversationChain
# llm = ChatOpenAI(model_name="gpt-4o-mini")
# llm = ChatOpenAI(model = "meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo",
#                       openai_api_key = st.secrets["TOGETHER_API_KEY"] , ## use your key
#                       openai_api_base = "https://api.together.xyz/v1"

# )

conversation = ConversationChain(memory=st.session_state.buffer_memory, llm=llm)

# Create user interface
st.title("🗣️ Conversational Chatbot")
st.subheader("㈻ Simple Chat Interface for LLMs by Zoro")


if prompt := st.chat_input("Your question"): # Prompt for user input and save to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

for message in st.session_state.messages: # Display the prior chat messages
    with st.chat_message(message["role"]):
        st.write(message["content"])

# If last message is not from assistant, generate a new response
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = conversation.predict(input = prompt)
            st.write(response)
            message = {"role": "assistant", "content": response}
            st.session_state.messages.append(message) # Add response to message history




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
# if "buffer_memory" not in st.session_state:
#     st.session_state.buffer_memory = ConversationSummaryMemory(llm=llm, return_messages=True)

# if "messages" not in st.session_state:
#     # Start with an assistant greeting message
#     st.session_state.messages = [
#         {"role": "assistant", "content": "Greetings! How may I assist you today?"}
#     ]

# # Initialize ConversationChain
# conversation = ConversationChain(memory=st.session_state.buffer_memory, llm=llm)

# # Create user interface
# st.title("🗣️ Conversational Chatbot")
# st.subheader("㈻ Simple Chat Interface for LLMs by Build Fast with AI")

# # Display the chat history (including the user's most recent input)
# for i, message in enumerate(st.session_state.messages):
#     with st.chat_message(message["role"]):
#         st.write(message["content"])

# # Prompt for user input
# if prompt := st.chat_input("Your question"):
#     # Append user input to the message history and display it immediately
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user"):
#         st.write(prompt)

#     # Generate a response
#     with st.chat_message("assistant"):
#         with st.spinner("Thinking..."):
#             response = conversation.predict(input=prompt)
#             st.write(response)
    
#     # Append the assistant's response to the message history
#     st.session_state.messages.append({"role": "assistant", "content": response})


