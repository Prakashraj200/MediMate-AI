# MediMate-AI: Database Design & Schema Documentation

## 1. Overview
MediMate-AI utilizes **Google Cloud Firestore**, a flexible, scalable NoSQL document database, structured around dedicated clinical, pharmaceutical, and operational collections.

---

## 2. Collection Schemas

### 2.1 `users`
Stores authenticated user accounts across all hospital portals.
```json
{
  "uid": "FIREBASE_UID_STRING",
  "name": "Dr. Sarah Connor",
  "email": "sarah.connor@medimate.ai",
  "role": "doctor", // patient | doctor | admin | laboratory | pharmacy
  "phone": "+1-555-349-8120",
  "created_at": "2026-10-12T10:00:00Z",
  "is_active": true
}
```

### 2.2 `patients`
Detailed demographic and baseline clinical data for registered patients.
```json
{
  "id": "PAT_DOC_ID",
  "user_id": "FIREBASE_UID_STRING",
  "mrn": "MRN-1001",
  "name": "John Doe",
  "date_of_birth": "1981-04-12",
  "gender": "Male",
  "blood_group": "O+",
  "allergies": ["Penicillin"],
  "chronic_conditions": ["Essential Hypertension Stage 2"],
  "emergency_contact": {
    "name": "Jane Doe",
    "relation": "Spouse",
    "phone": "+1-555-019-4820"
  }
}
```

### 2.3 `doctors`
Professional credentials and clinic practice configuration.
```json
{
  "id": "DOC_DOC_ID",
  "user_id": "FIREBASE_UID_STRING",
  "name": "Dr. Sarah Connor",
  "specialty": "Cardiology",
  "license_number": "MD-CARD-7842-CA",
  "department_id": "DEP-CARD",
  "room_number": "Room 304, 3rd Floor",
  "experience_years": 14,
  "consultation_fee": 120.00
}
```

### 2.4 `appointments`
Outpatient and telehealth consultation bookings.
```json
{
  "id": "APT_DOC_ID",
  "patient_id": "PAT_DOC_ID",
  "patient_name": "Sarah Jenkins",
  "doctor_id": "DOC_DOC_ID",
  "doctor_name": "Dr. Sarah Connor",
  "date": "2026-10-14",
  "time": "09:30 AM",
  "mode": "telehealth", // in-clinic | telehealth
  "reason": "Recurring Migraines",
  "status": "confirmed" // confirmed | waiting | in-consultation | completed | cancelled
}
```

### 2.5 `prescriptions`
Electronic prescriptions authored by physicians.
```json
{
  "id": "RX_DOC_ID",
  "rx_number": "RX-9821",
  "patient_id": "PAT_DOC_ID",
  "patient_name": "John Doe",
  "doctor_id": "DOC_DOC_ID",
  "doctor_name": "Dr. Sarah Connor",
  "diagnosis": "Essential Hypertension Stage 2",
  "medications": [
    {
      "name": "Amlodipine Besylate 5mg",
      "dosage": "1 tablet",
      "frequency": "1-0-0",
      "duration": "30 Days",
      "instructions": "Take in morning after breakfast"
    }
  ],
  "date": "2026-10-12",
  "status": "dispensed", // pending | dispensed | cancelled
  "digital_signature": "VERIFIED-SHA256"
}
```

### 2.6 `medicines`
Central pharmacy drug inventory and formulary catalog.
```json
{
  "id": "MED_DOC_ID",
  "batch_code": "PH-701",
  "name": "Amoxicillin 500mg",
  "generic_name": "Amoxicillin Trihydrate",
  "category": "Antibiotics",
  "dosage_form": "Capsule",
  "stock_quantity": 320,
  "unit_price": 14.50,
  "reorder_threshold": 50,
  "expiry_date": "2026-11-20",
  "is_prescription_only": true
}
```

### 2.7 `vitals`
Timestamped biometric telemetry stream logs.
```json
{
  "id": "VIT_DOC_ID",
  "patient_id": "PAT_DOC_ID",
  "timestamp": "2026-10-13T08:30:00Z",
  "systolic": 120,
  "diastolic": 80,
  "heart_rate": 72,
  "spo2": 98,
  "glucose": 95,
  "temperature": 98.6,
  "bmi": 22.4,
  "recorded_by": "Home Monitor"
}
```
