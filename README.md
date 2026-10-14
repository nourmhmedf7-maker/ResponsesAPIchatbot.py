# Python AI Chatbot — Responses API

A simple conversational AI chatbot built with Python using the OpenAI Responses API through Groq.

This project is part of my AI Engineering learning journey, where I am practicing Python fundamentals and learning how to integrate AI models into applications.

## Features

- Interactive command-line chat.
- Conversation history to maintain context across messages.
- AI model integration using the OpenAI Python SDK.
- Environment variables for API key configuration.
- Simple exit command to end the conversation.

## Technologies Used

- Python
- OpenAI Python SDK
- OpenAI Responses API
- Groq API
- python-dotenv
- Git and GitHub

## Getting Started

### 1. Clone the Repository

```bash
git clone YOUR_REPOSITORY_URL
cd python-responses-api-chatbot
```

### 2. Install Dependencies

```bash
pip install openai python-dotenv
```

### 3. Configure Environment Variables

Create a `.env` file in the project directory and add your Groq API key:

```env
grok_apikey=your_api_key_here
```

Replace `your_api_key_here` with your actual API key.

**Important:** Never upload your `.env` file or expose your API key publicly.

### 4. Run the Chatbot

```bash
python main.py
```

Start chatting with the model in your terminal. Type `exit` to quit.

## What I Learned

- Integrating an AI model into a Python application.
- Working with API requests and responses.
- Managing conversation history using lists and dictionaries.
- Using environment variables to handle API credentials.
- Building an interactive command-line application.

## Future Improvements

- Add error handling.
- Implement streaming responses.
- Explore tool calling and additional Responses API capabilities.

## Author

Created as part of my journey toward becoming an AI Engineer.

Feel free to explore the project and follow my progress!