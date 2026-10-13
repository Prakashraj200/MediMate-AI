/**
 * MediMate-AI - Universal Login Controller (login.js)
 */

async function handleUnifiedLogin(email, password, role) {
  let authenticatedUser = null;

  // 1. Check local medimateUsers first for instant offline responsiveness
  try {
    const users = JSON.parse(localStorage.getItem('medimateUsers') || '[]');
    const match = users.find(u => 
      u.email.toLowerCase() === email.toLowerCase() && 
      u.password === password &&
      (!role || u.role.toLowerCase() === role.toLowerCase() || u.role === 'admin')
    );
    if (match) {
      authenticatedUser = match;
    }
  } catch (e) {}

  // 2. Fallback to Firebase Client Auth if initialized
  if (!authenticatedUser && typeof firebase !== 'undefined' && firebase.auth) {
    try {
      const fbCred = await firebase.auth().signInWithEmailAndPassword(email, password);
      if (fbCred.user) {
        authenticatedUser = {
          email: fbCred.user.email,
          fullName: fbCred.user.displayName || email.split('@')[0],
          role: role || 'patient',
          uid: fbCred.user.uid
        };
      }
    } catch (fbErr) {
      console.warn('Firebase login notice:', fbErr.message);
    }
  }

  // 3. Fallback demo admin credentials
  if (!authenticatedUser && email === 'admin@medimate.ai' && password === 'admin123') {
    authenticatedUser = {
      email: 'admin@medimate.ai',
      fullName: 'System Administrator',
      role: 'admin',
      id: 'ADM-001'
    };
  }

  if (authenticatedUser) {
    if (window.AuthManager) {
      window.AuthManager.setCurrentUser(authenticatedUser);
    } else {
      localStorage.setItem('currentUser', JSON.stringify(authenticatedUser));
      localStorage.setItem('userRole', authenticatedUser.role);
    }
    return { success: true, user: authenticatedUser };
  }

  return { success: false, message: 'Invalid email credentials or portal role mismatch.' };
}

window.handleUnifiedLogin = handleUnifiedLogin;
