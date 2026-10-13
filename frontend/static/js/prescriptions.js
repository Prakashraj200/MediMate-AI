/**
 * MediMate-AI - Prescriptions Module (prescriptions.js)
 */

const PrescriptionFormatter = {
  formatDosage(frequencyCode) {
    const map = {
      '1-0-1': 'Twice Daily (Morning & Night, after meals)',
      '1-1-1': 'Three times daily (Morning, Noon & Night)',
      '1-0-0': 'Once Daily (Morning after breakfast)',
      '0-0-1': 'Once Daily (At Bedtime)',
      'SOS': 'As needed for emergency symptoms'
    };
    return map[frequencyCode] || frequencyCode;
  }
};

window.PrescriptionFormatter = PrescriptionFormatter;
