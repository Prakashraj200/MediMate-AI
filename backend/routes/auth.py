from flask import Blueprint, request, jsonify
from firebase_admin import auth

from backend.services.auth_service import (
    create_auth_user,
    get_auth_user_by_email,
    get_auth_user_by_uid,
    delete_auth_user
)

from backend.services.firebase_service import (
    create_user,
    get_user
)


auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/api/auth"
)


# =========================
# REGISTER USER
# =========================

@auth_bp.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "message": "Registration data is required"
        }), 400

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    role = data.get("role")

    if not name or not email or not password or not role:
        return jsonify({
            "success": False,
            "message": "Name, email, password and role are required"
        }), 400

    existing_user = get_auth_user_by_email(email)

    if existing_user is not None:
        return jsonify({
            "success": False,
            "message": "Email already registered"
        }), 409

    try:

        auth_user = create_auth_user(
            email,
            password
        )

        user_data = {
            "uid": auth_user.uid,
            "name": name,
            "email": email,
            "role": role.lower()
        }

        firestore_user_id = create_user(user_data)

        return jsonify({
            "success": True,
            "message": "User registered successfully",
            "uid": auth_user.uid,
            "user_id": firestore_user_id
        }), 201

    except Exception as e:

        return jsonify({
            "success": False,
            "message": str(e)
        }), 500


# =========================
# VERIFY FIREBASE ID TOKEN
# =========================

@auth_bp.route("/verify-token", methods=["POST"])
def verify_token():

    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "message": "Token is required"
        }), 400

    id_token = data.get("idToken")

    if not id_token:
        return jsonify({
            "success": False,
            "message": "Firebase ID token is required"
        }), 400

    try:

        decoded_token = auth.verify_id_token(id_token)

        uid = decoded_token.get("uid")

        auth_user = get_auth_user_by_uid(uid)

        if auth_user is None:
            return jsonify({
                "success": False,
                "message": "Authentication user not found"
            }), 404

        # Find Firestore profile using UID
        user_profile = None

        from config.firebase_config import db

        users = (
            db.collection("users")
            .where("uid", "==", uid)
            .limit(1)
            .stream()
        )

        for doc in users:
            user_profile = doc.to_dict()
            user_profile["id"] = doc.id
            break

        if user_profile is None:
            return jsonify({
                "success": False,
                "message": "User profile not found"
            }), 404

        return jsonify({
            "success": True,
            "message": "Token verified successfully",
            "uid": uid,
            "email": auth_user.email,
            "user": user_profile
        }), 200

    except Exception as e:

        return jsonify({
            "success": False,
            "message": "Invalid or expired Firebase token"
        }), 401


# =========================
# GET AUTH USER
# =========================

@auth_bp.route("/user/<uid>", methods=["GET"])
def get_auth_user(uid):

    user = get_auth_user_by_uid(uid)

    if user is None:
        return jsonify({
            "success": False,
            "message": "Authentication user not found"
        }), 404

    return jsonify({
        "success": True,
        "uid": user.uid,
        "email": user.email,
        "disabled": user.disabled
    }), 200


# =========================
# DELETE AUTH USER
# =========================

@auth_bp.route("/user/<uid>", methods=["DELETE"])
def remove_auth_user(uid):

    user = get_auth_user_by_uid(uid)

    if user is None:
        return jsonify({
            "success": False,
            "message": "Authentication user not found"
        }), 404

    delete_auth_user(uid)

    return jsonify({
        "success": True,
        "message": "Authentication user deleted successfully"
    }), 200