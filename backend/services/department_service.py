"""
Department Service - Hospital medical specialties and department administration.
"""

from config.firebase_config import db


DEFAULT_DEPARTMENTS = [
    {"name": "Cardiology", "head": "Head of Cardiology", "icon": "❤️", "room": "Wing B, Level 3", "active": True},
    {"name": "General Medicine", "head": "Head of General Medicine", "icon": "🩺", "room": "Wing A, Level 1", "active": True},
    {"name": "Dermatology", "head": "Head of Dermatology", "icon": "🧴", "room": "Wing A, Level 2", "active": True},
    {"name": "Orthopedics", "head": "Head of Orthopedics", "icon": "🦴", "room": "Wing C, Level 2", "active": True},
    {"name": "Neurology", "head": "Head of Neurology", "icon": "🧠", "room": "Wing B, Level 4", "active": True},
    {"name": "Pediatrics", "head": "Head of Pediatrics", "icon": "👶", "room": "Wing D, Level 1", "active": True}
]


def get_all_departments():
    """Retrieve departments from Firestore or default list."""
    docs = list(db.collection("departments").stream())
    if not docs:
        return DEFAULT_DEPARTMENTS
    departments = []
    for doc in docs:
        data = doc.to_dict()
        data["id"] = doc.id
        departments.append(data)
    return departments


def create_department(data):
    """Add new medical department."""
    doc_ref = db.collection("departments").document()
    doc_ref.set(data)
    return doc_ref.id


def update_department(dept_id, data):
    """Update department info."""
    db.collection("departments").document(dept_id).update(data)
    return True


def delete_department(dept_id):
    """Remove department."""
    db.collection("departments").document(dept_id).delete()
    return True
