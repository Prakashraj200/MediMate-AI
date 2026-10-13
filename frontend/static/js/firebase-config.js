// Firebase App
import { initializeApp } from "https://www.gstatic.com/firebasejs/12.19.0/firebase-app.js";

// Firebase Authentication
import { getAuth } from "https://www.gstatic.com/firebasejs/12.19.0/firebase-auth.js";

// Firebase Analytics
import { getAnalytics } from "https://www.gstatic.com/firebasejs/12.19.0/firebase-analytics.js";


// ===============================
// FIREBASE CONFIGURATION
// ===============================

const firebaseConfig = {
    apiKey: "AIzaSyBpOQiLcTB8vVeRgffRVO9YKtIkX9ouwvs",
    authDomain: "medimate-ai-2c35e.firebaseapp.com",
    projectId: "medimate-ai-2c35e",
    storageBucket: "medimate-ai-2c35e.firebasestorage.app",
    messagingSenderId: "19561334325",
    appId: "1:19561334325:web:0e2e50533f0e2a2889537c",
    measurementId: "G-LLLP6KW2QH"
};


// ===============================
// INITIALIZE FIREBASE
// ===============================

const app = initializeApp(firebaseConfig);


// ===============================
// INITIALIZE AUTHENTICATION
// ===============================

const auth = getAuth(app);


// ===============================
// INITIALIZE ANALYTICS
// ===============================

const analytics = getAnalytics(app);


// ===============================
// EXPORT
// ===============================

export {
    app,
    auth,
    analytics
};