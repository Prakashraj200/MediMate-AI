"""
Laboratory Service - Diagnostic test requests, lab facilities, and specimen handling.
"""

from backend.services.firebase_service import (
    get_all_laboratories,
    get_laboratory,
    create_laboratory,
    update_laboratory,
    delete_laboratory
)


def list_laboratories():
    """List certified laboratory units."""
    return get_all_laboratories()


def get_laboratory_details(lab_id):
    """Get laboratory facility info."""
    return get_laboratory(lab_id)


def add_laboratory_center(lab_data):
    """Add new laboratory center."""
    return create_laboratory(lab_data)


def update_laboratory_center(lab_id, lab_data):
    """Update lab info."""
    return update_laboratory(lab_id, lab_data)


def remove_laboratory_center(lab_id):
    """Remove lab center."""
    return delete_laboratory(lab_id)
