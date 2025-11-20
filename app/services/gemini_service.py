import google.generativeai as genai
import os
import datetime
from flask import jsonify

class GeminiService:
    def __init__(self):
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("No GOOGLE_API_KEY found in environment variables")
        genai.configure(api_key=api_key)
        self.chat_histories = {}

    def get_chat_response(self, message, model_version="gemini-2.5", user_id=None):
        """
        model_version: string, coming from UI.
        Here we are map user choice (Gemini 2.5/3) for the real name of a gemini model.
        """

        # Name mapper (if name on UI not equals for real slugs)
        # Update for more stable models
        model_map = {
            "gemini-2.5": "gemini-2.5-flash",  # Flash usually opens for everyone
            "gemini-3": "gemini-3-pro-preview", # Try lastest version or fallback to flash
        }

        # If models not found, use gemini-1.5-flash like a safe choice
        target_model = model_map.get(model_version, "gemini-2.5-flash")

        try:
            model = genai.GenerativeModel(target_model)

            history = []
            if user_id:
                history = self.chat_histories.get(user_id, [])

            chat = model.start_chat(history=history)
            response = chat.send_message(message)

            if user_id:
                self.chat_histories[user_id] = chat.history

            return jsonify({
                "reply": response.text,
                "model_used": model_version,
                "timestamp": str(datetime.datetime.now()),
            })
        except Exception as e:
            print(f"Gemini Error: {e}")
            return jsonify({"error": "Failed to generate response", "details": str(e)}), 500
