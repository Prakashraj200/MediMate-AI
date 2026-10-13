from flask import Blueprint, request, jsonify

from backend.services.firebase_service import (
    get_all_patients,
    get_patient,
    create_patient,
    update_patient,
    delete_patient
)


# =========================
# PATIENT BLUEPRINT
# =========================

patient_bp = Blueprint(
    "patient",
    __name__,
    url_prefix="/api/patients"
)


# =========================
# GET ALL PATIENTS
# =========================

@patient_bp.route("/", methods=["GET"])
def patients():

    patients = get_all_patients()

    return jsonify({
        "success": True,
        "patients": patients
    }), 200


# =========================
# GET SINGLE PATIENT
# =========================

@patient_bp.route("/<patient_id>", methods=["GET"])
def patient(patient_id):

    patient_data = get_patient(patient_id)

    if patient_data is None:
        return jsonify({
            "success": False,
            "message": "Patient not found"
        }), 404

    return jsonify({
        "success": True,
        "patient": patient_data
    }), 200


# =========================
# CREATE PATIENT
# =========================

@patient_bp.route("/", methods=["POST"])
def add_patient():

    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "message": "Patient data is required"
        }), 400

    patient_id = create_patient(data)

    return jsonify({
        "success": True,
        "message": "Patient created successfully",
        "patient_id": patient_id
    }), 201


# =========================
# UPDATE PATIENT
# =========================

@patient_bp.route("/<patient_id>", methods=["PUT"])
def edit_patient(patient_id):

    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "message": "Update data is required"
        }), 400

    existing_patient = get_patient(patient_id)

    if existing_patient is None:
        return jsonify({
            "success": False,
            "message": "Patient not found"
        }), 404

    update_patient(patient_id, data)

    return jsonify({
        "success": True,
        "message": "Patient updated successfully"
    }), 200


# =========================
# DELETE PATIENT
# =========================

@patient_bp.route("/<patient_id>", methods=["DELETE"])
def remove_patient(patient_id):

    existing_patient = get_patient(patient_id)

    if existing_patient is None:
        return jsonify({
            "success": False,
            "message": "Patient not found"
        }), 404

    delete_patient(patient_id)

    return jsonify({
        "success": True,
        "message": "Patient deleted successfully"
    }), 200