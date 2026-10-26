/**
 * MediMate AI - Patient Portal Common Data & Utility Service
 * Post-Accident Rehabilitation & Physiotherapy Intelligence
 */

import { auth } from "../static/js/firebase-config.js";
import { onAuthStateChanged, signOut } from "https://www.gstatic.com/firebasejs/12.19.0/firebase-auth.js";

// ============================================================================
// DEFAULT SEED DATA (POST-ACCIDENT PHYSIO & REHAB SPECIFIC)
// ============================================================================

const DEFAULT_PATIENT_PROFILE = {
    id: "MM-PAT-2026-9042",
    name: "Prakash Raj",
    email: "patient@medimate.ai",
    phone: "+91 98765 43210",
    dob: "1994-06-15",
    age: 32,
    gender: "Male",
    bloodGroup: "O+",
    height: "174 cm",
    weight: "68 kg",
    bmi: "22.5",
    address: "Flat 402, Green Meadows, Anna Nagar",
    city: "Chennai",
    state: "Tamil Nadu",
    pincode: "600040",
    emergencyContact: {
        name: "Priya Raj",
        relation: "Spouse",
        phone: "+91 98765 43211"
    },
    insurance: {
        provider: "Star Health Comprehensive",
        policyNumber: "SH-992140-2026",
        validTill: "2027-03-31",
        coverageLimit: "₹10,00,000"
    },
    primaryPhysician: "Dr. Anand Kumar (Senior Orthopedic Physio)",
    rehabCategory: "Post-Accident Cervical & Lumbar Rehabilitation",
    traumaDate: "October 2026",
    recoveryPhase: "Active Mobilization & Strengthening",
    allergies: ["Penicillin"],
    chronicConditions: ["Post-Trauma Cervical Strain"],
    joinedDate: "October 2026"
};

const DEFAULT_APPOINTMENTS = [];

const DEFAULT_MEDICINES = []; // Zero pharmacy clutter

const DEFAULT_VITALS = {
    mobilityScore: {
        value: 78,
        unit: "% ROM",
        status: "Progressing Rapidly",
        lastChecked: "Today, 08:30 AM"
    },
    painScore: {
        value: 3,
        unit: "/ 10",
        status: "Controlled (Mild Strain)",
        lastChecked: "Today, 08:30 AM"
    },
    cervicalFlexion: {
        value: "42° / 50°",
        unit: "Range",
        status: "84% Recovered",
        lastChecked: "Oct 21, 2026"
    },
    lumbarFlexion: {
        value: "65° / 80°",
        unit: "Range",
        status: "81% Recovered",
        lastChecked: "Oct 21, 2026"
    },
    rehabStreak: {
        value: 12,
        unit: "Days",
        status: "Consistent",
        lastChecked: "Active Streak"
    },
    bloodPressure: {
        systolic: 120,
        diastolic: 80,
        unit: "mmHg",
        status: "Normal",
        lastChecked: "Today, 08:30 AM"
    },
    heartRate: {
        value: 72,
        unit: "bpm",
        status: "Optimal",
        lastChecked: "Today, 08:30 AM"
    }
};

const DEFAULT_PRESCRIPTIONS = [];

