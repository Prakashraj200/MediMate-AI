# MediMate-AI: Security & Compliance Architecture

## 1. Compliance Standard
MediMate-AI is architected with strict compliance guidelines adhering to **HIPAA** (Health Insurance Portability and Accountability Act) and **GDPR** healthcare privacy principles.

---

## 2. Role-Based Access Control (RBAC) Matrix

| Resource / Action | Patient | Doctor | Laboratory | Pharmacy | Administrator |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **View Own Medical Records** | ✅ | ❌ | ❌ | ❌ | ❌ |
| **View Assigned Patients' EHR** | ❌ | ✅ | ❌ | ❌ | ❌ |
| **Author / Sign Prescriptions** | ❌ | ✅ | ❌ | ❌ | ❌ |
| **Dispense Medications** | ❌ | ❌ | ❌ | ✅ | ❌ |
| **Input Analyte Lab Results** | ❌ | ❌ | ✅ | ❌ | ❌ |
| **Manage Staff & System Roles** | ❌ | ❌ | ❌ | ❌ | ✅ |
| **Emergency Broadcast Alerts** | ❌ | ❌ | ❌ | ❌ | ✅ |

---

## 3. Data Protection Principles

### 3.1 Encryption
- **In Transit**: All network requests enforced over **TLS 1.3** / HTTPS.
- **At Rest**: Protected using **AES-256** encryption in Google Cloud Firestore and persistent disk volumes.

### 3.2 Authentication & Token Lifecycles
- Multi-factor authentication support via Firebase Auth.
- JSON Web Tokens (JWT) with cryptographic RS256 signature verification.
- Enforced session expiration and idle timeout revocation.

### 3.3 e-Prescription Cryptographic Tamper-Proofing
- Every electronic prescription signed by a licensed physician generates an immutable digital signature digest.
- Prescriptions cannot be modified once queued in pharmacy dispensaries.

### 3.4 Audit Trail Logging
- Critical operations (e.g. prescription issuance, laboratory result publishing, user privilege escalation) log immutable timestamps, user identifiers, and IP traces into the administrative audit ledger.
