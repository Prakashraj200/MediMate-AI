from flask import Blueprint, request, jsonify

from backend.services.firebase_service import (
    get_all_pharmacies,
    get_pharmacy,
    create_pharmacy,
    update_pharmacy,
    delete_pharmacy
)


pharmacy_bp = Blueprint(
    "pharmacy",
    __name__,
    url_prefix="/api/pharmacies"
)


# =========================
# GET ALL PHARMACIES
# =========================

@pharmacy_bp.route("/", methods=["GET"])
def pharmacies():

    pharmacies = get_all_pharmacies()

    return jsonify({
        "success": True,
        "pharmacies": pharmacies
    }), 200


# =========================
# GET ONE PHARMACY
# =========================

@pharmacy_bp.route("/<pharmacy_id>", methods=["GET"])
def pharmacy(pharmacy_id):

    pharmacy_data = get_pharmacy(pharmacy_id)

    if pharmacy_data is None:
        return jsonify({
            "success": False,
            "message": "Pharmacy not found"
        }), 404

    return jsonify({
        "success": True,
        "pharmacy": pharmacy_data
    }), 200


# =========================
# CREATE PHARMACY
# =========================

@pharmacy_bp.route("/", methods=["POST"])
def add_pharmacy():

    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "message": "Pharmacy data is required"
        }), 400

    pharmacy_id = create_pharmacy(data)

    return jsonify({
        "success": True,
        "message": "Pharmacy created successfully",
        "pharmacy_id": pharmacy_id
    }), 201


# =========================
# UPDATE PHARMACY
# =========================

@pharmacy_bp.route("/<pharmacy_id>", methods=["PUT"])
def edit_pharmacy(pharmacy_id):

    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "message": "Update data is required"
        }), 400

    existing_pharmacy = get_pharmacy(pharmacy_id)

    if existing_pharmacy is None:
        return jsonify({
            "success": False,
            "message": "Pharmacy not found"
        }), 404

    update_pharmacy(pharmacy_id, data)

    return jsonify({
        "success": True,
        "message": "Pharmacy updated successfully"
    }), 200


# =========================
# DELETE PHARMACY
# =========================

@pharmacy_bp.route("/<pharmacy_id>", methods=["DELETE"])
def remove_pharmacy(pharmacy_id):

    existing_pharmacy = get_pharmacy(pharmacy_id)

    if existing_pharmacy is None:
        return jsonify({
            "success": False,
            "message": "Pharmacy not found"
        }), 404

    delete_pharmacy(pharmacy_id)

    return jsonify({
        "success": True,
        "message": "Pharmacy deleted successfully"
    }), 200