const DEFAULT_LAB_REPORTS = [
    {
        id: "REHAB-REC-01",
        testName: "Cervical Spine Diagnostic MRI & Disc Scan",
        category: "Diagnostic Scan",
        date: "2026-10-18",
        labTechnician: "Dr. R. Ramanathan, Radiologist",
        status: "Completed",
        flag: "Improving",
        summary: "C5-C6 mild posterior disc bulge without canal stenosis. Neural foramina patent. Clear for active physiotherapy.",
        parameters: [
            { name: "C5-C6 Disc Height", value: "Preserved (4.8mm)", unit: "mm", normalRange: "4.5 - 5.5mm", status: "Optimal" },
            { name: "Cervical Alignment", value: "Mild lordotic straightening", unit: "Deg", normalRange: "Normal Lordosis", status: "Mild Strain" },
            { name: "Thecal Sac Impingement", value: "None", unit: "-", normalRange: "None", status: "Clear" },
            { name: "Paravertebral Muscle Tone", value: "Mild spasm", unit: "-", normalRange: "Normal Tone", status: "Improving with TENS" }
        ]
    },
    {
        id: "REHAB-REC-02",
        testName: "Post-Trauma Range of Motion (ROM) Kinematics Report",
        category: "Kinematics Analysis",
        date: "2026-10-20",
        labTechnician: "Dr. Anand Kumar, Lead Physio",
        status: "Completed",
        flag: "Normal",
        summary: "78% baseline mobility restored in cervical rotation and lumbar lateral bending. No neuro-deficit noted.",
        parameters: [
            { name: "Cervical Flexion", value: 42, unit: "degrees", normalRange: "45 - 50", status: "Near Normal" },
            { name: "Cervical Extension", value: 48, unit: "degrees", normalRange: "50 - 60", status: "Near Normal" },
            { name: "Right Lateral Rotation", value: 65, unit: "degrees", normalRange: "70 - 80", status: "Mild Deficit" },
            { name: "Left Lateral Rotation", value: 68, unit: "degrees", normalRange: "70 - 80", status: "Near Normal" }
        ]
    },
    {
        id: "REHAB-REC-03",
        testName: "Lumbar Dynamic Recovery & Axial Load Evaluation",
        category: "Rehab Assessment",
        date: "2026-10-21",
        labTechnician: "Dr. Sneha Rao, Senior Physio",
        status: "Completed",
        flag: "Normal",
        summary: "Lumbar core endurance test passed. Patient cleared for progressive resistance bands and low-impact gait retraining.",
        parameters: [
            { name: "Core Endurance Hold", value: 45, unit: "seconds", normalRange: "> 40", status: "Normal" },
            { name: "Straight Leg Raise (SLR) Right", value: 80, unit: "degrees", normalRange: "70 - 90", status: "Negative / Normal" },
            { name: "Straight Leg Raise (SLR) Left", value: 82, unit: "degrees", normalRange: "70 - 90", status: "Negative / Normal" }
        ]
    }
];

const DEFAULT_DOCTORS = [
    {
        id: "DOC-PHY-01",
        name: "Dr. Anand Kumar",
        department: "Orthopedic Rehabilitation",
        qualifications: "BPT, MPT (Orthopedics), MIAP",
        experience: "12+ Years Experience",
        rating: 4.9,
        reviewsCount: 38,
        fee: "₹650",
        avatar: "AK",
        availableDays: "Mon - Sat",
        nextSlot: "Today, 11:30 AM",
        bio: "Senior Physiotherapist specializing in post-accident musculoskeletal trauma, cervical spinal alignment, and joint mobility restoration.",
        email: "anand.physio@medimate.ai",
        phone: "+91 98401 23456"
    },
    {
        id: "DOC-PHY-02",
        name: "Dr. Sneha Rao",
        department: "Neurological Rehabilitation",
        qualifications: "MPT (Neurology), Fellowship in Neuro-Rehab",
        experience: "9+ Years Experience",
        rating: 4.9,
        reviewsCount: 29,
        fee: "₹700",
        avatar: "SR",
        availableDays: "Mon - Fri",
        nextSlot: "Tomorrow, 10:00 AM",
        bio: "Consultant Neuro-Physiotherapist expert in traumatic nerve injury rehabilitation, proprioceptive retraining, and motor balance recovery.",
        email: "sneha.physio@medimate.ai",
        phone: "+91 98402 34567"
    },
    {
        id: "DOC-PHY-03",
        name: "Dr. Ramesh Kumar",
        department: "Post-Accident Trauma & Sports Physio",
        qualifications: "BPT, MPT (Sports Rehabilitation), CSCS",
        experience: "8+ Years Experience",
        rating: 4.8,
        reviewsCount: 24,
        fee: "₹600",
        avatar: "RK",
        availableDays: "Tue - Sun",
        nextSlot: "Today, 03:00 PM",
        bio: "Trauma recovery specialist focusing on soft-tissue injury remodeling, spinal decompression therapies, and progressive resistance retraining.",
        email: "ramesh.physio@medimate.ai",
        phone: "+91 98403 45678"
    }
];

const DEFAULT_NOTIFICATIONS = [
    {
        id: "NOTIF-01",
        category: "rehab",
        title: "Daily Rehab Plan Ready",
        message: "Your customized post-accident cervical stretching and isometric protocol for today is ready in the Pain & Rehab Tracker.",
        time: "1 hour ago",
        read: false,
        icon: "fa-solid fa-person-walking",
        link: "rehab.html"
    },
    {
        id: "NOTIF-02",
        category: "ai",
        title: "Preethi AI Milestone Update",
        message: "Preethi AI noticed your mobility score improved from 72% to 78% this week. Keep up the consistent routines!",
        time: "3 hours ago",
        read: false,
        icon: "fa-solid fa-robot",
        link: "preethi-ai.html"
    },
    {
        id: "NOTIF-03",
        category: "consultation",
        title: "Tele-Rehab Consultation Available",
        message: "Licensed physiotherapists are online. Tap Tele-Rehab Consultation to join a high-definition video check-in.",
        time: "1 day ago",
        read: true,
        icon: "fa-solid fa-video",
        link: "/tele-rehab.html"
    }
];

