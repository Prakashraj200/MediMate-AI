"""
Appointment Service - Clinical appointment booking, rescheduling, and cancellation.
"""

from config.firebase_config import db
from backend.utils.helpers import generate_unique_id, format_iso_timestamp


def get_all_appointments(doctor_id=None, patient_id=None, status=None):
    """Retrieve appointments with optional filters."""
    query = db.collection("appointments")
    if doctor_id:
        query = query.where("doctor_id", "==", doctor_id)
    if patient_id:
        query = query.where("patient_id", "==", patient_id)
    if status:
        query = query.where("status", "==", status)
        
    docs = query.stream()
    appointments = []
    for doc in docs:
        data = doc.to_dict()
        data["id"] = doc.id
        appointments.append(data)
    return appointments


def get_appointment(appointment_id):
    """Get single appointment."""
    doc = db.collection("appointments").document(appointment_id).get()
    if not doc.exists:
        return None
    data = doc.to_dict()
    data["id"] = doc.id
    return data


def schedule_appointment(data):
    """Create a new appointment."""
    data["created_at"] = format_iso_timestamp()
    if "status" not in data:
        data["status"] = "Confirmed"
    if "appointment_code" not in data:
        data["appointment_code"] = generate_unique_id("APT")
        
    doc_ref = db.collection("appointments").document()
    doc_ref.set(data)
    return doc_ref.id


def update_appointment_details(appointment_id, data):
    """Update appointment details or status."""
    data["updated_at"] = format_iso_timestamp()
    db.collection("appointments").document(appointment_id).update(data)
    return True


def cancel_appointment(appointment_id, reason="Patient requested cancellation"):
    """Cancel an appointment."""
    update_data = {
        "status": "Cancelled",
        "cancellation_reason": reason,
        "cancelled_at": format_iso_timestamp()
    }
    db.collection("appointments").document(appointment_id).update(update_data)
    return True
