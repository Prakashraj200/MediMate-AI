/**
 * MediMate-AI - Patient Module Controller (patient.js)
 */

const PatientController = {
  getProfile() {
    const user = window.AuthManager ? window.AuthManager.getCurrentUser() : null;
    return user || {
      fullName: 'John Doe',
      email: 'patient@medimate.ai',
      mrn: 'MRN-1001',
      bloodGroup: 'O+ Positive',
      allergies: ['Penicillin']
    };
  },

  scheduleAppointment(doctor, date, time, reason) {
    const appts = JSON.parse(localStorage.getItem('patientAppointments') || '[]');
    const newAppt = {
      id: `APT-${Math.floor(100 + Math.random() * 900)}`,
      doctor,
      date,
      time,
      reason,
      status: 'Confirmed'
    };
    appts.unshift(newAppt);
    localStorage.setItem('patientAppointments', JSON.stringify(appts));
    return newAppt;
  }
};

window.PatientController = PatientController;
