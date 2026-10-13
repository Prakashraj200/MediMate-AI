"""
Preethi AI - Main Conversational Clinical Assistant Orchestrator
"""

from ai.symptom_analyzer import analyze_symptoms
from ai.recommendation_engine import get_recommendations
from config.ai_config import AI_CONFIG


class PreethiAI:
    def __init__(self):
        self.name = AI_CONFIG["engine_name"]
        self.version = AI_CONFIG["version"]

    def converse(self, message, patient_context=None):
        """Analyze message, extract clinical intent, and generate comprehensive response."""
        analysis = analyze_symptoms(message)
        recommendations = get_recommendations(analysis["detected_symptoms"])

        if analysis["is_emergency"]:
            response_text = (
                "🚨 HIGH PRIORITY CLINICAL EMERGENCY DETECTED: Symptoms like sudden chest tightness or severe "
                "shortness of breath require urgent intervention. Please contact emergency services (108 / 911) "
                "or report to the nearest hospital immediately."
            )
        elif analysis["detected_symptoms"]:
            symptoms_str = ", ".join(analysis["detected_symptoms"]).replace("_", " ")
            response_text = (
                f"I've noted your reported symptoms ({symptoms_str}). "
                f"Based on clinical triage, a consultation with **{recommendations['primary_specialty']}** is recommended. "
                "Here are immediate wellness recommendations to consider:"
            )
        else:
            response_text = (
                "Thank you for contacting Preethi AI. Your vitals and records can be viewed on your dashboard. "
                "If you are experiencing any acute discomfort, feel free to describe your symptoms."
            )

        return {
            "assistant": self.name,
            "response": response_text,
            "analysis": analysis,
            "recommendations": recommendations,
            "disclaimer": "Preethi AI provides medical information and guidance, not emergency clinical diagnosis."
        }


# Singleton instance
preethi_bot = PreethiAI()
