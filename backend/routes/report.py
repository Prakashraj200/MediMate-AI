from flask import Blueprint, request
from backend.services.report_service import (
    get_patient_lab_reports,
    get_single_lab_report,
    create_lab_report,
    update_lab_report
)
from backend.utils.response import success_response, error_response

report_bp = Blueprint("report", __name__, url_prefix="/api/reports")


@report_bp.route("/patient/<patient_id>", methods=["GET"])
def list_reports(patient_id):
    reports = get_patient_lab_reports(patient_id)
    return success_response({"reports": reports})


@report_bp.route("/<report_id>", methods=["GET"])
def get_report(report_id):
    report = get_single_lab_report(report_id)
    if not report:
        return error_response("Diagnostic report not found", 404)
    return success_response({"report": report})


@report_bp.route("/", methods=["POST"])
def add_report():
    data = request.get_json(silent=True)
    if not data or not data.get("test_name"):
        return error_response("test_name and findings required", 400)
    report_id = create_lab_report(data)
    return success_response({"report_id": report_id}, "Diagnostic report saved", 201)


@report_bp.route("/<report_id>", methods=["PUT"])
def edit_report(report_id):
    data = request.get_json(silent=True)
    if not data:
        return error_response("Update data required", 400)
    update_lab_report(report_id, data)
    return success_response(message="Diagnostic report updated")
