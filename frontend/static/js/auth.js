/**
 * MediMate-AI - Authentication & Session Manager (auth.js)
 */

const AuthManager = {
  getCurrentUser() {
    try {
      const userStr = localStorage.getItem('currentUser') || localStorage.getItem('medimateActiveUser');
      return userStr ? JSON.parse(userStr) : null;
    } catch (e) {
      return null;
    }
  },

  setCurrentUser(user) {
    localStorage.setItem('currentUser', JSON.stringify(user));
    localStorage.setItem('medimateActiveUser', JSON.stringify(user));
    if (user.role) {
      localStorage.setItem('userRole', user.role);
    }
  },

  isAuthenticated() {
    return !!this.getCurrentUser();
  },

  requireRole(expectedRole) {
    const user = this.getCurrentUser();
    if (!user) {
      window.location.href = `/${expectedRole}/${expectedRole}-login.html`;
      return false;
    }
    if (user.role && user.role.toLowerCase() !== expectedRole.toLowerCase() && user.role.toLowerCase() !== 'admin') {
      alert(`Access Restricted: This view requires ${expectedRole.toUpperCase()} credentials.`);
      window.location.href = `/${user.role}/${user.role}-login.html`;
      return false;
    }
    return true;
  },

  logout(redirectUrl = '/index.html') {
    localStorage.removeItem('currentUser');
    localStorage.removeItem('medimateActiveUser');
    localStorage.removeItem('medimateToken');
    localStorage.removeItem('userRole');
    localStorage.removeItem('doctorLoggedIn');
    localStorage.removeItem('adminLoggedIn');
    localStorage.removeItem('patientLoggedIn');
    localStorage.removeItem('pharmacyLoggedIn');
    localStorage.removeItem('labLoggedIn');
    localStorage.removeItem('firebaseIdToken');
    sessionStorage.clear();

    if (typeof firebase !== 'undefined' && firebase.auth) {
      try { firebase.auth().signOut(); } catch (e) {}
    }

    window.location.href = redirectUrl;
  }
};

window.AuthManager = AuthManager;
