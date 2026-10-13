from flask import Blueprint, request, jsonify

from backend.services.firebase_service import (
    get_all_laboratories,
    get_laboratory,
    create_laboratory,
    update_laboratory,
    delete_laboratory
)


# =========================
# LABORATORY BLUEPRINT
# =========================

laboratory_bp = Blueprint(
    "laboratory",
    __name__,
    url_prefix="/api/laboratories"
)


# =========================
# GET ALL LABORATORIES
# =========================

@laboratory_bp.route("/", methods=["GET"])
def laboratories():

    laboratories = get_all_laboratories()

    return jsonify({
        "success": True,
        "laboratories": laboratories
    }), 200


# =========================
# GET SINGLE LABORATORY
# =========================

@laboratory_bp.route("/<laboratory_id>", methods=["GET"])
def laboratory(laboratory_id):

    laboratory_data = get_laboratory(laboratory_id)

    if laboratory_data is None:
        return jsonify({
            "success": False,
            "message": "Laboratory not found"
        }), 404

    return jsonify({
        "success": True,
        "laboratory": laboratory_data
    }), 200


# =========================
# CREATE LABORATORY
# =========================

@laboratory_bp.route("/", methods=["POST"])
def add_laboratory():

    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "message": "Laboratory data is required"
        }), 400

    laboratory_id = create_laboratory(data)

    return jsonify({
        "success": True,
        "message": "Laboratory created successfully",
        "laboratory_id": laboratory_id
    }), 201


# =========================
# UPDATE LABORATORY
# =========================

@laboratory_bp.route("/<laboratory_id>", methods=["PUT"])
def edit_laboratory(laboratory_id):

    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "message": "Update data is required"
        }), 400

    existing_laboratory = get_laboratory(laboratory_id)

    if existing_laboratory is None:
        return jsonify({
            "success": False,
            "message": "Laboratory not found"
        }), 404

    update_laboratory(laboratory_id, data)

    return jsonify({
        "success": True,
        "message": "Laboratory updated successfully"
    }), 200


# =========================
# DELETE LABORATORY
# =========================

@laboratory_bp.route("/<laboratory_id>", methods=["DELETE"])
def remove_laboratory(laboratory_id):

    existing_laboratory = get_laboratory(laboratory_id)

    if existing_laboratory is None:
        return jsonify({
            "success": False,
            "message": "Laboratory not found"
        }), 404

    delete_laboratory(laboratory_id)

    return jsonify({
        "success": True,
        "message": "Laboratory deleted successfully"
    }), 200