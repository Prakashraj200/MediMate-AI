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
                "Here are immediate recovery and wellness guidelines to consider:\n\n"
                f"• Rest the affected area and avoid movements that cause sharp, shooting pain.\n"
                f"• Check your pain score on the VAS scale (1–10). If it exceeds 6/10, contact your physiotherapist."
            )
            severity = analysis.get("severity", "moderate")
        else:
            # Contextual Conversational Intents
            msg_clean = message.strip().lower()
            
            # 1. Greetings
            if any(g in msg_clean for g in ["hi", "hello", "hey", "vanakkam", "good morning", "good evening", "good afternoon"]):
                name_str = f", {patient_context.get('patient_name')}" if patient_context and patient_context.get("patient_name") else ""
                response_text = (
                    f"Hello{name_str}! 👋 I am **Preethi AI**, your clinical physiotherapy rehabilitation companion.\n\n"
                    "I am ready to help you with:\n"
                    "• **Acute Injury Relief:** When to use ice packs vs heat therapy (R.I.C.E protocol)\n"
                    "• **Rehab Exercises:** Safe gentle stretches, heel slides, chin tucks & posture guides\n"
                    "• **Pain Tracking:** Understanding your 1–10 VAS pain score & recovery milestones\n"
                    "• **Clinical Triage:** Immediate checks for orthopedic emergency red-flags\n\n"
                    "What symptoms or exercises would you like guidance on today?"
                )
                severity = "normal"

            # 2. Gratitude / Affirmation
            elif any(t in msg_clean for t in ["thank", "thanks", "nandri", "ok", "got it", "super", "helpful"]):
                response_text = (
                    "You're very welcome! 😊 Remember that consistency in daily gentle movement and adequate rest are the foundation of safe post-accident recovery.\n\n"
                    "Don't forget to log your daily VAS score in the **Pain & Rehab Tracker**. Feel free to ask anytime you experience discomfort or need exercise guidance!"
                )
                severity = "normal"

            # 3. Identity / Capabilities
            elif any(w in msg_clean for w in ["who are you", "what can you do", "help me", "introduce", "your name"]):
                response_text = (
                    "I am **Preethi AI** (v2.0), an intelligent clinical triage and tele-rehabilitation assistant trained on 105 specialized post-trauma recovery protocols.\n\n"
                    "Here are sample questions you can ask me right now:\n"
                    "1. *'Should I use ice or heat for acute neck swelling?'*\n"
                    "2. *'Why is my joint stiff after plaster cast removal?'*\n"
                    "3. *'When can I start putting weight on my leg after fracture surgery?'*\n"
                    "4. *'What are safe isometric exercises for knee recovery?'*\n"
                    "5. *'What universal red-flags require immediate emergency hospital care?'*"
                )
                severity = "normal"

            # 4. General / Tanglish Pain Inquiry
            elif any(p in msg_clean for p in ["pain", "hurt", "ache", "sore", "vali", "enna pannanum"]):
                response_text = (
                    "I understand you are experiencing discomfort. To give you the most accurate physiotherapy advice, please tell me a bit more:\n\n"
                    "1. **Location:** Which joint or muscle hurts (e.g., cervical neck, lumbar back, knee, shoulder, ankle)?\n"
                    "2. **Pain Rating:** What is your pain score from 0 (no pain) to 10 (unbearable) on the VAS scale?\n"
                    "3. **Duration:** Did this start recently after an accident/exercise, or has it been ongoing for weeks?\n\n"
                    "Once you share the location and symptoms, I will recommend the exact R.I.C.E or mobility protocol for you."
                )
                severity = "moderate"

            else:
                response_text = (
                    "I hear you! As your clinical rehabilitation assistant, I can guide you on post-accident pain, "
                    "ice vs heat therapy, safe home stretches, and emergency red-flags.\n\n"
                    "💡 *Try asking me:* 'Should I apply ice or heat?', 'How to do ankle pumps?', or describe where your pain is located."
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
