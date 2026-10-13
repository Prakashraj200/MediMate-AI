from flask import Blueprint, request
from backend.services.ai_service import process_clinical_query
from backend.utils.response import success_response, error_response

ai_chat_bp = Blueprint("ai_chat", __name__, url_prefix="/api/ai")


@ai_chat_bp.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True)
    if not data or not data.get("message"):
        return error_response("Message string is required", 400)
    
    user_message = data.get("message")
    context = data.get("context", {})
    
    result = process_clinical_query(user_message, context)
    return success_response(result, "Preethi AI response generated")
