"""
Health Records Service - Medical history, allergies, chronic conditions, and immunizations.
"""

from config.firebase_config import db
from backend.utils.helpers import format_iso_timestamp


def get_patient_health_summary(patient_id):
    """Retrieve full health records for a patient."""
    doc = db.collection("health_records").document(patient_id).get()
    if not doc.exists:
        return None
    data = doc.to_dict()
    data["patient_id"] = doc.id
    return data


def save_patient_health_summary(patient_id, data):
    """Create or update full patient health summary."""
    data["updated_at"] = format_iso_timestamp()
    db.collection("health_records").document(patient_id).set(data, merge=True)
    return True


def add_allergy_record(patient_id, allergy_item):
    """Append allergy to patient record."""
    from firebase_admin import firestore
    db.collection("health_records").document(patient_id).update({
        "allergies": firestore.ArrayUnion([allergy_item])
    })
    return True
