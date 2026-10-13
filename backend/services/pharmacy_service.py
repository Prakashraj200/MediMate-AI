"""
Pharmacy Service - Pharmacy outlets, medicine inventory, dispensing, and orders.
"""

from backend.services.firebase_service import (
    get_all_pharmacies,
    get_pharmacy,
    create_pharmacy,
    update_pharmacy,
    delete_pharmacy
)


def list_pharmacy_outlets():
    """List pharmacies in network."""
    return get_all_pharmacies()


def get_pharmacy_by_id(pharmacy_id):
    """Get pharmacy outlet details."""
    return get_pharmacy(pharmacy_id)


def add_pharmacy_outlet(pharmacy_data):
    """Add pharmacy outlet."""
    return create_pharmacy(pharmacy_data)


def update_pharmacy_outlet(pharmacy_id, pharmacy_data):
    """Update pharmacy outlet."""
    return update_pharmacy(pharmacy_id, pharmacy_data)


def remove_pharmacy_outlet(pharmacy_id):
    """Delete pharmacy outlet."""
    return delete_pharmacy(pharmacy_id)
