from flask import Blueprint, request
from backend.services.department_service import (
    get_all_departments,
    create_department,
    update_department,
    delete_department
)
from backend.utils.response import success_response, error_response

department_bp = Blueprint("department", __name__, url_prefix="/api/departments")


@department_bp.route("/", methods=["GET"])
def list_departments():
    departments = get_all_departments()
    return success_response({"departments": departments})


@department_bp.route("/", methods=["POST"])
def add_department():
    data = request.get_json(silent=True)
    if not data or not data.get("name"):
        return error_response("Department name is required", 400)
    dept_id = create_department(data)
    return success_response({"department_id": dept_id}, "Department created successfully", 201)


@department_bp.route("/<dept_id>", methods=["PUT"])
def edit_department(dept_id):
    data = request.get_json(silent=True)
    if not data:
        return error_response("Update data required", 400)
    update_department(dept_id, data)
    return success_response(message="Department updated successfully")


@department_bp.route("/<dept_id>", methods=["DELETE"])
def remove_department(dept_id):
    delete_department(dept_id)
    return success_response(message="Department removed successfully")
