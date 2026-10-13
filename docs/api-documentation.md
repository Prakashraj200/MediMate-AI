# MediMate-AI: REST API Documentation

## 1. Authentication Headers
All protected endpoints require a Bearer token in the HTTP Authorization header:
```http
Authorization: Bearer <FIREBASE_ID_TOKEN>
Content-Type: application/json
```

---

## 2. API Endpoints Directory

### 2.1 Authentication (`/api/auth`)
- **`POST /api/auth/register`**
  - **Body**: `{ "name": "...", "email": "...", "password": "...", "role": "patient|doctor|admin|laboratory|pharmacy" }`
  - **Response 201**: `{ "success": true, "uid": "...", "user_id": "..." }`
- **`POST /api/auth/verify-token`**
  - **Body**: `{ "idToken": "..." }`
  - **Response 200**: `{ "success": true, "user": { ... } }`

### 2.2 Users & Administration (`/api/admin`)
- **`GET /api/admin/users`** &rarr; List all registered accounts.
- **`GET /api/admin/users/<id>`** &rarr; Retrieve user by ID.
- **`POST /api/admin/users`** &rarr; Create or provision a staff user account.
- **`PUT /api/admin/users/<id>`** &rarr; Update user details.
- **`DELETE /api/admin/users/<id>`** &rarr; Deactivate account.

### 2.3 Doctors Directory (`/api/doctors`)
- **`GET /api/doctors/`** &rarr; List verified hospital physicians and specialists.
- **`GET /api/doctors/<id>`** &rarr; Retrieve doctor credentials and availability.
- **`POST /api/doctors/`** &rarr; Register new physician profile.

### 2.4 Patients Records (`/api/patients`)
- **`GET /api/patients/`** &rarr; List registered patients.
- **`GET /api/patients/<id>`** &rarr; Retrieve clinical demographics and emergency contacts.
- **`POST /api/patients/`** &rarr; Enroll new patient.

### 2.5 Appointments (`/api/appointments`)
- **`GET /api/appointments/`** &rarr; List consultation bookings.
- **`POST /api/appointments/`** &rarr; Schedule new in-person or telehealth visit.
- **`GET /api/appointments/<id>`** &rarr; Appointment details.
- **`PUT /api/appointments/<id>`** &rarr; Reschedule or update status (confirmed/completed).

### 2.6 Pharmacy & Formulary (`/api/pharmacies`, `/api/medicines`)
- **`GET /api/medicines/`** &rarr; Fetch drug formulary catalog.
- **`POST /api/medicines/`** &rarr; Add new medicine batch.
- **`GET /api/pharmacies/`** &rarr; Fetch pharmacy branch locations and dispensaries.

### 2.7 Electronic Prescriptions (`/api/prescriptions`)
- **`GET /api/prescriptions/`** &rarr; List issued prescriptions.
- **`POST /api/prescriptions/`** &rarr; Author and digitally sign electronic prescription.
- **`PUT /api/prescriptions/<id>`** &rarr; Mark prescription as filled/dispensed.

### 2.8 Diagnostic Laboratories (`/api/laboratories`)
- **`GET /api/laboratories/`** &rarr; List diagnostic facilities.
- **`GET /api/laboratories/<id>`** &rarr; Get laboratory details and accreditation.

### 2.9 Biometric Telemetry (`/api/vitals`)
- **`GET /api/vitals/`** &rarr; Retrieve patient vitals history.
- **`POST /api/vitals/`** &rarr; Record new telemetry sample (BP, HR, SpO2, Glucose).

### 2.10 Preethi AI Clinical Chat (`/api/ai/chat`)
- **`POST /api/ai/chat`**
  - **Body**: `{ "message": "I have sudden severe chest pain radiating to left arm", "history": [] }`
  - **Response 200**:
    ```json
    {
      "success": true,
      "data": {
        "response": "⚠️ EMERGENCY WARNING: Possible acute coronary syndrome...",
        "is_emergency": true,
        "department": "Emergency Medicine"
      }
    }
    ```
