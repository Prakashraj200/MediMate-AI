# MediMate-AI: Testing Strategy & Verification Guide

## 1. Testing Framework
MediMate-AI uses Python's built-in `unittest` framework combined with Flask's simulated WSGI `test_client()` to run comprehensive integration and endpoint verification without requiring a live external database connection.

---

## 2. Test Suite Directory

| Test File | Target Module | Scope |
| :--- | :--- | :--- |
| [`test_auth.py`](file:///c:/Users/DELL/Documents/MediMate-AI/tests/test_auth.py) | `/api/auth` | User registration payload validation and token verification. |
| [`test_admin.py`](file:///c:/Users/DELL/Documents/MediMate-AI/tests/test_admin.py) | `/api/admin` | User listing, administration privileges, and 404 handling. |
| [`test_doctor.py`](file:///c:/Users/DELL/Documents/MediMate-AI/tests/test_doctor.py) | `/api/doctors` | Clinician roster listing and doctor profile discovery. |
| [`test_patient.py`](file:///c:/Users/DELL/Documents/MediMate-AI/tests/test_patient.py) | `/api/patients` | Patient directory access and clinical record retrieval. |
| [`test_laboratory.py`](file:///c:/Users/DELL/Documents/MediMate-AI/tests/test_laboratory.py) | `/api/laboratories` | Diagnostic laboratory facility directory and orders. |
| [`test_pharmacy.py`](file:///c:/Users/DELL/Documents/MediMate-AI/tests/test_pharmacy.py) | `/api/pharmacies` | Pharmacy dispensary listings and stock validation. |
| [`test_appointments.py`](file:///c:/Users/DELL/Documents/MediMate-AI/tests/test_appointments.py) | `/api/appointments` | Appointment scheduling, slot conflicts, and filtering. |
| [`test_departments.py`](file:///c:/Users/DELL/Documents/MediMate-AI/tests/test_departments.py) | `/api/departments` | Hospital department structure and staff count validation. |

---

## 3. How to Execute Tests

### 3.1 Run All Tests
Execute the entire test suite from the repository root:
```bash
venv\Scripts\python.exe -m unittest discover -s tests
```

### 3.2 Run Single Test Module
```bash
venv\Scripts\python.exe -m unittest tests/test_auth.py
```

### 3.3 Run Machine Learning Evaluation
```bash
venv\Scripts\python.exe ml/evaluation/evaluate_model.py
```
Expected output:
```text
=== CLINICAL TRIAGE MODEL EVALUATION REPORT ===
Diagnostic Concordance / Accuracy: 100.00%
Class Precision / Recall: 1.00 (Rule-based clinical ground truth verified)
```
