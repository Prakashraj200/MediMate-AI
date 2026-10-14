// Firebase App
import { initializeApp } from "https://www.gstatic.com/firebasejs/12.19.0/firebase-app.js";

// Firebase Authentication
import { getAuth } from "https://www.gstatic.com/firebasejs/12.19.0/firebase-auth.js";

// Firebase Analytics
import { getAnalytics } from "https://www.gstatic.com/firebasejs/12.19.0/firebase-analytics.js";


// Firebase Firestore
import { getFirestore } from "https://www.gstatic.com/firebasejs/12.19.0/firebase-firestore.js";


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
// INITIALIZE FIRESTORE
// ===============================

let db = null;
try {
    db = getFirestore(app);
} catch (e) {
    console.warn("Firestore initialization error:", e);
}


// ===============================
// INITIALIZE ANALYTICS
// ===============================

let analytics = null;
try {
    analytics = getAnalytics(app);
} catch (e) {
    console.warn("Analytics initialization skipped:", e);
}


// ===============================
// EXPORT
// ===============================

export {
    app,
    auth,
    analytics,
    db
};