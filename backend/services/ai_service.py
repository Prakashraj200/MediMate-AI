"""
AI Service - Interface for Preethi AI clinical chat, symptom triage, and post-accident physiotherapy pain management.
Integrated with 105 Clinical Rehabilitation Q&A Knowledge Base & Red-Flag Triage Engine.
"""

from ai.preethi_ai import preethi_bot
from config.ai_config import AI_CONFIG


def process_clinical_query(user_message, user_context=None):
    """
    Analyze patient/physiotherapist query using Preethi AI 2.0.
    Integrates 105 Specialized Q&As for Post-Accident Pain, Safe Exercises,
    VAS Pain Scale, and Emergency Red Flags.
    """
    msg = (user_message or "").strip()
    if not msg:
        return {
            "triage_level": "routine",
            "emergency_alert": False,
            "response": "Please enter a question or describe your pain and recovery symptoms.",
            "action": "none"
        }

    # Run through PreethiAI orchestrator
    bot_result = preethi_bot.converse(msg, user_context)

    is_emergency = bot_result.get("severity") == "critical"

    return {
        "triage_level": "emergency" if is_emergency else bot_result.get("severity", "routine"),
        "emergency_alert": is_emergency,
        "response": bot_result.get("response", ""),
        "action": "call_emergency" if is_emergency else "follow_guidance",
        "pain_kb_match": bot_result.get("pain_kb_match"),
        "analysis": bot_result.get("analysis"),
        "recommendations": bot_result.get("recommendations"),
        "disclaimer": bot_result.get("disclaimer", "Preethi AI is an assistive clinical tool.")
    }
