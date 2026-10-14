# Responses API Learning Project

A hands-on Python project focused on learning and experimenting with the OpenAI Responses API through Groq.

This project is part of my journey toward becoming an AI Engineer. I started with a simple conversational chatbot and will continue expanding it as I learn more Responses API capabilities.

## Current Features

- Interactive command-line chatbot.
- Conversation history using Python lists and dictionaries.
- Multi-turn conversations with an AI model.
- API integration using the OpenAI Python SDK.
- Environment variable configuration for API credentials.

## Technologies Used

- Python
- OpenAI Python SDK
- Responses API
- Groq API
- python-dotenv

## Getting Started

### 1. Install Dependencies

```bash
pip install openai python-dotenv
```

### 2. Configure Environment Variables

Create a `.env` file in the project directory:

```env
grok_apikey=your_api_key_here
```

Replace `your_api_key_here` with your actual Groq API key.

**Important:** Never upload your `.env` file or expose your API key publicly.

### 3. Run the Project

```bash
python main.py
```

Type `exit` to end the conversation.

## Learning Roadmap

As I continue exploring the Responses API, I plan to experiment with:

- Streaming responses
- Tool calling
- Web search integration
- Reasoning models and capabilities
- More advanced API interactions

## What I'm Learning

Through this project, I'm developing practical skills in Python, API integration, conversation management, and AI application development.

This repository will evolve as I learn and implement new concepts.

## Author

Created as part of my journey toward becoming an AI Engineer.

## Getting Started

### 1. Install uv

Install `uv`, the Python package and project manager used in this project.

Follow the official installation guide: https://docs.astral.sh/uv/getting-started/installation/

### 2. Clone the Repository

```bash
git clone https://github.com/nourmhmedf7-maker/ResponsesAPIchatbot.py.git
cd ResponsesAPIchatbot.py
```

### 3. Install Dependencies

Run the following command in the project directory:

```bash
uv sync
```

This command creates or updates the project's virtual environment and installs the dependencies specified in `uv.lock`.

### 4. Configure Environment Variables

Create a `.env` file in the project directory and add your Groq API key:

```env
grok_apikey=your_api_key_here
```

Replace `your_api_key_here` with your actual API key.

**Important:** Never upload your `.env` file or expose your API key publicly.

### 5. Run the Project

```bash
uv run python main.py
```

Replace `main.py` with the actual Python filename if it is different.



