/**
 * MediMate-AI - Universal Login Controller (login.js)
 * Supports 3 Primary Portals: Patient, Physiotherapist, Clinic Admin
 * Ensures persistent, robust multi-layer storage across localStorage & sessionStorage
 */

async function handleUnifiedLogin(email, password, role) {
  let authenticatedUser = null;
  const normalizedEmail = (email || '').trim().toLowerCase();
  const normalizedRole = (role || 'patient').trim().toLowerCase();

  // 1. Check local medimateUsers first for instant offline responsiveness
  try {
    const users = JSON.parse(localStorage.getItem('medimateUsers') || '[]');
    const match = users.find(u => 
      u.email && u.email.toLowerCase() === normalizedEmail && 
      u.password === password &&
      (!role || u.role.toLowerCase() === normalizedRole || u.role === 'admin')
    );
    if (match) {
      authenticatedUser = match;
    }
  } catch (e) {}

  // 2. Fallback to Firebase Client Auth if initialized
  if (!authenticatedUser && typeof firebase !== 'undefined' && firebase.auth) {
    try {
      const fbCred = await firebase.auth().signInWithEmailAndPassword(normalizedEmail, password);
      if (fbCred.user) {
        authenticatedUser = {
          email: fbCred.user.email,
          fullName: fbCred.user.displayName || normalizedEmail.split('@')[0],
          role: normalizedRole,
          uid: fbCred.user.uid
        };
      }
    } catch (fbErr) {
      console.warn('Firebase login notice:', fbErr.message);
    }
  }

  // 3. Built-in Demo Credentials for the 3 Core Roles
  if (!authenticatedUser) {
    if (normalizedEmail === 'admin@medimate.ai' && password === 'admin123') {
      authenticatedUser = {
        email: 'admin@medimate.ai',
        fullName: 'Chief Rehabilitation Administrator',
        name: 'Chief Rehabilitation Administrator',
        role: 'admin',
        id: 'ADM-001'
      };
    } else if ((normalizedEmail === 'physio@medimate.ai' || normalizedEmail === 'doctor@medimate.ai') && (password === 'physio123' || password === 'doctor123')) {
      authenticatedUser = {
        email: 'physio@medimate.ai',
        fullName: 'Dr. Anand Kumar (Senior PT)',
        name: 'Dr. Anand Kumar',
        role: 'doctor',
        specialization: 'Whiplash & Cervical Spine Specialist',
        id: 'PHY-001'
      };
    } else if (normalizedEmail === 'patient@medimate.ai' && password === 'patient123') {
      authenticatedUser = {
        email: 'patient@medimate.ai',
        fullName: 'Karthik Subramanian',
        name: 'Karthik Subramanian',
        age: 32,
        injury: 'Two-Wheeler Collision • Cervical Whiplash & Lumbar Contusion',
        role: 'patient',
        id: 'PAT-101'
      };
    }
  }

  if (authenticatedUser) {
    const userRole = authenticatedUser.role || normalizedRole;

    // Set universal current user
    localStorage.setItem('currentUser', JSON.stringify(authenticatedUser));
    sessionStorage.setItem('currentUser', JSON.stringify(authenticatedUser));
    localStorage.setItem('userRole', userRole);
    sessionStorage.setItem('userRole', userRole);

    // Role-specific persistence to ensure zero-friction entry without redirect loops
    if (userRole === 'admin') {
      localStorage.setItem('adminLoggedIn', 'true');
      sessionStorage.setItem('adminLoggedIn', 'true');
      localStorage.setItem('adminUser', JSON.stringify(authenticatedUser));
      sessionStorage.setItem('adminUser', JSON.stringify(authenticatedUser));
      localStorage.setItem('medimateAdminProfile', JSON.stringify(authenticatedUser));
    } else if (userRole === 'doctor' || userRole === 'physio') {
      localStorage.setItem('doctorLoggedIn', 'true');
      sessionStorage.setItem('doctorLoggedIn', 'true');
      localStorage.setItem('doctorUser', JSON.stringify(authenticatedUser));
      sessionStorage.setItem('doctorUser', JSON.stringify(authenticatedUser));
    } else if (userRole === 'patient') {
      localStorage.setItem('patientLoggedIn', 'true');
      sessionStorage.setItem('patientLoggedIn', 'true');
      localStorage.setItem('patientUser', JSON.stringify(authenticatedUser));
      sessionStorage.setItem('patientUser', JSON.stringify(authenticatedUser));
      localStorage.setItem('patient_profile', JSON.stringify(authenticatedUser));
    }

    if (window.AuthManager) {
      try { window.AuthManager.setCurrentUser(authenticatedUser); } catch(e){}
    }

    return { success: true, user: authenticatedUser };
  }

  return { success: false, message: 'Invalid credentials. Please click a 1-click Demo Fill chip or enter valid email.' };
}

window.handleUnifiedLogin = handleUnifiedLogin;