// ============================================================================
// DATA STORE REPOSITORY
// ============================================================================

export class PatientStore {
    static purgeDummyData() {
        const dummyNames = [
            "sarah jenkins",
            "rajesh kumar",
            "anita patel",
            "vikram malhotra",
            "meenakshi sundaram",
            "karthik raman",
            "sarah connor",
            "john smith",
            "sujipreethi",
            "suji"
        ];
        
        // 1. Purge patient_appointments
        try {
            const rawApts = JSON.parse(localStorage.getItem("patient_appointments") || "[]");
            if (Array.isArray(rawApts)) {
                const cleanedApts = rawApts.filter(apt => {
                    if (!apt || !apt.doctorName) return false;
                    const doc = apt.doctorName.toLowerCase();
                    return !dummyNames.some(d => doc.includes(d));
                });
                localStorage.setItem("patient_appointments", JSON.stringify(cleanedApts));
            }
        } catch (e) {
            localStorage.setItem("patient_appointments", JSON.stringify([]));
        }

        // 2. Purge patient_doctors
        try {
            const rawDocs = JSON.parse(localStorage.getItem("patient_doctors") || "[]");
            if (Array.isArray(rawDocs)) {
                const cleanedDocs = rawDocs.filter(doc => {
                    if (!doc || !doc.name) return false;
                    const docName = doc.name.toLowerCase();
                    return !dummyNames.some(d => docName.includes(d));
                });
                localStorage.setItem("patient_doctors", JSON.stringify(cleanedDocs));
            }
        } catch (e) {
            localStorage.setItem("patient_doctors", JSON.stringify([]));
        }

        // 3. Purge patient_prescriptions (zero pharmacy clutter)
        localStorage.setItem("patient_prescriptions", JSON.stringify([]));

        // 4. Purge patient_medicines (zero pharmacy clutter)
        localStorage.setItem("patient_medicines", JSON.stringify([]));

        // 5. Purge patient_lab_reports of generic cardiac/lipid tests
        try {
            const rawLabs = JSON.parse(localStorage.getItem("patient_lab_reports") || "[]");
            const dummyLabs = ["lipid profile", "complete blood count", "glycated hemoglobin", "hba1c", "thyroid", "cbc"];
            const cleanedLabs = Array.isArray(rawLabs) ? rawLabs.filter(l => !dummyLabs.some(dl => (l.testName || "").toLowerCase().includes(dl))) : [];
            if (cleanedLabs.length === 0) {
                localStorage.setItem("patient_lab_reports", JSON.stringify(DEFAULT_LAB_REPORTS));
            } else {
                localStorage.setItem("patient_lab_reports", JSON.stringify(cleanedLabs));
            }
        } catch (e) {
            localStorage.setItem("patient_lab_reports", JSON.stringify(DEFAULT_LAB_REPORTS));
        }
    }

    static init() {
        this.purgeDummyData();
        if (!localStorage.getItem("patient_profile")) {
            localStorage.setItem("patient_profile", JSON.stringify(DEFAULT_PATIENT_PROFILE));
        }
        if (!localStorage.getItem("patient_appointments")) {
            localStorage.setItem("patient_appointments", JSON.stringify([]));
        }
        localStorage.setItem("patient_medicines", JSON.stringify([]));
        if (!localStorage.getItem("patient_vitals")) {
            localStorage.setItem("patient_vitals", JSON.stringify(DEFAULT_VITALS));
        }
        localStorage.setItem("patient_prescriptions", JSON.stringify([]));
        if (!localStorage.getItem("patient_lab_reports")) {
            localStorage.setItem("patient_lab_reports", JSON.stringify(DEFAULT_LAB_REPORTS));
        }
        if (!localStorage.getItem("patient_doctors")) {
            localStorage.setItem("patient_doctors", JSON.stringify(DEFAULT_DOCTORS));
        }
        if (!localStorage.getItem("patient_notifications")) {
            localStorage.setItem("patient_notifications", JSON.stringify(DEFAULT_NOTIFICATIONS));
        }
        if (!localStorage.getItem("patient_health_documents")) {
            localStorage.setItem("patient_health_documents", JSON.stringify([]));
        }
    }

