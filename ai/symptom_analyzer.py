"""
Symptom Analyzer - Detects reported symptoms, severity levels, and clinical emergency indicators.
"""

from ai.model_utils import preprocess_clinical_text

SYMPTOM_DICTIONARY = {
    "chest_pain": ["chest pain", "tightness in chest", "angina", "pressure on chest", "heart racing"],
    "shortness_of_breath": ["cannot breathe", "shortness of breath", "dyspnea", "gasping for air", "wheezing"],
    "headache": ["headache", "head pain", "migraine", "throbbing head", "head pressure"],
    "fever": ["fever", "high temperature", "chills", "feeling hot", "shivering"],
    "hypertension": ["high bp", "high blood pressure", "hypertension", "elevated pressure"],
    "dizziness": ["dizziness", "lightheaded", "feeling faint", "spinning", "vertigo"],
    "cough": ["cough", "dry cough", "phlegm", "congestion", "sore throat"],
    "skin_rash": ["rash", "itching", "skin spots", "hives", "red patches"]
}


def analyze_symptoms(text):
    """Identify matched symptoms and clinical triage tier."""
    cleaned = preprocess_clinical_text(text)
    detected = []

    for symptom_key, terms in SYMPTOM_DICTIONARY.items():
        if any(term in cleaned for term in terms):
            detected.append(symptom_key)

    is_emergency = "chest_pain" in detected or "shortness_of_breath" in detected
    severity = "critical" if is_emergency else ("moderate" if len(detected) > 1 else "mild")

    return {
        "detected_symptoms": detected,
        "is_emergency": is_emergency,
        "severity": severity,
        "symptoms_count": len(detected)
    }
