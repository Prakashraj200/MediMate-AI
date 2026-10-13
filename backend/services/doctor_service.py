"""
Doctor Service - Clinical profiles, specialist directory, and doctor workflow.
"""

from backend.services.firebase_service import (
    get_all_doctors,
    get_doctor,
    create_doctor,
    update_doctor,
    delete_doctor
)


def list_doctors(department=None):
    """List doctors, optionally filtered by medical specialty/department."""
    doctors = get_all_doctors()
    if department:
        return [d for d in doctors if str(d.get("department", "")).lower() == department.lower()]
    return doctors


def fetch_doctor_profile(doctor_id):
    """Retrieve individual doctor profile."""
    return get_doctor(doctor_id)


def register_doctor_profile(doctor_data):
    """Add new doctor profile."""
    return create_doctor(doctor_data)


def modify_doctor_profile(doctor_id, doctor_data):
    """Update doctor profile."""
    return update_doctor(doctor_id, doctor_data)


def remove_doctor_profile(doctor_id):
    """Delete doctor profile."""
    return delete_doctor(doctor_id)
