"""
Vitals Service - Physiological telemetry readings (BP, pulse, glucose, SpO2, temperature).
"""

from config.firebase_config import db
from backend.utils.helpers import format_iso_timestamp


def get_patient_vitals(patient_id):
    """Retrieve historical vital readings for a patient."""
    try:
        docs = db.collection("vitals").where("patient_id", "==", patient_id).stream()
        vitals_list = []
        for doc in docs:
            data = doc.to_dict()
            data["id"] = doc.id
            vitals_list.append(data)
        vitals_list.sort(key=lambda x: str(x.get("timestamp", "")), reverse=True)
        return vitals_list[:20]
    except Exception:
        return []


def record_vital_reading(data):
    """Save new vital signs reading."""
    data["timestamp"] = format_iso_timestamp()
    doc_ref = db.collection("vitals").document()
    doc_ref.set(data)
    return doc_ref.id


def classify_vitals(systolic, diastolic, heart_rate=None):
    """Classify blood pressure reading into clinical tier."""
    if systolic >= 140 or diastolic >= 90:
        return "Hypertension Stage 2"
    elif systolic >= 130 or diastolic >= 80:
        return "Hypertension Stage 1"
    elif systolic >= 120 and diastolic < 80:
        return "Elevated"
    elif systolic >= 90 and diastolic >= 60:
        return "Normal"
    else:
        return "Hypotension"
