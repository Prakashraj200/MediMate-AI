from flask import Blueprint, request, jsonify

from backend.services.firebase_service import (
    get_all_doctors,
    get_doctor,
    create_doctor,
    update_doctor,
    delete_doctor
)


doctor_bp = Blueprint("doctor", __name__, url_prefix="/api/doctors")


# GET ALL DOCTORS
@doctor_bp.route("/", methods=["GET"])
def doctors():
    doctors = get_all_doctors()

    return jsonify({
        "success": True,
        "doctors": doctors
    }), 200


# GET SINGLE DOCTOR
@doctor_bp.route("/<doctor_id>", methods=["GET"])
def doctor(doctor_id):
    doctor_data = get_doctor(doctor_id)

    if doctor_data is None:
        return jsonify({
            "success": False,
            "message": "Doctor not found"
        }), 404

    return jsonify({
        "success": True,
        "doctor": doctor_data
    }), 200


# CREATE DOCTOR
@doctor_bp.route("/", methods=["POST"])
def add_doctor():
    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "message": "Doctor data is required"
        }), 400

    doctor_id = create_doctor(data)

    return jsonify({
        "success": True,
        "message": "Doctor created successfully",
        "doctor_id": doctor_id
    }), 201


# UPDATE DOCTOR
@doctor_bp.route("/<doctor_id>", methods=["PUT"])
def edit_doctor(doctor_id):
    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "message": "Update data is required"
        }), 400

    existing_doctor = get_doctor(doctor_id)

    if existing_doctor is None:
        return jsonify({
            "success": False,
            "message": "Doctor not found"
        }), 404

    update_doctor(doctor_id, data)

    return jsonify({
        "success": True,
        "message": "Doctor updated successfully"
    }), 200


# DELETE DOCTOR
@doctor_bp.route("/<doctor_id>", methods=["DELETE"])
def remove_doctor(doctor_id):
    existing_doctor = get_doctor(doctor_id)

    if existing_doctor is None:
        return jsonify({
            "success": False,
            "message": "Doctor not found"
        }), 404

    delete_doctor(doctor_id)

    return jsonify({
        "success": True,
        "message": "Doctor deleted successfully"
    }), 200