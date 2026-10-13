"""
Patient Service - Patient demographic information and records.
"""

from backend.services.firebase_service import (
    get_all_patients,
    get_patient,
    create_patient,
    update_patient,
    delete_patient
)


def list_patients():
    """Retrieve all patients."""
    return get_all_patients()


def fetch_patient_by_id(patient_id):
    """Retrieve specific patient details."""
    return get_patient(patient_id)


def register_new_patient(patient_data):
    """Register patient record."""
    return create_patient(patient_data)


def update_patient_record(patient_id, patient_data):
    """Update patient demographic/contact record."""
    return update_patient(patient_id, patient_data)


def delete_patient_record(patient_id):
    """Remove patient record."""
    return delete_patient(patient_id)
