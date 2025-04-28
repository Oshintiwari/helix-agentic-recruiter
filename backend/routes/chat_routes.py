from flask import Blueprint, request, jsonify
from services.agent_service import process_user_message
from models.database import get_all_messages


chat_bp = Blueprint('chat', __name__)
# chat_bp is a Flask Blueprint for handling chat-related routes
# It allows for modular organization of routes and can be registered with a Flask app.

# Define the route for the chat endpoint
@chat_bp.route('/chat', methods=['POST']) #/chat POST API endpoint ready.
def chat():
    user_message = request.json.get('message')
    ai_response = process_user_message(user_message)
    return jsonify({"response": ai_response})
# chat() is a Flask route handler function that processes incoming chat messages.
# It retrieves the user's message from the request, processes it using the agent service, and returns the AI's response in JSON format.

# Define the route for getting chat history
# This route retrieves all messages from the database and returns them in JSON format.
@chat_bp.route('/messages', methods=['GET'])
def get_messages():
    """
    Get all chat history from the database.
    """
    messages = get_all_messages()
    return jsonify({"messages": messages})