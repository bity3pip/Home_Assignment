# Flask Gemini AI Integration

This project is a Flask-based REST API that integrates with Google's Gemini AI models to provide conversational capabilities. It was developed as a home assignment to demonstrate API development, third-party service integration, and state management.

## Home Assignment Features

The following requirements have been implemented:

### REST API Endpoints
- **`POST /api/chat`**: Core endpoint for sending messages to Gemini. Supports model selection (`gemini-2.5`, `gemini-3`) and conversation history.
- **`POST /api/user`**: Creates a user session in memory and returns a generated `user_id`.
- **`GET /health`**: Simple health check endpoint returning system status.

### Gemini Integration
- **Service Module**: A dedicated `GeminiService` class handles interactions with the Google Generative AI SDK.
- **Model Selection**: Logic to map frontend model names (e.g., `gemini-2.5`) to actual API model IDs.
- **Context Management**: Maintains conversation history in-memory for specific users, allowing for multi-turn conversations.
- **Error Handling**: Robust error handling with fallback mechanisms (e.g., falling back to "Flash" models if the primary model is unavailable).

## Documentation

Detailed documentation for the project resources can be found in the following files:

- **[API Documentation](API_DOCS.md)**: Complete reference for all API endpoints, request/response schemas, and error codes.
- **[AI Prompts](AI_PROMPTS.md)**: Information regarding prompts or AI interactions relevant to the project.

## Setup and Run

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Environment**:
   Create a `.env` file in the root directory and add your Google API Key:
   ```env
   GOOGLE_API_KEY=your_api_key_here
   ```

3. **Run the Application**:
   ```bash
   python run.py
   ```
   The server will start at `http://localhost:5000`.