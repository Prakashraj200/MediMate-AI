/**
 * MediMate-AI - Pharmacy Module Controller (pharmacy.js)
 */

const PharmacyController = {
  getInventory() {
    return [
      { code: 'PH-701', name: 'Amoxicillin 500mg', qty: 320, reorder: 50, price: 14.50 },
      { code: 'PH-702', name: 'Paracetamol 650mg', qty: 850, reorder: 100, price: 4.20 },
      { code: 'PH-705', name: 'Azithromycin 250mg', qty: 18, reorder: 50, price: 22.00 }
    ];
  },

  dispensePrescription(rxId, patientName) {
    console.log(`[PharmacyController] Dispensing ${rxId} for ${patientName}`);
    return { success: true, timestamp: new Date().toISOString() };
  }
};

window.PharmacyController = PharmacyController;
