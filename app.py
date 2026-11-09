import streamlit as st
import uuid

from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory


st.set_page_config(
    page_title="Local LLM Chatbot",
    page_icon="💬",
    layout="centered"
)


st.title("Local LLM Chatbot")
st.write("Chat with an AI assistant powered by Gemma and LangChain Memory.")


if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "messages" not in st.session_state:
    st.session_state.messages = []

store = {}

def get_session_history(session_id):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]


llm = ChatOllama(
    model="gemma3:1b",
    temperature=0.7
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant. Answer clearly and politely."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{question}")
])

chain = prompt | llm

chatbot = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="question",
    history_messages_key="history"
)

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input("Ask me anything...")

if user_input:

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.write(user_input)

    try:
        with st.spinner("Thinking..."):

            response = chatbot.invoke(
                {"question": user_input},
                config={
                    "configurable": {
                        "session_id": st.session_state.session_id
                    }
                }
            )

            answer = response.content

        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })

        with st.chat_message("assistant"):
            st.write(answer)

    except Exception as e:
        st.error(f"Error: {e}")

if st.button("Clear Chat"):
    session_id = st.session_state.session_id

    if session_id in store:
        store[session_id].clear()

    st.session_state.messages = []
    st.rerun()