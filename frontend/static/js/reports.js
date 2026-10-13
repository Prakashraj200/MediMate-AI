/**
 * MediMate-AI - Reports & Analytics Helpers (reports.js)
 */

const ReportsHelper = {
  exportToCsv(filename, headers, rows) {
    let csv = headers.join(',') + '\n';
    rows.forEach(r => {
      csv += r.map(field => `"${field}"`).join(',') + '\n';
    });
    const blob = new Blob([csv], { type: 'text/csv' });
    const a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = filename;
    a.click();
  }
};

window.ReportsHelper = ReportsHelper;
