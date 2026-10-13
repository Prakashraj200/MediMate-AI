"""
Notification Service - Dispatching and tracking real-time clinical alerts.
"""

from config.firebase_config import db
from backend.utils.helpers import format_iso_timestamp


def get_user_notifications(user_id):
    """Retrieve notifications for user."""
    docs = (
        db.collection("notifications")
        .where("user_id", "==", user_id)
        .order_by("created_at", direction="DESCENDING")
        .limit(30)
        .stream()
    )
    notifications = []
    for doc in docs:
        data = doc.to_dict()
        data["id"] = doc.id
        notifications.append(data)
    return notifications


def create_notification(data):
    """Create notification record."""
    data["created_at"] = format_iso_timestamp()
    if "read" not in data:
        data["read"] = False
    doc_ref = db.collection("notifications").document()
    doc_ref.set(data)
    return doc_ref.id


def mark_notification_as_read(notif_id):
    """Mark single notification read."""
    db.collection("notifications").document(notif_id).update({"read": True})
    return True


def mark_all_user_notifications_read(user_id):
    """Mark all user notifications read."""
    docs = db.collection("notifications").where("user_id", "==", user_id).where("read", "==", False).stream()
    batch = db.batch()
    for doc in docs:
        batch.update(doc.reference, {"read": True})
    batch.commit()
    return True
