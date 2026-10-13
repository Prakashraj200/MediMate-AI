"""
MediMate-AI - AI & Preethi AI Clinical Engine Configuration
"""

import os

AI_CONFIG = {
    "engine_name": "Preethi AI Health Assistant",
    "version": "2.4.0",
    "emergency_keywords": [
        "chest pain", "heart attack", "cannot breathe", "shortness of breath",
        "stroke", "numbness", "severe bleeding", "unconscious", "cyanosis",
        "paralysis", "anaphylaxis", "severe burn", "head trauma"
    ],
    "emergency_hotline": "108 / 911",
    "triage_levels": {
        "emergency": 1,
        "urgent": 2,
        "routine": 3,
        "self_care": 4
    },
    "vital_normal_ranges": {
        "systolic_bp": (90, 130),
        "diastolic_bp": (60, 85),
        "heart_rate": (60, 100),
        "fasting_blood_glucose": (70, 100),
        "spo2": (95, 100),
        "temperature_f": (97.0, 99.5),
        "bmi": (18.5, 24.9)
    },
    "recommendation_limits": {
        "max_medications": 5,
        "max_lifestyle_tips": 4
    }
}
