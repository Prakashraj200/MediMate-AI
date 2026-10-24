"""
Tele-Rehabilitation Video Consultation Service (Google Meet / WebRTC Style).
Provides:
1. Virtual Meeting Room Generation (Room code, host, participant)
2. Live In-Call Session Metadata
3. Real-time Exercise Demonstration Notes & In-Call Chat
"""

import time
import random
from flask import Blueprint, request, jsonify
from backend.utils.response import success_response, error_response

tele_rehab_bp = Blueprint("tele_rehab", __name__, url_prefix="/api/tele-rehab")

# Active meeting rooms
_active_sessions = {
    "rehab-meet-101": {
        "room_id": "rehab-meet-101",
        "room_code": "med-phx-kth",
        "title": "Post-Accident Cervical & Whiplash Mobility Assessment",
        "host_name": "Dr. Anand Kumar (Senior Physiotherapist)",
        "patient_name": "Karthik Subramanian (Rehab Patient)",
        "status": "LIVE",
        "started_at": "16:00",
        "meet_link": "/tele-rehab.html?room=rehab-meet-101",
        "guidelines": [
            "Ensure camera captures full upper body posture from side view.",
            "Wear loose, comfortable clothing for neck and shoulder rotation drills.",
            "Keep resistance band or towel roll ready nearby."
        ]
    }
}

_meeting_chat = [
    {
        "sender": "Dr. Anand Kumar",
        "role": "physio",
        "time": "16:02",
        "text": "Hello Karthik! Please align your camera so I can view your cervical extension angle."
    },
    {
        "sender": "Karthik Subramanian",
        "role": "patient",
        "time": "16:03",
        "text": "Yes doctor, camera is set. Today neck stiffness is around VAS 4."
    }
]


@tele_rehab_bp.route("/session/<room_id>", methods=["GET"])
@tele_rehab_bp.route("/session", methods=["GET"])
def get_session(room_id="rehab-meet-101"):
    """Get active tele-rehabilitation session details."""
    session = _active_sessions.get(room_id, _active_sessions["rehab-meet-101"])
    return success_response({
        "session": session,
        "chat_messages": _meeting_chat
    }, "Tele-rehab session loaded")


@tele_rehab_bp.route("/create-room", methods=["POST"])
def create_room():
    """Create a new Google Meet style consultation room."""
    data = request.get_json(silent=True) or {}
    title = data.get("title", "Post-Accident Physical Therapy Assessment")
    host = data.get("host_name", "Dr. Anand Kumar")
    patient = data.get("patient_name", "Karthik Subramanian")

    random_code = f"reh-{random.randint(100,999)}-{random.randint(100,999)}"
    room_id = f"room-{int(time.time())}"

    new_room = {
        "room_id": room_id,
        "room_code": random_code,
        "title": title,
        "host_name": host,
        "patient_name": patient,
        "status": "LIVE",
        "started_at": "Just now",
        "meet_link": f"/tele-rehab.html?room={room_id}",
        "guidelines": [
            "Good lighting facing patient's joint movement area.",
            "Stable Wi-Fi connection for uninterrupted posture assessment."
        ]
    }
    _active_sessions[room_id] = new_room

    return success_response(new_room, "New tele-rehab meeting room created")


@tele_rehab_bp.route("/rooms", methods=["GET"])
def get_rooms():
    """Get all active tele-rehab rooms."""
    return success_response({
        "rooms": list(_active_sessions.values()),
        "count": len(_active_sessions)
    }, "Active consultation rooms retrieved")


@tele_rehab_bp.route("/chat", methods=["POST"])
def post_chat():
    """Send in-meeting chat message."""
    data = request.get_json(silent=True) or {}
    sender = data.get("sender", "Participant")
    role = data.get("role", "patient")
    text = data.get("text", "").strip()

    if not text:
        return error_response("Message cannot be empty", 400)

    time_str = time.strftime("%H:%M")
    msg = {
        "sender": sender,
        "role": role,
        "time": time_str,
        "text": text
    }
    _meeting_chat.append(msg)
    return success_response(msg, "Message sent")


@tele_rehab_bp.route("/chat", methods=["GET"])
def get_chat():
    """Get in-meeting chat messages."""
    return success_response({"messages": _meeting_chat}, "Chat retrieved")
