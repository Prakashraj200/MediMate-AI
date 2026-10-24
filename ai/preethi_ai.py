"""
Preethi AI - Main Conversational Clinical & Physiotherapy Rehabilitation Assistant Orchestrator
Specialized in Post-Accident Pain Management, 105 Q&A Knowledge Base & Clinical Triage.
"""

from ai.symptom_analyzer import analyze_symptoms
from ai.recommendation_engine import get_recommendations
from ai.physio_pain_dataset import query_pain_knowledge_base
from config.ai_config import AI_CONFIG


class PreethiAI:
    def __init__(self):
        self.name = AI_CONFIG["engine_name"]
        self.version = "2.0.0-PhysioRehab"

    def converse(self, message, patient_context=None):
        """
        Analyze message, check specialized 105 Physiotherapy & Pain Q&A database,
        evaluate red flags, and generate comprehensive clinical guidance.
        """
        # Step 1: Check specialized Physiotherapy & Pain Knowledge Base
        pain_kb_result = query_pain_knowledge_base(message)

        # Step 2: Check general symptom analyzer & red-flag detection
        analysis = analyze_symptoms(message)
        recommendations = get_recommendations(analysis.get("detected_symptoms", []))

        # Check if pain KB returned a critical red flag
        is_red_flag = analysis["is_emergency"] or (pain_kb_result.get("found") and pain_kb_result.get("red_flag"))

        if is_red_flag:
            red_flag_reason = pain_kb_result.get("answer") if (pain_kb_result.get("found") and pain_kb_result.get("red_flag")) else (
                "Symptoms indicate an acute clinical emergency (such as DVT, Compartment Syndrome, or severe distress)."
            )
            response_text = (
                f"🚨 RED-FLAG EMERGENCY ALERT: {red_flag_reason} "
                "Please STOP all physical exercises immediately, contact emergency services (108 / 911), "
                "or report to the nearest orthopedic emergency department right away."
            )
            severity = "critical"
        elif pain_kb_result.get("found"):
            # Direct match from the 105 Physiotherapy & Pain Dataset!
            response_text = (
                f"**Clinical Guidance for: {pain_kb_result['question']}**\n\n"
                f"{pain_kb_result['answer']}\n\n"
                f"💡 *Physiotherapist Note:* If your pain score exceeds 6/10 on the VAS scale during exercises, "
                f"pause the routine, apply cold compression for 15 minutes, and notify your supervising therapist."
            )
            severity = pain_kb_result.get("severity", "moderate")
        elif analysis["detected_symptoms"]:
            symptoms_str = ", ".join(analysis["detected_symptoms"]).replace("_", " ")
            response_text = (
                f"I've noted your reported recovery symptoms ({symptoms_str}). "
                f"Based on clinical rehabilitation triage, a consultation with **{recommendations['primary_specialty']}** is recommended. "
                "Here are immediate recovery and wellness guidelines to consider:"
            )
            severity = analysis.get("severity", "moderate")
        else:
            response_text = (
                "Hello! I am Preethi AI, your specialized Physiotherapy Rehabilitation and Pain Relief Assistant. "
                "I can guide you on post-accident recovery, safe rehabilitation exercises, R.I.C.E ice/heat protocols, "
                "and pain scale tracking. How can I assist with your recovery today?"
            )
            severity = "normal"

        return {
            "assistant": self.name,
            "response": response_text,
            "analysis": analysis,
            "pain_kb_match": pain_kb_result if pain_kb_result.get("found") else None,
            "recommendations": recommendations,
            "severity": severity,
            "disclaimer": "Preethi AI provides evidence-based physiotherapy guidance and triage, not a substitute for formal diagnostic imaging."
        }


# Singleton instance
preethi_bot = PreethiAI()
