# MediMate-AI: Comprehensive User & Operational Guide

## 1. Getting Started

### 1.1 Server Startup
Ensure the Python virtual environment is activated and start the Flask server:
```bash
venv\Scripts\python.exe app.py
```
Open your web browser and navigate to:
**`http://127.0.0.1:5000`**

---

## 2. Portal User Guides

### 2.1 Patient Portal (`/frontend/patient/dashboard.html`)
- **Login / Register**: Access via `/frontend/patient/patient-login.html` or `/frontend/register.html`.
- **Preethi AI**: Click **Preethi AI** in the sidebar. Describe symptoms by typing or clicking the microphone icon. Follow triage advice or click suggested prompt chips.
- **Appointments**: View upcoming visits or book a new appointment with any hospital specialist.
- **Vitals & Telemetry**: Monitor live Blood Pressure, Heart Rate, SpO2, and Blood Sugar. Click **Record New Vital** to save readings.
- **Medicines & Adherence**: Review daily morning, afternoon, and bedtime medication schedules.
- **Lab Reports**: Download and view verified diagnostic reports from the hospital laboratory.

### 2.2 Doctor Portal (`/frontend/doctor/dashboard.html`)
- **Login**: Access via `/frontend/doctor/doctor-login.html`.
- **Appointments Queue**: Check today's scheduled consultations. Click **Start Consult** to join encrypted telehealth video calls or attend walk-in patients.
- **Patient Records (EHR)**: View longitudinal medical history, allergy lists, and write clinical **SOAP notes** (Subjective, Objective, Assessment, Plan).
- **e-Prescribing Pad**: Click **Write Prescription** to author tamper-proof digital prescriptions with automated interaction checks.
- **Telemetry Monitoring**: Monitor patients on remote telemetry. Receive immediate red alerts for hypertensive crises or desaturations.

### 2.3 Laboratory Portal (`/frontend/laboratory/dashboard.html`)
- **Login**: Access via `/frontend/laboratory/lab-login.html`.
- **Requisition Intake**: Scan specimen barcodes and confirm blood/sample collection.
- **Results Entry**: Enter observed analyte values. Automatic algorithms verify whether parameters fall within biological reference intervals.
- **Diagnostic Reports**: Pathologist review and digital release stamp publishing reports to doctors and patients.

### 2.4 Pharmacy Portal (`/frontend/pharmacy/dashboard.html`)
- **Login**: Access via `/frontend/pharmacy/pharmacy-login.html`.
- **Dispensation Queue**: View incoming doctor prescriptions. Click **Dispense** to verify drug items, generate dispensing labels, and deduct stock.
- **Stock & Inventory**: Track shelf locations (Aisles/Bins) and view critical reorder alerts.
- **Expiry Surveillance**: Isolate near-expiry batches (< 30 days) into quarantine lockboxes.

### 2.5 Admin Portal (`/frontend/admin/dashboard.html`)
- **Login**: Access via `/frontend/admin/admin-login.html` (Credentials: `admin@medimate.ai` / `admin123`).
- **Hospital Overview**: Executive metrics covering consultations, bed occupancy, laboratory throughput, and financial performance.
- **Broadcast Alerts**: Dispatch emergency notices to all staff or targeted departments.
