"""
Physiotherapy Rehabilitation & Post-Accident Pain Management Routes.
Serves:
1. 105 Clinical Q&A Knowledge Base
2. Daily VAS Pain Logging & Tracking
3. ML Recovery Trajectory & Chronic Pain Risk Prediction
4. Prescribed Home Exercises & Red-Flag Triage
"""

from flask import Blueprint, request, jsonify
from ai.physio_pain_dataset import PHYSIO_PAIN_KNOWLEDGE_BASE, query_pain_knowledge_base
from ml.pain_recovery_predictor import predict_recovery_risk
from backend.utils.response import success_response, error_response

physio_rehab_bp = Blueprint("physio_rehab", __name__, url_prefix="/api/rehab")

# In-memory storage for demonstration / local mode (backed by session/cache)
_pain_logs = [
    {
        "id": "log-001",
        "patient_id": "P-101",
        "patient_name": "Karthik Subramanian",
        "injury_type": "Whiplash & Cervical Strain (Bike Accident)",
        "days_since_accident": 18,
        "pain_score": 5.5,
        "mobility_rom_pct": 65,
        "exercise_adherence_pct": 75,
        "swelling_level": 1,
        "date": "2026-10-21"
    },
    {
        "id": "log-002",
        "patient_id": "P-102",
        "patient_name": "Priya Natarajan",
        "injury_type": "Knee Meniscus & ACL Sprain",
        "days_since_accident": 34,
        "pain_score": 3.0,
        "mobility_rom_pct": 82,
        "exercise_adherence_pct": 90,
        "swelling_level": 0,
        "date": "2026-10-21"
    },
    {
        "id": "log-003",
        "patient_id": "P-103",
        "patient_name": "Manoj Kumar",
        "injury_type": "Lumbar Spine Disc Herniation",
        "days_since_accident": 45,
        "pain_score": 7.5,
        "mobility_rom_pct": 48,
        "exercise_adherence_pct": 40,
        "swelling_level": 2,
        "date": "2026-10-21"
    }
]

_prescribed_exercises = [
    {
        "id": "ex-01",
        "name": "Cervical Chin Tucks",
        "category": "Neck & Whiplash",
        "sets": 3,
        "reps": 10,
        "hold_sec": 5,
        "instruction": "Gently retract neck straight back creating a subtle double chin. Never tilt chin down.",
        "precautions": "Pain should not radiate into shoulders."
    },
    {
        "id": "ex-02",
        "name": "Isometric Quad Sets",
        "category": "Knee & Lower Limb",
        "sets": 3,
        "reps": 12,
        "hold_sec": 5,
        "instruction": "Tighten top thigh muscle pushing back of knee flat into towel roll.",
        "precautions": "Do not hold breath; engage quadriceps smoothly."
    },
    {
        "id": "ex-03",
        "name": "Pelvic Tilts & Bridge",
        "category": "Lumbar Spine",
        "sets": 2,
        "reps": 10,
        "hold_sec": 4,
        "instruction": "Flatten lower back against floor by tightening abdominals, then gently lift pelvis.",
        "precautions": "Avoid hyperextension of lumbar arch."
    },
    {
        "id": "ex-04",
        "name": "Codman Pendulum Exercises",
        "category": "Shoulder & Clavicle",
        "sets": 3,
        "reps": 15,
        "hold_sec": 0,
        "instruction": "Lean forward supporting good arm on table. Let injured arm dangle and sway gently in small circles.",
        "precautions": "Passive motion only; do not actively engage shoulder muscles."
    },
    {
        "id": "ex-05",
        "name": "Ankle Pumps & Alphabet Drills",
        "category": "Ankle & DVT Prevention",
        "sets": 4,
        "reps": 20,
        "hold_sec": 0,
        "instruction": "Move toes up towards shin then down pointing away. Promotes venous blood return.",
        "precautions": "Perform hourly if bedridden to prevent deep vein thrombosis."
    }
]


