from flask import jsonify


def success_response(data=None, message="Success", status_code=200):
    """Standardized API success JSON response."""
    payload = {
        "success": True,
        "message": message
    }
    if data is not None:
        if isinstance(data, dict):
            payload.update(data)
        else:
            payload["data"] = data
            
    return jsonify(payload), status_code


def error_response(message="An error occurred", status_code=400, errors=None):
    """Standardized API error JSON response."""
    payload = {
        "success": False,
        "message": message
    }
    if errors is not None:
        payload["errors"] = errors
        
    return jsonify(payload), status_code
