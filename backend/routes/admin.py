from flask import Blueprint, request, jsonify

from backend.services.firebase_service import (
    get_all_users,
    get_user,
    create_user,
    update_user,
    delete_user
)


admin_bp = Blueprint(
    "admin",
    __name__,
    url_prefix="/api/admin"
)


# =========================
# GET ALL USERS
# =========================

@admin_bp.route("/users", methods=["GET"])
def users():

    users = get_all_users()

    return jsonify({
        "success": True,
        "users": users
    }), 200


# =========================
# GET ONE USER
# =========================

@admin_bp.route("/users/<user_id>", methods=["GET"])
def user(user_id):

    user_data = get_user(user_id)

    if user_data is None:
        return jsonify({
            "success": False,
            "message": "User not found"
        }), 404

    return jsonify({
        "success": True,
        "user": user_data
    }), 200


# =========================
# CREATE USER
# =========================

@admin_bp.route("/users", methods=["POST"])
def add_user():

    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "message": "User data is required"
        }), 400

    user_id = create_user(data)

    return jsonify({
        "success": True,
        "message": "User created successfully",
        "user_id": user_id
    }), 201


# =========================
# UPDATE USER
# =========================

@admin_bp.route("/users/<user_id>", methods=["PUT"])
def edit_user(user_id):

    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "message": "Update data is required"
        }), 400

    existing_user = get_user(user_id)

    if existing_user is None:
        return jsonify({
            "success": False,
            "message": "User not found"
        }), 404

    update_user(user_id, data)

    return jsonify({
        "success": True,
        "message": "User updated successfully"
    }), 200


# =========================
# DELETE USER
# =========================

@admin_bp.route("/users/<user_id>", methods=["DELETE"])
def remove_user(user_id):

    existing_user = get_user(user_id)

    if existing_user is None:
        return jsonify({
            "success": False,
            "message": "User not found"
        }), 404

    delete_user(user_id)

    return jsonify({
        "success": True,
        "message": "User deleted successfully"
    }), 200