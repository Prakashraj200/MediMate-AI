/**
 * MediMate-AI - Doctor Module Helpers (doctor.js)
 */

const DoctorController = {
  getConsultationQueue() {
    return [
      { id: 'APT-101', patient: 'Meera Sharma', mrn: 'MRN-8429', time: '09:30 AM', mode: 'Telehealth', status: 'Confirmed' },
      { id: 'APT-102', patient: 'Robert Chen', mrn: 'MRN-3312', time: '10:15 AM', mode: 'In-Clinic', status: 'Checked In' },
      { id: 'APT-103', patient: 'Amelia Rodriguez', mrn: 'MRN-9104', time: '11:00 AM', mode: 'In-Clinic', status: 'Waiting' }
    ];
  },

  signPrescription(patientName, meds, diagnosis) {
    const prescriptions = JSON.parse(localStorage.getItem('issuedPrescriptions') || '[]');
    const rx = {
      id: `RX-${Math.floor(1000 + Math.random() * 9000)}`,
      patientName,
      diagnosis,
      medications: meds,
      date: new Date().toISOString().split('T')[0],
      signature: 'DIGITALLY-SIGNED-MD'
    };
    prescriptions.unshift(rx);
    localStorage.setItem('issuedPrescriptions', JSON.stringify(prescriptions));
    return rx;
  }
};

window.DoctorController = DoctorController;
