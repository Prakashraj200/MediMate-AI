# MediMate-AI: System Architecture

## 1. Architectural Overview
MediMate-AI follows a modular, decoupled 4-tier healthcare architecture designed for high availability, security, and low latency.

```mermaid
graph TD
    subgraph ClientLayer["Client Layer (Web Portals)"]
        P[Patient Portal]
        D[Doctor Portal]
        L[Laboratory Portal]
        PH[Pharmacy Portal]
        A[Admin Portal]
    end

    subgraph APILayer["API Gateway & Presentation (Flask :5000)"]
        APP[Flask Core Server app.py]
        BP1[Auth Blueprint]
        BP2[Clinical Blueprints]
        BP3[Operational Blueprints]
        BP4[AI Chat Blueprint]
    end

    subgraph ServiceLayer["Service & Business Logic Layer"]
        AUTH_S[Auth Service]
        CLIN_S[Doctor, Patient, Records Services]
        DIAG_S[Lab & Pharmacy Services]
        AI_S[Preethi AI & ML Triage Service]
    end

    subgraph DataLayer["Persistence & Cloud Infrastructure"]
        FB_AUTH[Firebase Auth]
        FIRESTORE[Cloud Firestore]
        MODELS[ML Model Artifacts]
        LOCAL[Local Fallback Cache]
    end

    ClientLayer --> APP
    APP --> BP1 & BP2 & BP3 & BP4
    BP1 --> AUTH_S
    BP2 --> CLIN_S
    BP3 --> DIAG_S
    BP4 --> AI_S

    AUTH_S --> FB_AUTH & FIRESTORE
    CLIN_S --> FIRESTORE & LOCAL
    DIAG_S --> FIRESTORE & LOCAL
    AI_S --> MODELS
```

---

## 2. Layer Specifications

### 2.1 Client Layer
- Pure **Vanilla HTML/CSS/JS** architecture eliminating bloated single-page framework dependencies.
- Unified Emerald Healthcare design system tokens (`var(--primary)`, `var(--bg-main)`).
- Role-specific security checkpoints validating authenticated session state before rendering sensitive health telemetry.

### 2.2 Routing & Presentation Layer (Flask)
- Organized into **15 isolated Blueprints** under `backend/routes/`:
  - `auth.py`: Registration and Firebase ID token resolution.
  - `admin.py`: User lifecycle and hospital metrics.
  - `doctor.py`, `patient.py`, `appointment.py`, `department.py`: Clinical coordination.
  - `laboratory.py`, `pharmacy.py`, `medicine.py`, `prescription.py`: Diagnostic and pharmaceutical operations.
  - `vitals.py`, `health_records.py`, `report.py`, `notification.py`, `ai_chat.py`: Telemetry, records, and AI assistance.

### 2.3 Service Layer
- Independent domain services located under `backend/services/` encapsulating validation, transaction logic, and Firebase Admin SDK bindings.

### 2.4 Data & AI Layer
- Real-time NoSQL collections in **Google Cloud Firestore**.
- Supervised clinical classification models (`RandomForestClassifier`) deployed for real-time risk triage.
