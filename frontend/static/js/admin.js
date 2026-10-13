/**
 * MediMate-AI - Admin Module Helpers (admin.js)
 */

const AdminController = {
  fetchDashboardMetrics() {
    return {
      doctorsCount: 42,
      patientsCount: 1420,
      activeAppointments: 85,
      pharmacyFormularyCount: 264,
      laboratoryOrdersToday: 48,
      occupancyRate: '88%'
    };
  },

  broadcastNotification(title, message, targetRole = 'all') {
    const notifications = JSON.parse(localStorage.getItem('systemBroadcasts') || '[]');
    const newAlert = {
      id: `BRD-${Date.now()}`,
      title,
      message,
      targetRole,
      timestamp: new Date().toISOString()
    };
    notifications.unshift(newAlert);
    localStorage.setItem('systemBroadcasts', JSON.stringify(notifications));
    return newAlert;
  }
};

window.AdminController = AdminController;
