/**
 * MediMate-AI - Health Records Aggregator (health-records.js)
 */

const HealthRecordsManager = {
  getEhrSummary(mrn) {
    return {
      mrn: mrn || 'MRN-1001',
      patientName: 'John Doe',
      bloodGroup: 'O+',
      allergies: ['Penicillin'],
      chronicDiseases: ['Essential Hypertension Stage 2'],
      lastVisitDate: '2026-10-10'
    };
  }
};

window.HealthRecordsManager = HealthRecordsManager;