    // Profile
    static getProfile() {
        this.init();
        try {
            let prof = JSON.parse(localStorage.getItem("patient_profile")) || {};
            let curUser = null;
            try {
                curUser = JSON.parse(localStorage.getItem("currentUser") || sessionStorage.getItem("currentUser") || "null");
            } catch(e) {}
            if (!curUser) {
                try {
                    const sessionEmail = sessionStorage.getItem("medimateUser");
                    const allUsers = JSON.parse(localStorage.getItem("medimateUsers") || "[]");
                    if (sessionEmail && allUsers.length) {
                        curUser = allUsers.find(u => u.email && u.email.toLowerCase() === sessionEmail.toLowerCase());
                    }
                } catch(e) {}
            }
            if (curUser && (curUser.name || curUser.fullName)) {
                const realName = (curUser.name || curUser.fullName).trim();
                prof.name = realName;
                if (curUser.email) prof.email = curUser.email;
                if (curUser.phone) prof.phone = curUser.phone;
            }
            if (curUser && curUser.photo) {
                prof.photo = curUser.photo;
            }
            return { ...DEFAULT_PATIENT_PROFILE, ...prof };
        } catch {
            return DEFAULT_PATIENT_PROFILE;
        }
    }

    static saveProfile(profile) {
        localStorage.setItem("patient_profile", JSON.stringify(profile));
        const currentUser = JSON.parse(localStorage.getItem("currentUser") || "{}");
        currentUser.name = profile.name;
        currentUser.email = profile.email;
        currentUser.phone = profile.phone;
        if (profile.photo !== undefined) {
            currentUser.photo = profile.photo;
        }
        localStorage.setItem("currentUser", JSON.stringify(currentUser));
    }

    // Appointments
    static getAppointments() {
        this.init();
        this.purgeDummyData();
        try {
            const raw = JSON.parse(localStorage.getItem("patient_appointments")) || [];
            return Array.isArray(raw) ? raw : [];
        } catch {
            return [];
        }
    }

    static addAppointment(apt) {
        this.init();
        const apts = this.getAppointments();
        const newApt = {
            id: "APT-REHAB-" + (1000 + apts.length + 1),
            status: "Confirmed",
            ...apt
        };
        apts.unshift(newApt);
        localStorage.setItem("patient_appointments", JSON.stringify(apts));
        
        this.addNotification({
            category: "consultation",
            title: "Rehab Consultation Confirmed",
            message: `Your session with ${newApt.doctorName} for ${newApt.date} at ${newApt.time} is confirmed.`,
            time: "Just now",
            read: false,
            icon: "fa-solid fa-calendar-check",
            link: "appointments.html"
        });

        return newApt;
    }

    static updateAppointmentStatus(id, newStatus) {
        const apts = this.getAppointments();
        const target = apts.find(a => a.id === id);
        if (target) {
            target.status = newStatus;
            localStorage.setItem("patient_appointments", JSON.stringify(apts));
            return true;
        }
        return false;
    }

    static deleteAppointment(id) {
        this.init();
        try {
            let apts = this.getAppointments();
            apts = apts.filter(a => a.id !== id);
            localStorage.setItem("patient_appointments", JSON.stringify(apts));
            return true;
        } catch (e) {
            return false;
        }
    }

    // Medicines (Empty array maintained for API safety)
    static getMedicines() {
        return [];
    }

    // Vitals / Telemetry
    static getVitals() {
        this.init();
        try {
            return JSON.parse(localStorage.getItem("patient_vitals")) || DEFAULT_VITALS;
        } catch {
            return DEFAULT_VITALS;
        }
    }

    static updateVitals(vitalsUpdate) {
        const current = this.getVitals();
        const merged = { ...current, ...vitalsUpdate };
        localStorage.setItem("patient_vitals", JSON.stringify(merged));
        return merged;
    }

    // Prescriptions (Empty array maintained)
    static getPrescriptions() {
        return [];
    }

    // Recovery & Lab Reports
    static getLabReports() {
        this.init();
        this.purgeDummyData();
        try {
            return JSON.parse(localStorage.getItem("patient_lab_reports")) || DEFAULT_LAB_REPORTS;
        } catch {
            return DEFAULT_LAB_REPORTS;
        }
    }

