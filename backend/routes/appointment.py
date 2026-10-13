from flask import Blueprint, request
from backend.services.appointment_service import (
    get_all_appointments,
    get_appointment,
    schedule_appointment,
    update_appointment_details,
    cancel_appointment
)
from backend.utils.response import success_response, error_response

appointment_bp = Blueprint("appointment", __name__, url_prefix="/api/appointments")


@appointment_bp.route("/", methods=["GET"])
def list_appointments():
    doctor_id = request.args.get("doctor_id")
    patient_id = request.args.get("patient_id")
    status = request.args.get("status")
    appointments = get_all_appointments(doctor_id, patient_id, status)
    return success_response({"appointments": appointments}, "Appointments retrieved successfully")


@appointment_bp.route("/<appointment_id>", methods=["GET"])
def get_single(appointment_id):
    appointment = get_appointment(appointment_id)
    if not appointment:
        return error_response("Appointment not found", 404)
    return success_response({"appointment": appointment})


@appointment_bp.route("/", methods=["POST"])
def book_new():
    data = request.get_json(silent=True)
    if not data:
        return error_response("Appointment data is required", 400)
    apt_id = schedule_appointment(data)
    return success_response({"appointment_id": apt_id}, "Appointment scheduled successfully", 201)


@appointment_bp.route("/<appointment_id>", methods=["PUT"])
def update_details(appointment_id):
    data = request.get_json(silent=True)
    if not data:
        return error_response("Update data required", 400)
    update_appointment_details(appointment_id, data)
    return success_response(message="Appointment updated successfully")


@appointment_bp.route("/<appointment_id>/cancel", methods=["POST"])
def cancel(appointment_id):
    data = request.get_json(silent=True) or {}
    reason = data.get("reason", "Cancelled by user")
    cancel_appointment(appointment_id, reason)
    return success_response(message="Appointment cancelled successfully")
