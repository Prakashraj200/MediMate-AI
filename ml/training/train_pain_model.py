"""
ML Training Pipeline: Post-Accident Pain & Physiotherapy Recovery Prediction Model.
Predicts Recovery Trajectory and Chronic Pain Risk using Random Forest Classifier.
"""

import os
import random
import csv
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "datasets")
MODELS_DIR = os.path.join(BASE_DIR, "saved_models")

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(MODELS_DIR, exist_ok=True)


def generate_pain_rehab_dataset(n_samples=600):
    """Generate realistic post-accident physiotherapy clinical dataset."""
    random.seed(42)
    csv_path = os.path.join(DATA_DIR, "pain_rehab_recovery_data.csv")
    rows = []

    for _ in range(n_samples):
        age = random.randint(18, 78)
        days = random.randint(1, 90)
        adherence = random.randint(20, 100)  # % of physio exercises done
        
        # Pain score tends to decrease with days and higher exercise adherence
        base_pain = max(1.0, min(10.0, 9.0 - (days * 0.08) - (adherence * 0.02) + random.gauss(0, 1.2)))
        pain_score = round(base_pain, 1)

        # Range of motion improves over time with adherence
        base_rom = max(20.0, min(100.0, 30.0 + (days * 0.7) + (adherence * 0.3) + random.gauss(0, 5)))
        rom_pct = round(base_rom, 1)

        # Swelling level (0: None, 1: Mild, 2: Moderate, 3: Severe)
        if days < 14 and pain_score >= 6:
            swelling = random.choice([2, 3])
        elif days > 30 and pain_score <= 4:
            swelling = 0
        else:
            swelling = random.choice([0, 1, 2])

        # Clinical Target: Recovery Risk Class
        # 0: On-Track Recovery (Normal Healing)
        # 1: Delayed Recovery / Stiffness Risk
        # 2: High Risk / Chronic Pain & Complication Risk
        if pain_score <= 4.0 and rom_pct >= 70 and adherence >= 60:
            risk = 0  # On-Track
        elif pain_score >= 7.5 or (days > 45 and rom_pct < 55) or (days > 30 and swelling >= 2):
            risk = 2  # High Risk / Chronic Pain Alert
        else:
            risk = 1  # Delayed / Needs Physio Adjustment

        rows.append({
            "age": age,
            "days_since_accident": days,
            "pain_score": pain_score,
            "exercise_adherence_pct": adherence,
            "mobility_rom_pct": rom_pct,
            "swelling_level": swelling,
            "recovery_risk_tier": risk
        })

    with open(csv_path, mode="w", newline="", encoding="utf-8") as f:
        fieldnames = ["age", "days_since_accident", "pain_score", "exercise_adherence_pct", "mobility_rom_pct", "swelling_level", "recovery_risk_tier"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Generated Pain & Rehab Recovery Dataset with {n_samples} records at: {csv_path}")
    return rows, csv_path


def train_pain_model():
    """Train Random Forest model to predict recovery trajectory."""
    rows, csv_path = generate_pain_rehab_dataset()

    try:
        import pandas as pd
        from sklearn.model_selection import train_test_split
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.metrics import accuracy_score
        import joblib

        df = pd.read_csv(csv_path)
        feature_cols = ["age", "days_since_accident", "pain_score", "exercise_adherence_pct", "mobility_rom_pct", "swelling_level"]
        X = df[feature_cols]
        y = df["recovery_risk_tier"]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = RandomForestClassifier(n_estimators=100, max_depth=8, random_state=42)
        model.fit(X_train, y_train)

        acc = accuracy_score(y_test, model.predict(X_test))
        print(f"Pain Recovery Model trained with Scikit-Learn. Test Accuracy: {acc * 100:.2f}%")

        model_path = os.path.join(MODELS_DIR, "pain_recovery_model.joblib")
        joblib.dump(model, model_path)
        print(f"Model saved successfully to: {model_path}")
        return model_path

    except Exception as e:
        print(f"Standard library fallback: {e}")
        return None


if __name__ == "__main__":
    train_pain_model()