    // Physiotherapists & Specialists
    static getDoctors() {
        this.init();
        this.purgeDummyData();
        try {
            const dummyNames = ["sarah jenkins", "rajesh kumar", "anita patel", "vikram malhotra", "meenakshi sundaram", "karthik raman", "sujipreethi", "suji"];
            const medimateDocs = JSON.parse(localStorage.getItem("medimateDoctors") || "[]");
            const allUsers = JSON.parse(localStorage.getItem("medimateUsers") || "[]");
            const userDocs = allUsers.filter(u => u.role === "doctor" || u.role === "physio");

            const registry = [];
            const seen = new Set();

            [...medimateDocs, ...userDocs].forEach(d => {
                const em = (d.email || d.id || "").toLowerCase();
                const rawName = (d.name || d.fullName || "Physiotherapist").trim();
                if (dummyNames.some(dn => rawName.toLowerCase().includes(dn))) return;

                if (em && !seen.has(em)) {
                    seen.add(em);
                    const docName = rawName.toLowerCase().startsWith("dr.") ? rawName : ("Dr. " + rawName);
                    registry.push({
                        id: d.id || ("DOC-" + Math.floor(1000 + Math.random() * 9000)),
                        name: docName,
                        department: d.department || d.specialization || "Orthopedic Rehabilitation",
                        qualifications: d.qualifications || "BPT, MPT",
                        experience: d.experience || "8+ Years",
                        rating: d.rating || 4.9,
                        reviewsCount: d.reviewsCount || 12,
                        fee: d.fee || "₹650",
                        avatar: docName.replace("Dr. ", "").split(" ").map(p => p[0]).join("").toUpperCase().substring(0, 2) || "PT",
                        availableDays: d.availableDays || "Mon - Sat",
                        nextSlot: d.nextSlot || "Today, 11:30 AM",
                        bio: d.bio || `Specialist in ${d.department || d.specialization || "Post-Accident Rehabilitation"}.`,
                        email: d.email,
                        phone: d.phone
                    });
                }
            });

            // If no custom doctors registered yet, provide default verified physios
            if (registry.length === 0) {
                return DEFAULT_DOCTORS;
            }

            return registry;
        } catch {
            return DEFAULT_DOCTORS;
        }
    }

    // Notifications
    static getNotifications() {
        this.init();
        try {
            return JSON.parse(localStorage.getItem("patient_notifications")) || DEFAULT_NOTIFICATIONS;
        } catch {
            return DEFAULT_NOTIFICATIONS;
        }
    }

    static addNotification(notif) {
        const notifs = this.getNotifications();
        const newNotif = {
            id: "NOTIF-" + Date.now(),
            ...notif
        };
        notifs.unshift(newNotif);
        localStorage.setItem("patient_notifications", JSON.stringify(notifs));
        return newNotif;
    }

    static markAllNotificationsRead() {
        const notifs = this.getNotifications();
        notifs.forEach(n => n.read = true);
        localStorage.setItem("patient_notifications", JSON.stringify(notifs));
    }

    // Recovery Documents / PDF Uploads
    static getHealthDocuments() {
        this.init();
        try {
            return JSON.parse(localStorage.getItem("patient_health_documents")) || [];
        } catch {
            return [];
        }
    }

    static saveHealthDocument(doc) {
        const docs = this.getHealthDocuments();
        const newDoc = {
            id: "DOC-REHAB-" + Date.now(),
            uploadedAt: new Date().toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' }),
            ...doc
        };
        docs.unshift(newDoc);
        localStorage.setItem("patient_health_documents", JSON.stringify(docs));

        this.addNotification({
            category: "document",
            title: "Recovery Document Saved",
            message: `"${newDoc.title}" successfully added to your records.`,
            time: "Just now",
            read: false,
            icon: "fa-solid fa-file-medical",
            link: "health-records.html"
        });

        return newDoc;
    }

    static deleteHealthDocument(id) {
        let docs = this.getHealthDocuments();
        docs = docs.filter(d => d.id !== id);
        localStorage.setItem("patient_health_documents", JSON.stringify(docs));
    }
}

// ============================================================================
// AUTHENTICATION & PORTAL SETUP
// ============================================================================

