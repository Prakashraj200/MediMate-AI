from datetime import datetime, timezone
import uuid


def generate_unique_id(prefix="MM"):
    """Generate standardized ID with prefix and timestamp component."""
    unique_part = uuid.uuid4().hex[:8].upper()
    return f"{prefix}-{unique_part}"


def format_iso_timestamp():
    """Current UTC timestamp in ISO 8601 string."""
    return datetime.now(timezone.utc).isoformat()


def sanitize_dict(data, allowed_keys):
    """Filter dictionary to only contain allowed keys."""
    if not isinstance(data, dict):
        return {}
    return {k: v for k, v in data.items() if k in allowed_keys}
