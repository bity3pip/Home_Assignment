For AI Chat inside PyCharm:

1) You need to create a Flask app where you have three endpoints. Technical requirements:
    - Use the Flask framework.
    - Google Gemini API integration (option to choose between Gemini 2.5 and Gemini 3)
      - Gemini Integration
      - Create a separate client module
      - Accept model name (gemini-2.5 or gemini-3)
      - Map to correct model IDs or mock them if needed
      - Maintain conversation history per user in memory (optional)
    - File structure should be organized in a way that makes sense.
    - Make a test for every endpoint and make sure it passes.

2) Create endpoints for:
    - POST /api/chat
      - Input JSON: {
            "user_id": "optional",
            "message": "text",
            "model": "gemini-2.5"
      }
      - Response JSON: {
          "reply": "AI answer",
          "model_used": "gemini-2.5",
          "timestamp": "..."
      }
    - POST /api/user
        - Create a simple user object in memory
        - Return a generated user_id
      
    - GET /api/helth
        - Return {"status": "ok"}

3) Do choose between Gemini 2.5 and Gemini 3.

4) Create a API_DOCS.md file with REST API documentation include: 
    - Overview 
    - All endpoints with request and response examples.
    - Schemas
    - Basic error handling.
For Lovable:

1) Create a simple chatbot that can answer questions about cats.
    - Requested features:
        - Build a simple chat interface
        - Call your Flask API using HTTPS (ngrok recommended)
        - Show loading states
        - Handle errors gracefully
        - Include a simple “API Docs” page that uses your generated documentation
    - Simple UI with:
        - Input box
        - Send button
        - Chat display
        - Model selector (Gemini 2.5 or Gemini 3)

2) src/pages/Chat.tsx content: data.reply || data.message || "No response received",


- Where AI helped
    - AI helped with:
      - creating a simple chatbot
      - creating a simple chat interface
      - explaining all logic behind the chatbot
      - sped up the process of development

- Where AI made mistakes
    - For example:
      - Prompt for AI Chat inside PyCharm was not clear enough
        - AI give me response but he don't clearly understand what he need to do

- What you learned
    - I learned simple Flask
    - I learned how to use ngrok
    - I learned how to use Gemini API
    - I learned what all response from AI depends on your prompt