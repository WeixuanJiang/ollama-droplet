# Ollama Flask API Integration

This project provides a Flask-based API service that integrates with Ollama for AI model inference. It uses LangChain for prompt management and streaming responses.

## Project Structure

- `app.py` - Main Flask application with streaming API endpoint
- `Dockerfile` - Container configuration for the Flask application
- `docker-compose.yml` - Docker Compose configuration for both Ollama and Flask services
- `requirements.txt` - Python dependencies
- `start-ollama.sh` - Initialization script for Ollama service
- `.env` - Environment configuration file

## Prerequisites

- Docker and Docker Compose
- Python 3.9 or later (if running locally)

## Setup

1. Clone this repository
2. Configure your environment variables in `.env` file:
   ```
   MODEL=nemotron-mini
   LANGCHAIN_PROJECT=gogomonkey
   ```

## Running with Docker Compose

1. Start the services:
   ```bash
   docker-compose up --build
   ```

This will:
- Start the Ollama service on port 11434
- Start the Flask application on port 8080
- Set up a bridge network for communication between services
- Pull and initialize the nemotron-mini model

## API Usage

The API provides a single endpoint for asking questions:

```
GET /ask?question=your_question_here
```

The response is streamed in real-time as the model generates the output.

## Dependencies

- Flask 3.0.3
- langchain-core 0.3.14
- langchain-ollama 0.2.0
- python-dotenv 1.0.1

## Architecture

The application consists of two main services:

1. **Ollama Service**
   - Runs the Ollama model server
   - Manages model loading and inference
   - Persists model data in ./data/ollama

2. **Flask Application**
   - Provides HTTP API endpoint
   - Integrates with Ollama via LangChain
   - Handles streaming responses

## Environment Variables

- `MODEL`: The Ollama model to use (default: nemotron-mini)
- `OLLAMA_BASE_URL`: URL for the Ollama service
- `LANGCHAIN_PROJECT`: Project name for LangChain
