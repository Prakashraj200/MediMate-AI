# MediMate-AI: Project Overview

## 1. Executive Summary
**MediMate-AI** is an intelligent, integrated healthcare management and clinical decision-support ecosystem. Built with a modern Python Flask backend, Firebase cloud infrastructure, and an intuitive emerald-themed frontend, MediMate-AI bridges the gap between patients, clinicians, diagnostic laboratories, and pharmacy dispensaries.

---

## 2. Core Pillars & Stakeholder Portals

| Portal | Target User | Key Capabilities |
| :--- | :--- | :--- |
| **Patient Portal** | Patients & Caregivers | Appointment booking, live vitals telemetry, prescription medication adherence, Preethi AI conversational symptom triage, diagnostic lab report access, and Emergency Medical ID generation. |
| **Doctor Portal** | Physicians & Specialists | Daily consultation queues, encrypted WebRTC telehealth rooms, longitudinal Electronic Health Records (EHR) with SOAP notes, digital e-prescribing with interaction safety checks, and remote biometric tele-monitoring. |
| **Laboratory Portal** | Pathologists & Technicians | Test catalog management (Hematology, Biochemistry, etc.), sample requisition intake with specimen barcoding, automated analyte result recording with biological reference range validation, and pathologist sign-off. |
| **Pharmacy Portal** | Pharmacists | Real-time e-prescription filling and dispensation, drug formulary management, warehouse stock levels, supplier replenishment consignments, and near-expiry surveillance. |
| **Admin Portal** | Hospital Directors & IT Officers | System-wide statistics and occupancy tracking, staff and patient access control, central drug catalog administration, hospital-wide broadcast dispatch, and security policy management. |

---

## 3. Preethi AI Clinical Intelligence
MediMate-AI integrates **Preethi AI**, an autonomous clinical triage assistant capable of:
- Processing natural language symptom descriptions.
- Providing differential triage recommendations with department routing.
- Real-time life-threatening emergency keyword detection (triggering immediate ER protocols).
- Text-to-speech synthesis and voice input support.

---

## 4. Technology Stack Summary
- **Backend**: Python 3.10+, Flask, REST API Blueprints, Firebase Admin SDK.
- **Frontend**: Vanilla HTML5, CSS3 (Emerald Healthcare Design System), Vanilla JavaScript (ES6+), FontAwesome Icons.
- **Database & Auth**: Google Firebase Authentication, Cloud Firestore, local fallback cache.
- **Machine Learning**: Random Forest clinical triage classifier trained on physiological telemetry.
