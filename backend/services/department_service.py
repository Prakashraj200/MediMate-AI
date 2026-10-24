"""
Department Service - Rehabilitation Divisions & Trauma Recovery Administration.
"""

from config.firebase_config import db


DEFAULT_DEPARTMENTS = [
    {"name": "Whiplash & Cervical Spine Unit", "head": "Dr. Anand Kumar (Senior PT)", "icon": "🛡️", "room": "Rehab Wing A, Room 101", "active": True},
    {"name": "Orthopedic Trauma & Fracture Recovery", "head": "Dr. Radhika Menon (MPT)", "icon": "🦴", "room": "Trauma Wing B, Room 204", "active": True},
    {"name": "Knee Meniscus & ACL Rehab", "head": "Dr. Sanjay Patel (BPT)", "icon": "🦵", "room": "Sports Rehab Wing C, Room 302", "active": True},
    {"name": "Lumbar Spine & Core Rehabilitation", "head": "Dr. Malini Swaminathan (MPT)", "icon": "🧘", "room": "Rehab Wing A, Room 105", "active": True},
    {"name": "TENS & Electrotherapy Modality Unit", "head": "Dr. Anand Kumar (Lead Physio)", "icon": "⚡", "room": "Modality Lab, Level 1", "active": True},
    {"name": "Sports Ligament & Soft Tissue Trauma", "head": "Dr. Sanjay Patel (Sports PT)", "icon": "🏃", "room": "Biomechanics Lab 2", "active": True}
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
    """Add new rehabilitation department."""
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
