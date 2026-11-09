# Local LLM Chatbot with Conversational Memory using LangChain

## Project Overview

The **Local LLM Chatbot with Conversational Memory** is a simple AI-powered chatbot developed using Python, Ollama, Gemma 3:1B, LangChain, and Streamlit.

The chatbot runs locally on the system and generates responses using a local Large Language Model (LLM). It also uses LangChain conversational memory to remember previous messages and maintain context throughout the conversation.

## Objectives

- To build a simple chatbot using a Local LLM.
- To integrate LangChain into the chatbot.
- To implement conversational memory.
- To maintain context from previous conversations.
- To create a user-friendly chatbot interface using Streamlit.

## Technologies Used

- **Python** – Programming language.
- **Ollama** – Runs the LLM locally.
- **Gemma 3:1B** – Local language model.
- **LangChain** – LLM application framework.
- **Streamlit** – Web-based chatbot interface.

## Features

- Local AI chatbot without requiring an external API key.
- Real-time conversational responses.
- LangChain-based conversation memory.
- Context-aware responses using previous messages.
- Interactive chat interface.
- Clear Chat option to reset the conversation.

## Project Structure

```text
Local-LLM-Chatbot/
│
├── app.py
├── requirements.txt
└── README.md
```

## Installation and Setup

### 1. Install Python

Download Python from:

https://www.python.org/downloads/

### 2. Install Ollama

Download Ollama from:

https://ollama.com/download

### 3. Download Gemma Model

Open the terminal and execute:

```bash
ollama pull gemma3:1b
```

### 4. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Navigate to the project folder:

```bash
cd Local-LLM-Chatbot
```

### 5. Create Virtual Environment

```bash
python -m venv venv
```

Activate the environment on Windows:

```bash
venv\Scripts\activate
```

### 6. Install Dependencies

```bash
pip install -r requirements.txt
```

### 7. Run the Application

```bash
streamlit run app.py
```

The chatbot will open in your web browser.

## How Conversational Memory Works

The chatbot uses LangChain's `RunnableWithMessageHistory` and `InMemoryChatMessageHistory` to maintain conversation history.

When a user sends a message:

1. The chatbot receives the user input.
2. LangChain retrieves previous conversation messages.
3. The conversation history is passed to the local LLM.
4. Gemma generates a context-aware response.
5. The new messages are stored in memory.

## Limitations

- The chatbot requires Ollama to be running locally.
- Response speed depends on system hardware.
- Conversation memory is temporary and stored in application memory.
- Previous conversations are not permanently saved after restarting the application.

## Future Enhancements

- Persistent conversation storage.
- Multiple chat sessions.
- Improved chatbot interface.
- Chat history management.
- Support for additional local LLM models.

## Conclusion

This project demonstrates how to build a simple local AI chatbot using Ollama and LangChain. By incorporating conversational memory, the chatbot can understand previous interactions and provide more relevant responses without depending on external LLM APIs.

---

**Developed using Python, Ollama, Gemma 3:1B, LangChain, and Streamlit.**
