"""
AI Service - Interface for Preethi AI clinical chat, symptom triage, and health recommendations.
"""

from config.ai_config import AI_CONFIG


def process_clinical_query(user_message, user_context=None):
    """Analyze patient query and provide medically structured guidance."""
    msg = (user_message or "").strip().lower()

    # 1. Emergency detection
    for kw in AI_CONFIG["emergency_keywords"]:
        if kw in msg:
            return {
                "triage_level": "emergency",
                "emergency_alert": True,
                "response": (
                    "🚨 HIGH PRIORITY MEDICAL ALERT: Your symptoms may indicate an acute emergency. "
                    f"Please contact emergency services immediately ({AI_CONFIG['emergency_hotline']}) "
                    "or visit the nearest hospital emergency department."
                ),
                "action": "call_emergency",
                "disclaimer": "Preethi AI is not a substitute for emergent clinical care."
            }

    # 2. Symptoms classification
    if "fever" in msg or "temperature" in msg:
        return {
            "triage_level": "routine",
            "emergency_alert": False,
            "response": (
                "For low to moderate fever, rest and oral hydration are paramount. "
                "Monitor your temperature every 4 hours. If fever exceeds 102°F or persists for over 48 hours, "
                "schedule an evaluation with a general physician."
            ),
            "suggested_specialist": "General Medicine"
        }

    if "headache" in msg or "migraine" in msg:
        return {
            "triage_level": "routine",
            "emergency_alert": False,
            "response": (
                "Mild headaches often stem from hydration, screen strain, or sleep deprivation. "
                "Drink 500ml water and rest in a dim environment. If accompanied by sudden visual changes, "
                "stiff neck, or vomiting, seek immediate medical attention."
            ),
            "suggested_specialist": "Neurology"
        }

    if "blood pressure" in msg or "hypertension" in msg:
        return {
            "triage_level": "routine",
            "emergency_alert": False,
            "response": (
                "Maintain low sodium intake (<2,000 mg/day). Engage in 30 minutes of moderate aerobic exercise "
                "and take prescribed antihypertensive medications consistently at the same time each morning."
            ),
            "suggested_specialist": "Cardiology"
        }

    # Default supportive response
    return {
        "triage_level": "routine",
        "emergency_alert": False,
        "response": (
            "Thank you for sharing your inquiry. To get personalized clinical attention, "
            "you can book an in-person or video consultation directly with our hospital specialists."
        ),
        "suggested_specialist": "General Medicine"
    }
