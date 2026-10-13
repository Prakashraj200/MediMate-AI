from flask import Blueprint, request
from backend.services.health_records_service import (
    get_patient_health_summary,
    save_patient_health_summary,
    add_allergy_record
)
from backend.utils.response import success_response, error_response

health_records_bp = Blueprint("health_records", __name__, url_prefix="/api/health-records")


@health_records_bp.route("/<patient_id>", methods=["GET"])
def get_summary(patient_id):
    records = get_patient_health_summary(patient_id)
    if not records:
        return error_response("Health record summary not found", 404)
    return success_response({"health_records": records})


@health_records_bp.route("/<patient_id>", methods=["POST", "PUT"])
def save_summary(patient_id):
    data = request.get_json(silent=True)
    if not data:
        return error_response("Health data required", 400)
    save_patient_health_summary(patient_id, data)
    return success_response(message="Health summary updated successfully")


@health_records_bp.route("/<patient_id>/allergies", methods=["POST"])
def add_allergy(patient_id):
    data = request.get_json(silent=True)
    if not data or not data.get("allergy"):
        return error_response("Allergy item required", 400)
    add_allergy_record(patient_id, data["allergy"])
    return success_response(message="Allergy added to medical record")
