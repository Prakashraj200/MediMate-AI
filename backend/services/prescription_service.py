"""
Prescription Service - Digital clinical prescriptions issued by licensed doctors.
"""

from config.firebase_config import db
from backend.utils.helpers import generate_unique_id, format_iso_timestamp


def get_all_prescriptions(patient_id=None, doctor_id=None):
    """Retrieve prescriptions list with optional filters."""
    query = db.collection("prescriptions")
    if patient_id:
        query = query.where("patient_id", "==", patient_id)
    if doctor_id:
        query = query.where("doctor_id", "==", doctor_id)
        
    docs = query.stream()
    prescriptions = []
    for doc in docs:
        data = doc.to_dict()
        data["id"] = doc.id
        prescriptions.append(data)
    return prescriptions


def get_prescription_by_id(rx_id):
    """Retrieve full prescription details."""
    doc = db.collection("prescriptions").document(rx_id).get()
    if not doc.exists:
        return None
    data = doc.to_dict()
    data["id"] = doc.id
    return data


def issue_prescription(data):
    """Issue a new electronic prescription."""
    data["created_at"] = format_iso_timestamp()
    if "rx_number" not in data:
        data["rx_number"] = generate_unique_id("RX-2026")
    if "status" not in data:
        data["status"] = "Active"
        
    doc_ref = db.collection("prescriptions").document()
    doc_ref.set(data)
    return doc_ref.id


def update_prescription_status(rx_id, status_data):
    """Update prescription status (Active/Completed)."""
    db.collection("prescriptions").document(rx_id).update(status_data)
    return True
