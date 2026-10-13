"""
Medicine Service - Drug catalog, dosages, inventory, and pharmacy refill handling.
"""

from config.firebase_config import db


def get_all_medicines():
    """Retrieve catalog of medications."""
    docs = db.collection("medicines").stream()
    medicines = []
    for doc in docs:
        data = doc.to_dict()
        data["id"] = doc.id
        medicines.append(data)
    return medicines


def get_medicine_by_id(med_id):
    """Retrieve single medicine details."""
    doc = db.collection("medicines").document(med_id).get()
    if not doc.exists:
        return None
    data = doc.to_dict()
    data["id"] = doc.id
    return data


def add_medicine(data):
    """Add new drug to pharmacy catalog."""
    doc_ref = db.collection("medicines").document()
    doc_ref.set(data)
    return doc_ref.id


def update_medicine(med_id, data):
    """Update medicine stock or details."""
    db.collection("medicines").document(med_id).update(data)
    return True


def delete_medicine(med_id):
    """Remove medicine."""
    db.collection("medicines").document(med_id).delete()
    return True
