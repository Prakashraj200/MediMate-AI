from config.firebase_config import db


# =========================
# USERS
# =========================

def get_all_users():
    docs = db.collection("users").stream()

    users = []

    for doc in docs:
        data = doc.to_dict()
        data["id"] = doc.id
        users.append(data)

    return users


def get_user(user_id):
    doc = db.collection("users").document(user_id).get()

    if not doc.exists:
        return None

    data = doc.to_dict()
    data["id"] = doc.id

    return data


def create_user(data):
    doc_ref = db.collection("users").document()
    doc_ref.set(data)

    return doc_ref.id


def update_user(user_id, data):
    db.collection("users").document(user_id).update(data)

    return True


def delete_user(user_id):
    db.collection("users").document(user_id).delete()

    return True


# =========================
# DOCTORS
# =========================

def get_all_doctors():
    docs = db.collection("doctors").stream()

    doctors = []

    for doc in docs:
        data = doc.to_dict()
        data["id"] = doc.id
        doctors.append(data)

    return doctors


def get_doctor(doctor_id):
    doc = db.collection("doctors").document(doctor_id).get()

    if not doc.exists:
        return None

    data = doc.to_dict()
    data["id"] = doc.id

    return data


def create_doctor(data):
    doc_ref = db.collection("doctors").document()
    doc_ref.set(data)

    return doc_ref.id


def update_doctor(doctor_id, data):
    db.collection("doctors").document(doctor_id).update(data)

    return True


def delete_doctor(doctor_id):
    db.collection("doctors").document(doctor_id).delete()

    return True


# =========================
# PATIENTS
# =========================

def get_all_patients():
    docs = db.collection("patients").stream()

    patients = []

    for doc in docs:
        data = doc.to_dict()
        data["id"] = doc.id
        patients.append(data)

    return patients


def get_patient(patient_id):
    doc = db.collection("patients").document(patient_id).get()

    if not doc.exists:
        return None

    data = doc.to_dict()
    data["id"] = doc.id

    return data


def create_patient(data):
    doc_ref = db.collection("patients").document()
    doc_ref.set(data)

    return doc_ref.id


def update_patient(patient_id, data):
    db.collection("patients").document(patient_id).update(data)

    return True


def delete_patient(patient_id):
    db.collection("patients").document(patient_id).delete()

    return True


# =========================
# LABORATORY
# =========================

def get_all_laboratories():
    docs = db.collection("laboratory").stream()

    laboratories = []

    for doc in docs:
        data = doc.to_dict()
        data["id"] = doc.id
        laboratories.append(data)

    return laboratories


def get_laboratory(laboratory_id):
    doc = db.collection("laboratory").document(laboratory_id).get()

    if not doc.exists:
        return None

    data = doc.to_dict()
    data["id"] = doc.id

    return data


def create_laboratory(data):
    doc_ref = db.collection("laboratory").document()
    doc_ref.set(data)

    return doc_ref.id


def update_laboratory(laboratory_id, data):
    db.collection("laboratory").document(laboratory_id).update(data)

    return True


def delete_laboratory(laboratory_id):
    db.collection("laboratory").document(laboratory_id).delete()

    return True


# =========================
# PHARMACY
# =========================

def get_all_pharmacies():
    docs = db.collection("pharmacy").stream()

    pharmacies = []

    for doc in docs:
        data = doc.to_dict()
        data["id"] = doc.id
        pharmacies.append(data)

    return pharmacies


def get_pharmacy(pharmacy_id):
    doc = db.collection("pharmacy").document(pharmacy_id).get()

    if not doc.exists:
        return None

    data = doc.to_dict()
    data["id"] = doc.id

    return data


def create_pharmacy(data):
    doc_ref = db.collection("pharmacy").document()
    doc_ref.set(data)

    return doc_ref.id


def update_pharmacy(pharmacy_id, data):
    db.collection("pharmacy").document(pharmacy_id).update(data)

    return True


def delete_pharmacy(pharmacy_id):
    db.collection("pharmacy").document(pharmacy_id).delete()

    return True