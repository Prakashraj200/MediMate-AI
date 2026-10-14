/**
 * MediMate-AI - Laboratory Module Controller (laboratory.js)
 */

const LabController = {
  getTestRequests() {
    return [
      { accession: 'BAR-9012', patient: 'John Doe', test: 'Lipid Profile Panel', status: 'Pending Collection' },
      { accession: 'BAR-9013', patient: 'David Kim', test: 'Complete Blood Count', status: 'Sample Collected' },
      { accession: 'BAR-9014', patient: 'Meera Sharma', test: 'Thyroid Profile', status: 'In Processing' }
    ];
  },

  validateRange(value, min, max) {
    const num = parseFloat(value);
    if (isNaN(num)) return 'normal';
    if (num < min) return 'low';
    if (num > max) return 'high';
    return 'normal';
  }
};

window.LabController = LabController;
