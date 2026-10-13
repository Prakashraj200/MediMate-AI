"""
Admin Service - System administration, hospital analytics, and user oversight.
"""

from backend.services.firebase_service import get_all_users, get_user, update_user, delete_user


def get_admin_dashboard_metrics():
    """Aggregate statistics for admin dashboard."""
    users = get_all_users()
    doctors = [u for u in users if u.get("role") == "doctor"]
    patients = [u for u in users if u.get("role") == "patient"]
    labs = [u for u in users if u.get("role") == "laboratory"]
    pharmacies = [u for u in users if u.get("role") == "pharmacy"]

    return {
        "total_users": len(users),
        "total_doctors": len(doctors),
        "total_patients": len(patients),
        "total_laboratories": len(labs),
        "total_pharmacies": len(pharmacies),
        "system_status": "Healthy",
        "database_connected": True
    }


def list_users_by_role(role=None):
    """Filter users by role."""
    users = get_all_users()
    if role:
        return [u for u in users if str(u.get("role", "")).lower() == role.lower()]
    return users


def update_user_status(user_id, status_data):
    """Update user account active/suspended status."""
    return update_user(user_id, status_data)


def remove_system_user(user_id):
    """Delete a user account."""
    return delete_user(user_id)