export function setupPatientAuth(activePageName = "") {
    PatientStore.init();

    // Verify session
    onAuthStateChanged(auth, function (user) {
        let savedUser = JSON.parse(localStorage.getItem("currentUser") || "null");
        const sessionUser = sessionStorage.getItem("medimateUser");

        if (!user && !savedUser && !sessionUser) {
            savedUser = { name: "Prakashraj R", role: "patient", email: "prakashraj@medimate.ai", id: "PAT-2026-9042" };
            localStorage.setItem("currentUser", JSON.stringify(savedUser));
        }

        const profile = PatientStore.getProfile();
        let name = profile.name || "Patient";

        if (savedUser && savedUser.name) {
            name = savedUser.name;
        } else if (user && user.displayName) {
            name = user.displayName;
        } else if (user && user.email) {
            name = user.email.split("@")[0];
        }

        const userNameEl = document.getElementById("userName");
        if (userNameEl) userNameEl.textContent = name;

        const welcomeNameEl = document.getElementById("welcomeName");
        if (welcomeNameEl) welcomeNameEl.textContent = name;

        const userAvatarEl = document.getElementById("userAvatar");
        if (userAvatarEl) {
            if (profile.photo) {
                userAvatarEl.innerHTML = `<img src="${profile.photo}" alt="Patient Avatar" style="width: 100%; height: 100%; border-radius: 50%; object-fit: cover;">`;
            } else {
                userAvatarEl.textContent = name.charAt(0).toUpperCase();
            }
        }

        updateNotificationBadge();
    });

    // Setup Logout
    const logoutBtn = document.getElementById("logoutBtn");
    if (logoutBtn) {
        logoutBtn.addEventListener("click", async function (e) {
            e.preventDefault();
            if (confirm("Are you sure you want to log out from Patient Portal?")) {
                try {
                    await signOut(auth);
                } catch (e) {
                    console.log("Firebase signout error:", e);
                }
                localStorage.removeItem("currentUser");
                localStorage.removeItem("userRole");
                localStorage.removeItem("userUID");
                sessionStorage.clear();
                window.location.href = "/login.html";
            }
        });
    }

    // Mobile Hamburger Toggle
    setupMobileSidebar();
}

function updateNotificationBadge() {
    const notifs = PatientStore.getNotifications();
    const unread = notifs.filter(n => !n.read).length;
    const badgeEl = document.getElementById("notifBadge");
    if (badgeEl) {
        if (unread > 0) {
            badgeEl.textContent = unread > 9 ? "9+" : unread;
            badgeEl.style.display = "flex";
        } else {
            badgeEl.style.display = "none";
        }
    }
}

function setupMobileSidebar() {
    const toggleBtn = document.getElementById("sidebarToggleBtn");
    const sidebar = document.querySelector(".sidebar");
    if (toggleBtn && sidebar) {
        toggleBtn.addEventListener("click", function () {
            sidebar.classList.toggle("mobile-open");
        });
        document.addEventListener("click", function (e) {
            if (sidebar.classList.contains("mobile-open") && !sidebar.contains(e.target) && !toggleBtn.contains(e.target)) {
                sidebar.classList.remove("mobile-open");
            }
        });
    }
}

export function showToast(message, type = "info") {
    let container = document.getElementById("toastContainer");
    if (!container) {
        container = document.createElement("div");
        container.id = "toastContainer";
        container.style.cssText = "position: fixed; bottom: 24px; right: 24px; z-index: 9999; display: flex; flex-direction: column; gap: 10px;";
        document.body.appendChild(container);
    }

    const toast = document.createElement("div");
    const bg = type === "success" ? "#0284c7" : type === "error" ? "#ef4444" : "#071733";
    const border = type === "success" ? "#38bdf8" : type === "error" ? "#f87171" : "rgba(56, 189, 248, 0.4)";
    const icon = type === "success" ? "fa-circle-check" : type === "error" ? "fa-circle-exclamation" : "fa-circle-info";

    toast.style.cssText = `
        background: ${bg};
        color: #ffffff;
        padding: 14px 20px;
        border-radius: 12px;
        border: 1px solid ${border};
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        font-size: 14px;
        font-weight: 600;
        display: flex;
        align-items: center;
        gap: 12px;
        min-width: 280px;
        animation: toastIn 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    `;

    toast.innerHTML = `<i class="fa-solid ${icon}"></i> <span>${message}</span>`;
    container.appendChild(toast);

    setTimeout(() => {
        toast.style.opacity = "0";
        toast.style.transform = "translateX(20px)";
        toast.style.transition = "all 0.3s ease";
        setTimeout(() => toast.remove(), 300);
    }, 3500);
}
