/**
 * MediMate-AI - Central API Client (api.js)
 * Connects frontend views to Flask backend endpoints on port 5000 with offline resilience.
 */

const ApiClient = {
  baseUrl: window.location.origin,

  async request(endpoint, options = {}) {
    const defaultHeaders = {
      'Content-Type': 'application/json',
      'Accept': 'application/json'
    };

    const token = localStorage.getItem('medimateToken');
    if (token) {
      defaultHeaders['Authorization'] = `Bearer ${token}`;
    }

    const config = {
      ...options,
      headers: {
        ...defaultHeaders,
        ...(options.headers || {})
      }
    };

    try {
      const response = await fetch(`${this.baseUrl}${endpoint}`, config);
      const data = await response.json();
      return data;
    } catch (err) {
      console.warn(`[ApiClient] Network request to ${endpoint} failed:`, err.message);
      return {
        success: false,
        error: 'Network request could not reach backend server.',
        offline: true
      };
    }
  },

  // Auth Endpoints
  async register(userData) {
    return this.request('/api/auth/register', {
      method: 'POST',
      body: JSON.stringify(userData)
    });
  },

  async login(credentials) {
    return this.request('/api/auth/login', {
      method: 'POST',
      body: JSON.stringify(credentials)
    });
  },

  // Appointments
  async getAppointments() {
    return this.request('/api/appointments/');
  },

  async createAppointment(apptData) {
    return this.request('/api/appointments/', {
      method: 'POST',
      body: JSON.stringify(apptData)
    });
  },

  // Medicines
  async getMedicines() {
    return this.request('/api/medicines/');
  },

  // Prescriptions
  async getPrescriptions() {
    return this.request('/api/prescriptions/');
  },

  // Vitals
  async getVitals() {
    return this.request('/api/vitals/');
  },

  async logVitals(vitalData) {
    return this.request('/api/vitals/', {
      method: 'POST',
      body: JSON.stringify(vitalData)
    });
  },

  // AI Chat (Preethi AI)
  async sendAiMessage(message, history = []) {
    return this.request('/api/ai/chat', {
      method: 'POST',
      body: JSON.stringify({ message, history })
    });
  }
};

window.ApiClient = ApiClient;
