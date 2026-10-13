"""
Recommendation Engine - Maps symptoms to medical specialties, dietary tips, and lifestyle interventions.
"""

SPECIALTY_MAPPING = {
    "chest_pain": "Cardiology",
    "shortness_of_breath": "Pulmonology / Emergency Medicine",
    "hypertension": "Cardiology",
    "headache": "Neurology",
    "fever": "General Medicine",
    "cough": "General Medicine",
    "skin_rash": "Dermatology",
    "dizziness": "General Medicine"
}

LIFESTYLE_TIPS = {
    "hypertension": [
        "Reduce dietary sodium intake to under 2,000 mg daily.",
        "Engage in 30 minutes of brisk walking 5 days a week.",
        "Eat potassium-rich foods such as spinach, bananas, and coconut water."
    ],
    "headache": [
        "Maintain adequate oral hydration (at least 2.5 liters of water daily).",
        "Take regular 5-minute screen breaks every hour.",
        "Ensure 7 to 8 hours of restorative sleep."
    ],
    "fever": [
        "Rest completely and stay well hydrated with electrolyte fluids.",
        "Wear lightweight, breathable clothing.",
        "Use lukewarm sponge compresses if temperature is elevated."
    ]
}


def get_recommendations(detected_symptoms):
    """Generate recommendations based on analyzed symptoms."""
    suggested_specialists = list({
        SPECIALTY_MAPPING.get(s, "General Medicine") for s in detected_symptoms
    }) if detected_symptoms else ["General Medicine"]

    tips = []
    for s in detected_symptoms:
        if s in LIFESTYLE_TIPS:
            tips.extend(LIFESTYLE_TIPS[s])

    if not tips:
        tips = [
            "Maintain balanced nutrition and adequate hydration.",
            "Monitor everyday vital signs regularly.",
            "Consult a licensed physician for any unresolved discomfort."
        ]

    return {
        "primary_specialty": suggested_specialists[0],
        "specialists": suggested_specialists,
        "lifestyle_tips": tips[:4]
    }
