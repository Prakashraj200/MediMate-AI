"""
Report Service - Diagnostic pathology reports and hospital operational statistics.
"""

from config.firebase_config import db
from backend.utils.helpers import format_iso_timestamp, generate_unique_id


def get_patient_lab_reports(patient_id):
    """Retrieve laboratory reports for patient."""
    docs = db.collection("lab_reports").where("patient_id", "==", patient_id).stream()
    reports = []
    for doc in docs:
        data = doc.to_dict()
        data["id"] = doc.id
        reports.append(data)
    return reports


def get_single_lab_report(report_id):
    """Retrieve single lab report."""
    doc = db.collection("lab_reports").document(report_id).get()
    if not doc.exists:
        return None
    data = doc.to_dict()
    data["id"] = doc.id
    return data


def create_lab_report(data):
    """Store certified lab report."""
    data["created_at"] = format_iso_timestamp()
    if "report_code" not in data:
        data["report_code"] = generate_unique_id("LAB")
    doc_ref = db.collection("lab_reports").document()
    doc_ref.set(data)
    return doc_ref.id


def update_lab_report(report_id, data):
    """Update lab report findings."""
    db.collection("lab_reports").document(report_id).update(data)
    return True
