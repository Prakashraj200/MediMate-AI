import { initializeApp } from "https://www.gstatic.com/firebasejs/12.19.0/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/12.19.0/firebase-analytics.js";

const firebaseConfig = {
    apiKey: "YOUR_API_KEY",
    authDomain: "medimate-ai-2c35e.firebaseapp.com",
    projectId: "medimate-ai-2c35e",
    storageBucket: "medimate-ai-2c35e.firebasestorage.app",
    messagingSenderId: "19561334325",
    appId: "1:19561334325:web:0e2e50533f0e2a2889537c",
    measurementId: "G-LLLP6KW2QH"
};

const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

export { app };