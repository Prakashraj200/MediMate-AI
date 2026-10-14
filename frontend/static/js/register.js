/**
 * MediMate-AI - Universal Registration Controller (register.js)
 */

document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('registerForm');
  if (!form) return;

  form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const fullName = document.getElementById('name') ? document.getElementById('name').value.trim() : '';
    const email = document.getElementById('email') ? document.getElementById('email').value.trim() : '';
    const password = document.getElementById('password') ? document.getElementById('password').value : '';
    const role = (window.selectedRole || 'patient').toLowerCase();

    if (!email || !password) {
      alert('Please fill in all mandatory registration fields.');
      return;
    }

    // Save to medimateUsers local registry for dual authentication support
    try {
      const users = JSON.parse(localStorage.getItem('medimateUsers') || '[]');
      const existing = users.find(u => u.email.toLowerCase() === email.toLowerCase());
      if (!existing) {
        users.push({
          fullName,
          name: fullName,
          email,
          password,
          role,
          id: `USR-${Date.now()}`
        });
        localStorage.setItem('medimateUsers', JSON.stringify(users));
      }
    } catch (e) {}

    // Dispatch to Flask backend API
    if (window.ApiClient) {
      await window.ApiClient.register({ email, password, fullName, role });
    }

    alert(`Registration successful! You may now sign in as ${role.toUpperCase()}.`);
    const targetUrl = `/${role}/${role === 'laboratory' ? 'lab' : role}-login.html`;
    window.location.href = targetUrl;
  });
});
