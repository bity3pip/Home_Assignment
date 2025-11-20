# API Documentation

## Overview
This API provides a conversational interface powered by Google's Gemini models. It allows client applications to manage user sessions and interact with different versions of the Gemini AI model.

## Base URL
`http://localhost:5000` (default for local development)

---

## Endpoints

### 1. System Health Check
Checks if the API is running and responsive.

- **URL**: `/health`
- **Method**: `GET`
- **Auth**: None

**Response:**
```
json
{
  "status": "ok"
}
```
---

### 2. Create User
Creates a new temporary user session in memory. This is useful for maintaining conversation history context.

- **URL**: `/api/user`
- **Method**: `POST`
- **Auth**: None

**Request Body:**
Empty JSON object or `null`.

**Response (200 OK):**
```
json
{
  "user_id": "550e8400-e29b-41d4-a716-446655440000"
}
```
---

### 3. Chat with AI
Sends a message to the AI model and receives a response. Supports conversation history if `user_id` is provided.

- **URL**: `/api/chat`
- **Method**: `POST`
- **Auth**: None

**Request Body Schema:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `message` | string | Yes | The text prompt to send to the AI. |
| `model` | string | No | Model version to use. Options: `gemini-2.5` (default), `gemini-3`. |
| `user_id` | string | No | The ID returned from `/api/user` to maintain conversation context. |

**Example Request:**
```
json
{
  "user_id": "550e8400-e29b-41d4-a716-446655440000",
  "message": "Explain quantum physics in simple terms",
  "model": "gemini-2.5"
}
```
**Response (200 OK):**
```
json
{
  "reply": "Quantum physics is the study of how very small things like atoms and subatomic particles behave...",
  "model_used": "gemini-2.5",
  "timestamp": "2023-10-27 10:30:00.123456"
}
```
**Error Response (400 Bad Request):**
```
json
{
  "error": "Message is required"
}
```
---

## Schemas

### Chat Request
```
json
{
  "type": "object",
  "properties": {
    "user_id": { "type": "string" },
    "message": { "type": "string" },
    "model": { "type": "string", "enum": ["gemini-2.5", "gemini-3"] }
  },
  "required": ["message"]
}
```
### Chat Response
```
json
{
  "type": "object",
  "properties": {
    "reply": { "type": "string" },
    "model_used": { "type": "string" },
    "timestamp": { "type": "string" }
  }
}
```
---

## Error Handling

The API uses standard HTTP status codes:

- **200 OK**: The request was successful.
- **400 Bad Request**: The request was invalid (e.g., missing `message` field).
- **429 Too Many Requests**: The API rate limit has been exceeded. Please try again later.
- **500 Internal Server Error**: An error occurred on the server side (e.g., Gemini API connection failure).

If the Gemini service fails, the `reply` field in the successful response might contain an error description string starting with "Error interacting with Gemini...".
```
