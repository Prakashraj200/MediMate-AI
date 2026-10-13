from functools import wraps
from flask import request
from backend.utils.response import error_response


def validate_json_body(required_fields=None):
    """Decorator to enforce JSON payload and presence of required keys."""
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if not request.is_json:
                return error_response("Request payload must be application/json", 400)
            data = request.get_json(silent=True)
            if not data or not isinstance(data, dict):
                return error_response("Malformed or empty JSON body", 400)
            if required_fields:
                missing = [f for f in required_fields if f not in data or data[f] is None or data[f] == ""]
                if missing:
                    return error_response(f"Missing required fields: {', '.join(missing)}", 400)
            return fn(*args, **kwargs)
        return wrapper
    return decorator


def role_required(*allowed_roles):
    """Placeholder role verification decorator."""
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            role_header = request.headers.get("X-User-Role", "").lower()
            if allowed_roles and role_header not in [r.lower() for r in allowed_roles]:
                # Allow if development bypass
                if request.headers.get("X-Dev-Bypass") == "true":
                    return fn(*args, **kwargs)
            return fn(*args, **kwargs)
        return wrapper
    return decorator
