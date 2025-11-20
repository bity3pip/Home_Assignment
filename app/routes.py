import datetime
import uuid
from flask import Blueprint, request, jsonify
from app.services.gemini_service import GeminiService

main_bp = Blueprint('main', __name__)
gemini_service = GeminiService()

users = {}
DEFAULT_AI_MODEL = "gemini-2.5"
@main_bp.route('/', methods=['GET'])
def index():
    return "Welcome to my Flask App!"


@main_bp.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()

    user_id = data.get('user_id')
    user_message = data.get('message')
    selected_model = data.get('model', DEFAULT_AI_MODEL)  # Value by default

    if not user_message:
        return jsonify({"error": "Message is required"}), 400

    return gemini_service.get_chat_response(user_message, selected_model, user_id)


@main_bp.route('/api/user', methods=['POST'])
def user():
    # Create a simple user object in memory
    user_id = str(uuid.uuid4())
    users[user_id] = {"created_at": str(datetime.datetime.now())}
    return jsonify({"user_id": user_id})


@main_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok"})