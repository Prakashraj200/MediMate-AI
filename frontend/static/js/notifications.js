/**
 * MediMate-AI - Universal Notification & Toast System (notifications.js)
 */

function showToast(message, type = 'info') {
  let container = document.querySelector('.medimate-toast-container');
  if (!container) {
    container = document.createElement('div');
    container.className = 'medimate-toast-container';
    document.body.appendChild(container);
  }

  const toast = document.createElement('div');
  toast.className = `medimate-toast ${type}`;
  const icon = type === 'success' ? 'fa-circle-check' : (type === 'error' ? 'fa-triangle-exclamation' : 'fa-bell');
  toast.innerHTML = `<i class="fa-solid ${icon}"></i> <span>${message}</span>`;

  container.appendChild(toast);
  setTimeout(() => {
    toast.style.opacity = '0';
    setTimeout(() => toast.remove(), 300);
  }, 3500);
}

window.showToast = showToast;
