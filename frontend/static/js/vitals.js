/**
 * MediMate-AI - Biometric Vitals & Telemetry Engine (vitals.js)
 */

const VitalsTelemetry = {
  calculateBmi(weightKg, heightCm) {
    if (!weightKg || !heightCm) return null;
    const heightM = heightCm / 100;
    const bmi = (weightKg / (heightM * heightM)).toFixed(1);
    let category = 'Normal';
    if (bmi < 18.5) category = 'Underweight';
    else if (bmi >= 25 && bmi < 29.9) category = 'Overweight';
    else if (bmi >= 30) category = 'Obese';
    return { bmi: parseFloat(bmi), category };
  },

  checkEmergencyThresholds(vitals = {}) {
    const alerts = [];
    if (vitals.systolic >= 160 || vitals.diastolic >= 100) {
      alerts.push('Hypertensive Crisis (Stage 2 High)');
    }
    if (vitals.heartRate > 110) {
      alerts.push('Tachycardia Warning');
    }
    if (vitals.spo2 && vitals.spo2 < 93) {
      alerts.push('Hypoxia / Low Oxygen Saturation');
    }
    return alerts;
  }
};

window.VitalsTelemetry = VitalsTelemetry;
