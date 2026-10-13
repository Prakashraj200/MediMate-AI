/**
 * MediMate-AI - Medicines Catalog Helpers (medicines.js)
 */

const MedicinesRegistry = {
  search(keyword) {
    const term = (keyword || '').toLowerCase();
    const all = [
      { code: 'MED-701', name: 'Amoxicillin 500mg', category: 'Antibiotics', price: 14.50 },
      { code: 'MED-702', name: 'Paracetamol 650mg', category: 'Analgesics', price: 4.20 },
      { code: 'MED-703', name: 'Atorvastatin 20mg', category: 'Cardiovascular', price: 28.00 },
      { code: 'MED-704', name: 'Metformin 500mg', category: 'Antidiabetic', price: 9.80 }
    ];
    return all.filter(m => m.name.toLowerCase().includes(term) || m.code.toLowerCase().includes(term));
  }
};

window.MedicinesRegistry = MedicinesRegistry;
