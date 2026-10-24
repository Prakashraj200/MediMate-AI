"""
Pain & Rehabilitation Recovery Trajectory Predictor.
Predicts whether a post-accident patient is On-Track, Experiencing Delayed Recovery,
or at High Risk of Chronic Pain / Complications.
Supports both trained Scikit-Learn RandomForest models and clinical decision trees.
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "ml", "saved_models", "pain_recovery_model.joblib")

_model = None

def _load_model():
    global _model
    if _model is not None:
        return _model
    if os.path.exists(MODEL_PATH):
        try:
            import joblib
            _model = joblib.load(MODEL_PATH)
            return _model
        except Exception:
            _model = None
    return None


def predict_recovery_risk(age, days_since_accident, pain_score, exercise_adherence_pct, mobility_rom_pct, swelling_level):
    """
    Predict recovery risk tier:
    0: On-Track (Good healing velocity, low chronic pain risk)
    1: Delayed Recovery (Sub-optimal progress, therapist adjustment needed)
    2: High Risk (Chronic pain danger, possible nerve impingement/DVT/secondary injury)
    """
    age = float(age)
    days = float(days_since_accident)
    pain = float(pain_score)
    adherence = float(exercise_adherence_pct)
    rom = float(mobility_rom_pct)
    swelling = int(swelling_level)

    model = _load_model()
    tier = None

    if model is not None:
        try:
            import pandas as pd
            features = pd.DataFrame([{
                "age": age,
                "days_since_accident": days,
                "pain_score": pain,
                "exercise_adherence_pct": adherence,
                "mobility_rom_pct": rom,
                "swelling_level": swelling
            }])
            tier = int(model.predict(features)[0])
        except Exception:
            tier = None

    # Deterministic Clinical Boundary Engine (Ensures 100% reliable uptime)
    if tier is None:
        if pain <= 4.0 and rom >= 70 and adherence >= 60:
            tier = 0
        elif pain >= 7.5 or (days > 45 and rom < 55) or (days > 30 and swelling >= 2):
            tier = 2
        else:
            tier = 1

    # Format clinical prognosis details
    if tier == 0:
        label = "On-Track Recovery"
        risk_level = "Low"
        color = "#10b981"
        est_days = max(7, int(35 - (days * 0.4)))
        recommendations = [
            "Continue current home exercise regimen and mobility drills.",
            "Maintain post-exercise ice application (15 mins) if mild soreness arises.",
            "Schedule standard bi-weekly physiotherapy check-in."
        ]
    elif tier == 1:
        label = "Delayed Recovery / Moderate Stiffness"
        risk_level = "Moderate"
        color = "#f59e0b"
        est_days = max(21, int(60 - (days * 0.3)))
        recommendations = [
            "Increase exercise adherence to at least 75% for optimal ligament remodeling.",
            "Focus on passive stretching and gradual Range of Motion (ROM) restoration.",
            "Consult supervising physiotherapist to adjust resistance levels."
        ]
    else:
        label = "High Chronic Pain / Complication Risk"
        risk_level = "High"
        color = "#ef4444"
        est_days = max(45, int(90 - (days * 0.2)))
        recommendations = [
            "Urgent in-clinic orthopedic re-evaluation recommended.",
            "Rule out complex regional pain syndrome (CRPS), tendon tear, or nerve impingement.",
            "Pause high-resistance loading exercises until reviewed by clinical team."
        ]

    return {
        "recovery_risk_tier": tier,
        "risk_level": risk_level,
        "status_label": label,
        "badge_color": color,
        "estimated_recovery_days_remaining": est_days,
        "patient_metrics": {
            "age": age,
            "days_since_accident": days,
            "pain_score_vas": pain,
            "exercise_adherence_pct": adherence,
            "mobility_rom_pct": rom,
            "swelling_level": swelling
        },
        "clinical_recommendations": recommendations
    }
