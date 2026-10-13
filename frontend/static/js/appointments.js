/**
 * MediMate-AI - Appointments Module Controller (appointments.js)
 */

const AppointmentsManager = {
  filterAppointments(list, filterCriteria = {}) {
    return list.filter(item => {
      if (filterCriteria.status && item.status !== filterCriteria.status) return false;
      if (filterCriteria.doctor && item.doctor !== filterCriteria.doctor) return false;
      if (filterCriteria.patient && item.patient !== filterCriteria.patient) return false;
      return true;
    });
  },

  formatAppointmentTime(timeStr) {
    return timeStr || 'Scheduled Consultation';
  }
};

window.AppointmentsManager = AppointmentsManager;
