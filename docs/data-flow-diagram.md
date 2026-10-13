# MediMate-AI: Data Flow Diagrams

## 1. Patient Triage & Appointment Flow

```mermaid
sequenceDiagram
    autonumber
    actor Patient
    participant PreethiAI as Preethi AI Engine
    participant FlaskAPI as Flask API Gateway
    participant Doctor
    participant Firestore as Cloud Firestore

    Patient->>PreethiAI: Submits symptoms ("Chest tightness, shortness of breath")
    PreethiAI->>PreethiAI: Evaluates risk & emergency keywords
    alt Life-Threatening Emergency
        PreethiAI-->>Patient: Returns Immediate 911 / ER Red Alert
    else Non-Emergency Condition
        PreethiAI-->>Patient: Suggests Department (Cardiology) & Triage notes
        Patient->>FlaskAPI: Books Appointment (/api/appointments)
        FlaskAPI->>Firestore: Inserts appointment record (status: confirmed)
        Firestore-->>Doctor: Updates Doctor Daily Queue
    end
```

---

## 2. Diagnostic Investigation & Lab Report Flow

```mermaid
sequenceDiagram
    autonumber
    actor Doctor
    participant FlaskAPI as Flask API Gateway
    participant LabTech as Laboratory Scientist
    participant Pathologist
    actor Patient

    Doctor->>FlaskAPI: Orders Diagnostic Lab Test (/api/lab_tests)
    FlaskAPI->>LabTech: Generates Specimen Accession Barcode (BAR-9013)
    LabTech->>LabTech: Draws Blood Sample & Runs Automated Analyzer
    LabTech->>FlaskAPI: Inputs Analyte Results (Hb, WBC, Platelets)
    Pathologist->>FlaskAPI: Reviews out-of-range flags & Signs Report
    FlaskAPI-->>Doctor: Notifies Doctor (Results Ready)
    FlaskAPI-->>Patient: Publishes Report to Patient Portal (PDF / Online)
```

---

## 3. Electronic Prescription & Pharmacy Dispensation Flow

```mermaid
sequenceDiagram
    autonumber
    actor Doctor
    participant FlaskAPI as Flask API Gateway
    actor Pharmacist
    actor Patient

    Doctor->>FlaskAPI: Authors e-Prescription (Meds, Dosage, Frequency, Duration)
    FlaskAPI->>FlaskAPI: Digitally signs with cryptographic stamp (SHA-256)
    FlaskAPI-->>Pharmacist: Queues script in Dispensary Queue (/api/prescriptions)
    Pharmacist->>Pharmacist: Verifies drug-drug interactions & allergy check
    Pharmacist->>FlaskAPI: Fills & marks Dispensed
    FlaskAPI->>FlaskAPI: Automatically decrements pharmacy stock inventory
    FlaskAPI-->>Patient: Updates Patient Medication Schedule & Dosage Alarms
```