@physio_rehab_bp.route("/knowledge-base", methods=["GET"])
def get_knowledge_base():
    """Retrieve full or categorized 105 Q&A dataset."""
    category = request.args.get("category")
    search = request.args.get("search", "").strip()

    if search:
        search_match = query_pain_knowledge_base(search)
        return jsonify({
            "success": True,
            "total": len(PHYSIO_PAIN_KNOWLEDGE_BASE),
            "matched": search_match
        })

    if category:
        filtered = [item for item in PHYSIO_PAIN_KNOWLEDGE_BASE if item.get("category") == category]
        return jsonify({
            "success": True,
            "category": category,
            "count": len(filtered),
            "data": filtered
        })

    return jsonify({
        "success": True,
        "total_questions": len(PHYSIO_PAIN_KNOWLEDGE_BASE),
        "categories": [
            "post_accident_recovery",
            "ice_vs_heat",
            "safe_exercises",
            "pain_scale_vas",
            "red_flags"
        ],
        "data": PHYSIO_PAIN_KNOWLEDGE_BASE
    })


@physio_rehab_bp.route("/predict-recovery", methods=["POST"])
def predict_recovery():
    """Predict recovery trajectory & chronic pain risk using ML."""
    data = request.get_json(silent=True) or {}
    age = data.get("age", 32)
    days = data.get("days_since_accident", 14)
    pain = data.get("pain_score", 4.5)
    adherence = data.get("exercise_adherence_pct", 75)
    rom = data.get("mobility_rom_pct", 65)
    swelling = data.get("swelling_level", 1)

    prediction = predict_recovery_risk(
        age=age,
        days_since_accident=days,
        pain_score=pain,
        exercise_adherence_pct=adherence,
        mobility_rom_pct=rom,
        swelling_level=swelling
    )

    return success_response(prediction, "Recovery trajectory prediction calculated")


@physio_rehab_bp.route("/log-pain", methods=["POST"])
def log_pain():
    """Log daily patient pain score (VAS 1-10) and calculate instant recovery tier."""
    data = request.get_json(silent=True) or {}
    patient_id = data.get("patient_id", "P-USER")
    patient_name = data.get("patient_name", "Logged Patient")
    pain_score = float(data.get("pain_score", 5.0))
    days = int(data.get("days_since_accident", 10))
    rom = float(data.get("mobility_rom_pct", 60.0))
    adherence = float(data.get("exercise_adherence_pct", 70.0))
    swelling = int(data.get("swelling_level", 1))
    injury_type = data.get("injury_type", "Post-Trauma Rehabilitation")

    # Run ML prediction
    prediction = predict_recovery_risk(
        age=data.get("age", 35),
        days_since_accident=days,
        pain_score=pain_score,
        exercise_adherence_pct=adherence,
        mobility_rom_pct=rom,
        swelling_level=swelling
    )

    log_entry = {
        "id": f"log-{len(_pain_logs) + 1:03d}",
        "patient_id": patient_id,
        "patient_name": patient_name,
        "injury_type": injury_type,
        "days_since_accident": days,
        "pain_score": pain_score,
        "mobility_rom_pct": rom,
        "exercise_adherence_pct": adherence,
        "swelling_level": swelling,
        "prediction": prediction
    }
    _pain_logs.insert(0, log_entry)

    return success_response({
        "log_entry": log_entry,
        "prediction": prediction
    }, "Daily pain and recovery metric logged successfully")


@physio_rehab_bp.route("/patient-logs", methods=["GET"])
def get_patient_logs():
    """Get pain logs for physiotherapist & patient dashboard."""
    return success_response({
        "total": len(_pain_logs),
        "logs": _pain_logs
    }, "Pain and recovery records retrieved")


@physio_rehab_bp.route("/exercises", methods=["GET"])
def get_exercises():
    """Get standard rehabilitation exercise protocols."""
    return success_response({
        "total": len(_prescribed_exercises),
        "exercises": _prescribed_exercises
    }, "Rehabilitation exercise routines retrieved")
