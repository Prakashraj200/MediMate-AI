from flask import Blueprint, request
from backend.services.notification_service import (
    get_user_notifications,
    create_notification,
    mark_notification_as_read,
    mark_all_user_notifications_read
)
from backend.utils.response import success_response, error_response

notification_bp = Blueprint("notification", __name__, url_prefix="/api/notifications")


@notification_bp.route("/user/<user_id>", methods=["GET"])
def list_notifications(user_id):
    notifications = get_user_notifications(user_id)
    return success_response({"notifications": notifications})


@notification_bp.route("/", methods=["POST"])
def send_notification():
    data = request.get_json(silent=True)
    if not data or not data.get("user_id") or not data.get("title"):
        return error_response("user_id and title required", 400)
    notif_id = create_notification(data)
    return success_response({"notification_id": notif_id}, "Notification dispatched", 201)


@notification_bp.route("/<notif_id>/read", methods=["PUT"])
def mark_read(notif_id):
    mark_notification_as_read(notif_id)
    return success_response(message="Notification marked as read")


@notification_bp.route("/user/<user_id>/read-all", methods=["PUT"])
def mark_all_read(user_id):
    mark_all_user_notifications_read(user_id)
    return success_response(message="All notifications marked as read")
