from flask import Blueprint, request
from backend.services.prescription_service import (
    get_all_prescriptions,
    get_prescription_by_id,
    issue_prescription,
    update_prescription_status
)
from backend.utils.response import success_response, error_response

prescription_bp = Blueprint("prescription", __name__, url_prefix="/api/prescriptions")


@prescription_bp.route("/", methods=["GET"])
def list_prescriptions():
    patient_id = request.args.get("patient_id")
    doctor_id = request.args.get("doctor_id")
    prescriptions = get_all_prescriptions(patient_id, doctor_id)
    return success_response({"prescriptions": prescriptions})


@prescription_bp.route("/<rx_id>", methods=["GET"])
def get_prescription(rx_id):
    prescription = get_prescription_by_id(rx_id)
    if not prescription:
        return error_response("Prescription not found", 404)
    return success_response({"prescription": prescription})


@prescription_bp.route("/", methods=["POST"])
def create_prescription():
    data = request.get_json(silent=True)
    if not data or not data.get("medicines"):
        return error_response("Prescription medicines data required", 400)
    rx_id = issue_prescription(data)
    return success_response({"prescription_id": rx_id}, "Electronic prescription issued", 201)


@prescription_bp.route("/<rx_id>/status", methods=["PUT"])
def change_status(rx_id):
    data = request.get_json(silent=True) or {}
    update_prescription_status(rx_id, data)
    return success_response(message="Prescription status updated")
