from flask import Blueprint, request
from backend.services.medicine_service import (
    get_all_medicines,
    get_medicine_by_id,
    add_medicine,
    update_medicine,
    delete_medicine
)
from backend.utils.response import success_response, error_response

medicine_bp = Blueprint("medicine", __name__, url_prefix="/api/medicines")


@medicine_bp.route("/", methods=["GET"])
def list_medicines():
    medicines = get_all_medicines()
    return success_response({"medicines": medicines})


@medicine_bp.route("/<med_id>", methods=["GET"])
def get_medicine(med_id):
    medicine = get_medicine_by_id(med_id)
    if not medicine:
        return error_response("Medicine not found", 404)
    return success_response({"medicine": medicine})


@medicine_bp.route("/", methods=["POST"])
def create_medicine():
    data = request.get_json(silent=True)
    if not data or not data.get("name"):
        return error_response("Medicine name required", 400)
    med_id = add_medicine(data)
    return success_response({"medicine_id": med_id}, "Medicine added to inventory", 201)


@medicine_bp.route("/<med_id>", methods=["PUT"])
def edit_medicine(med_id):
    data = request.get_json(silent=True)
    if not data:
        return error_response("Update data required", 400)
    update_medicine(med_id, data)
    return success_response(message="Medicine updated successfully")


@medicine_bp.route("/<med_id>", methods=["DELETE"])
def remove_medicine(med_id):
    delete_medicine(med_id)
    return success_response(message="Medicine removed successfully")
