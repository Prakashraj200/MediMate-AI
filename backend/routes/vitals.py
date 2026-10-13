from flask import Blueprint, request
from backend.services.vitals_service import (
    get_patient_vitals,
    record_vital_reading,
    classify_vitals
)
from backend.utils.response import success_response, error_response

vitals_bp = Blueprint("vitals", __name__, url_prefix="/api/vitals")


@vitals_bp.route("/patient/<patient_id>", methods=["GET"])
def get_vitals(patient_id):
    records = get_patient_vitals(patient_id)
    return success_response({"vitals": records})


@vitals_bp.route("/", methods=["POST"])
def log_vital():
    data = request.get_json(silent=True)
    if not data or not data.get("patient_id"):
        return error_response("patient_id and readings required", 400)
    
    # Classify BP if available
    if "systolic" in data and "diastolic" in data:
        data["bp_classification"] = classify_vitals(
            float(data["systolic"]), float(data["diastolic"])
        )
        
    vital_id = record_vital_reading(data)
    return success_response({"vital_id": vital_id}, "Vitals recorded successfully", 201)
