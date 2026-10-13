import re


def validate_email(email):
    """Check if email matches basic RFC pattern."""
    if not email or not isinstance(email, str):
        return False
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email.strip()))


def validate_password(password, min_length=6):
    """Check minimum password strength."""
    if not password or not isinstance(password, str):
        return False
    return len(password) >= min_length


def validate_role(role):
    """Validate allowed hospital ecosystem roles."""
    allowed = {"admin", "doctor", "patient", "laboratory", "pharmacy"}
    return str(role).strip().lower() in allowed


def validate_phone(phone):
    """Validate international/Indian mobile phone numbers."""
    if not phone or not isinstance(phone, str):
        return False
    cleaned = re.sub(r"[\s\-\(\)\+]", "", phone)
    return len(cleaned) >= 10 and cleaned.isdigit()


def validate_required_fields(data, required_fields):
    """Validate presence of required keys in JSON payload."""
    if not data or not isinstance(data, dict):
        return False, "Payload must be a valid JSON object."
    missing = [field for field in required_fields if field not in data or data[field] is None or data[field] == ""]
    if missing:
        return False, f"Missing required fields: {', '.join(missing)}"
    return True, None
