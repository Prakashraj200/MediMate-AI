# 🏥 MediMate-AI: Integrated Clinical Decision-Support & Healthcare Management System

[![Python](https://img.shields.io/badge/Python-3.10+-087f5b?style=flat&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-Framework-075e45?style=flat&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Firebase](https://img.shields.io/badge/Firebase-Admin%20%26%20Firestore-f59e0b?style=flat&logo=firebase&logoColor=white)](https://firebase.google.com/)
[![License](https://img.shields.io/badge/License-Proprietary%20Healthcare-0284c7?style=flat)](LICENSE)

MediMate-AI is an end-to-end, multi-portal healthcare information system and clinical decision-support suite powered by **Preethi AI**. It interconnects patients, physicians, diagnostic laboratories, pharmacy dispensaries, and hospital administrators into a unified, high-performance ecosystem.

---

## 🌟 Key Features & Stakeholder Portals

| Portal | Role | Core Features |
| :--- | :--- | :--- |
| 🧑‍🤝‍🧑 **Patient** | Patient / Caregiver | Telehealth appointment booking, live biometric vitals telemetry, daily medication adherence schedule, Preethi AI conversational clinical triage, official lab reports access, and Emergency Medical ID. |
| 👨‍⚕️ **Doctor** | Physician / Specialist | Daily consultation queue, encrypted WebRTC video call room, longitudinal Electronic Health Records (EHR) with SOAP notes, digital e-prescribing with interaction checks, and remote tele-monitoring. |
| 🧪 **Laboratory** | Pathologist / Tech | Test catalog formulary, specimen accession barcoding, analyte results recording with automated biological reference intervals, and certified pathologist report release. |
| 💊 **Pharmacy** | Pharmacist / Dispensary | Real-time e-prescription filling and dispensation, warehouse inventory levels, supplier PO consignments, and near-expiry surveillance lockbox. |
| 🛡️ **Admin** | Hospital Management | Executive clinical and operations analytics, multi-role user provisioning, formulary drug management, hospital-wide emergency broadcasts, and system security parameters. |

---

## 📁 Directory Structure

```
MediMate-AI/
│
├── app.py                      # Core Flask WSGI server & static router (:5000)
├── requirements.txt            # Python dependencies
├── README.md                   # System documentation & quickstart
├── .env                        # Environment configurations
├── .gitignore                  # Git ignore rules
│
├── config/                     # System & Firebase configurations
│   ├── __init__.py
│   ├── firebase_config.py
│   ├── settings.py
│   └── ai_config.py
│
├── backend/                    # Core REST API application
│   ├── __init__.py
│   ├── routes/                 # 15 isolated Flask Blueprints
│   │   ├── auth.py, admin.py, doctor.py, patient.py, laboratory.py
│   │   ├── pharmacy.py, appointment.py, department.py, medicine.py
│   │   ├── prescription.py, vitals.py, health_records.py, notification.py
│   │   ├── report.py, ai_chat.py
│   │
│   ├── services/               # Business logic domain services
│   │   ├── firebase_service.py, auth_service.py, admin_service.py
│   │   ├── doctor_service.py, patient_service.py, laboratory_service.py
│   │   ├── pharmacy_service.py, appointment_service.py, department_service.py
│   │   ├── medicine_service.py, prescription_service.py, vitals_service.py
│   │   ├── health_records_service.py, notification_service.py, report_service.py
│   │   └── ai_service.py
│   │
│   └── utils/                  # Decorators, response helpers, validators
│       ├── decorators.py, validators.py, helpers.py, response.py
│
├── frontend/                   # Client-side presentation layer
│   ├── index.html              # Landing page
│   ├── register.html           # Universal multi-role registration
│   ├── forgot-password.html    # Account recovery portal
│   │
│   ├── admin/                  # Hospital administration portal (14 views)
│   ├── doctor/                 # Physician & specialist portal (9 views)
│   ├── patient/                # Patient health tracking & triage (13 views)
│   ├── laboratory/             # Diagnostic pathology portal (8 views)
│   ├── pharmacy/               # Dispensary & inventory portal (9 views)
│   │
│   └── static/                 # Modular design assets & scripts
│       ├── css/                # 11 CSS modules (common, auth, dashboard, etc.)
│       ├── js/                 # 18 client-side controllers (api.js, auth.js, etc.)
│       └── images/             # Visual brand assets
│
├── ai/                         # Preethi AI conversational triage engine
│   ├── preethi_ai.py, symptom_analyzer.py, recommendation_engine.py, model_utils.py
│
├── ml/                         # Machine learning training & evaluation
│   ├── notebooks/model_training.ipynb
│   ├── datasets/clinical_triage_data.csv
│   ├── training/train_model.py
│   ├── evaluation/evaluate_model.py
│   └── saved_models/
│
├── tests/                      # Automated unit test suite (15 test cases)
│   ├── test_auth.py, test_admin.py, test_doctor.py, test_patient.py
│   ├── test_laboratory.py, test_pharmacy.py, test_appointments.py, test_departments.py
│
└── docs/                       # Comprehensive documentation
    ├── project-overview.md, architecture.md, database-design.md
    ├── api-documentation.md, data-flow-diagram.md, security.md
    ├── testing.md, user-guide.md
```

---

## 🚀 Quickstart & Installation

### 1. Prerequisites
- Python 3.10+
- Modern Web Browser (Chrome, Firefox, Edge, Safari)

### 2. Environment Setup
```bash
# Clone repository
git clone https://github.com/Prakashraj200/MediMate-AI.git
cd MediMate-AI

# Activate virtual environment
venv\Scripts\activate      # Windows
# source venv/bin/activate  # Linux / macOS

# Install dependencies
pip install -r requirements.txt
```

### 3. Running the Server
```bash
python app.py
```
The server will bind to `http://127.0.0.1:5000` with CORS enabled and serve both the static frontend portals and the REST API.

---

## 🧪 Running Automated Tests
```bash
# Run unit test suite
python -m unittest discover -s tests

# Run ML model evaluation
python ml/evaluation/evaluate_model.py
```

---

## 🔐 Credentials & Default Accounts

| Portal | Email | Password | Role |
| :--- | :--- | :--- | :--- |
| **Admin** | `admin@medimate.ai` | `admin123` | System Administrator |
| **Doctor** | `doctor@medimate.ai` | `doctor123` | Senior Clinician |
| **Patient** | `patient@medimate.ai` | `patient123` | Registered Patient |
| **Laboratory** | `lab@medimate.ai` | `lab123` | Chief Pathologist |
| **Pharmacy** | `pharmacy@medimate.ai` | `pharm123` | Clinical Pharmacist |

---

## 📄 License & Attribution
&copy; 2026 MediMate-AI Healthcare Systems. Developed for modern clinical infrastructure and patient wellness.
