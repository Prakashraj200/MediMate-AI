/**
 * MediMate AI - Patient Portal Common Data & Utility Service
 * Provides centralized data synchronization, authentication verification,
 * notifications, and interactive portal functionality.
 */

import { auth } from "../static/js/firebase-config.js";
import { onAuthStateChanged, signOut } from "https://www.gstatic.com/firebasejs/12.19.0/firebase-auth.js";

// ============================================================================
// DEFAULT SEED DATA
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
    primaryPhysician: "",
    allergies: ["Penicillin", "Peanuts", "Dust Mites"],
    chronicConditions: ["Mild Hypertension"],
    joinedDate: "January 2024"
};

const DEFAULT_APPOINTMENTS = [];

const DEFAULT_MEDICINES = [
    {
        id: "MED-01",
        name: "Telmisartan 40mg",
        generic: "Telmisartan",
        dosage: "40 mg",
        timing: ["Morning"],
        scheduleDescription: "1 tablet daily after breakfast",
        purpose: "Blood Pressure control",
        prescribedBy: "Dr. Sarah Jenkins",
        startDate: "2026-08-01",
        duration: "90 Days",
        remainingPills: 28,
        totalPills: 90,
        takenToday: {
            morning: true,
            afternoon: false,
            evening: false,
            night: false
        },
        refillNeeded: false,
        instructions: "Take with water. Do not skip morning dose."
    },
    {
        id: "MED-02",
        name: "Atorvastatin 10mg",
        generic: "Atorvastatin Calcium",
        dosage: "10 mg",
        timing: ["Night"],
        scheduleDescription: "1 tablet before bedtime",
        purpose: "Cholesterol management",
        prescribedBy: "Dr. Rajesh Kumar",
        startDate: "2026-09-01",
        duration: "60 Days",
        remainingPills: 14,
        totalPills: 60,
        takenToday: {
            morning: false,
            afternoon: false,
            evening: false,
            night: false
        },
        refillNeeded: true,
        instructions: "Take at bedtime. Avoid eating grapefruit."
    },
    {
        id: "MED-03",
        name: "Vitamin D3 60,000 IU",
        generic: "Cholecalciferol",
        dosage: "60,000 IU",
        timing: ["Morning"],
        scheduleDescription: "1 capsule once weekly on Sundays",
        purpose: "Bone & Immune Health",
        prescribedBy: "Dr. Rajesh Kumar",
        startDate: "2026-09-10",
        duration: "8 Weeks",
        remainingPills: 4,
        totalPills: 8,
        takenToday: {
            morning: true,
            afternoon: false,
            evening: false,
            night: false
        },
        refillNeeded: false,
        instructions: "Take after breakfast with a glass of milk or warm water."
    },
    {
        id: "MED-04",
        name: "Omega-3 Fish Oil 1000mg",
        generic: "EPA + DHA Fatty Acids",
        dosage: "1000 mg",
        timing: ["Afternoon"],
        scheduleDescription: "1 softgel daily after lunch",
        purpose: "Cardiovascular wellness",
        prescribedBy: "Dr. Sarah Jenkins",
        startDate: "2026-08-15",
        duration: "120 Days",
        remainingPills: 52,
        totalPills: 120,
        takenToday: {
            morning: false,
            afternoon: true,
            evening: false,
            night: false
        },
        refillNeeded: false,
        instructions: "Take with a full meal."
    }
];

const DEFAULT_VITALS = {
    bloodPressure: {
        systolic: 120,
        diastolic: 80,
        unit: "mmHg",
        status: "Normal",
        lastChecked: "Today, 08:30 AM",
        history: [
            { date: "Oct 13", value: "120/80" },
            { date: "Oct 10", value: "122/82" },
            { date: "Oct 06", value: "124/84" },
            { date: "Oct 01", value: "119/79" }
        ]
    },
    heartRate: {
        value: 72,
        unit: "bpm",
        status: "Optimal",
        lastChecked: "Today, 08:30 AM"
    },
    bloodSugar: {
        fasting: 95,
        postPrandial: 132,
        unit: "mg/dL",
        status: "Normal",
        lastChecked: "Yesterday, 07:45 AM"
    },
    oxygenSaturation: {
        value: 99,
        unit: "% SpO2",
        status: "Normal",
        lastChecked: "Today, 08:30 AM"
    },
    bodyTemp: {
        value: 98.4,
        unit: "°F",
        status: "Normal",
        lastChecked: "Today, 08:30 AM"
    },
    weight: {
        value: 68.0,
        unit: "kg",
        status: "Healthy BMI (22.5)",
        lastChecked: "Oct 10, 2026"
    }
};

const DEFAULT_PRESCRIPTIONS = [
    {
        id: "RX-2026-8841",
        date: "2026-09-01",
        doctorName: "Dr. Sarah Jenkins",
        doctorDepartment: "Department of Cardiology",
        doctorReg: "MCI-48192-TN",
        diagnosis: "Stage 1 Essential Hypertension (Well Controlled)",
        medicines: [
            { name: "Telmisartan", dosage: "40 mg", frequency: "1-0-0", duration: "90 Days", instructions: "After breakfast" },
            { name: "Omega-3 Marine Lipid", dosage: "1000 mg", frequency: "0-1-0", duration: "90 Days", instructions: "After lunch" }
        ],
        advice: "Low sodium diet (<2.3g/day). 30 minutes brisk walking 5 days a week. Keep daily blood pressure log.",
        nextVisit: "2026-12-01",
        status: "Active"
    },
    {
        id: "RX-2026-7215",
        date: "2026-08-10",
        doctorName: "Dr. Rajesh Kumar",
        doctorDepartment: "Internal Medicine",
        doctorReg: "MCI-31094-TN",
        diagnosis: "Mild Dyslipidemia & Vitamin D Insufficiency",
        medicines: [
            { name: "Atorvastatin", dosage: "10 mg", frequency: "0-0-1", duration: "60 Days", instructions: "Bedtime" },
            { name: "Cholecalciferol D3", dosage: "60,000 IU", frequency: "Once Weekly", duration: "8 Weeks", instructions: "Sundays after meal" }
        ],
        advice: "Limit fried foods and refined sugar. Recheck Lipid Profile in 8 weeks.",
        nextVisit: "2026-10-22",
        status: "Active"
    },
    {
        id: "RX-2026-5540",
        date: "2026-05-14",
        doctorName: "Dr. Anita Patel",
        doctorDepartment: "Department of Dermatology",
        doctorReg: "MCI-55219-TN",
        diagnosis: "Contact Dermatitis / Xerosis",
        medicines: [
            { name: "Hydrocortisone Cream 1%", dosage: "Apply thin layer", frequency: "0-1-0", duration: "7 Days", instructions: "External use only" },
            { name: "Cetaphil Restoraderm Lotion", dosage: "Liberal application", frequency: "1-1-1", duration: "30 Days", instructions: "Post shower" }
        ],
        advice: "Avoid harsh perfumed soaps. Drink adequate fluids.",
        nextVisit: "Completed",
        status: "Completed"
    }
];

const DEFAULT_LAB_REPORTS = [
    {
        id: "LAB-9801",
        testName: "Lipid Profile Comprehensive",
        category: "Biochemistry",
        date: "2026-10-02",
        labTechnician: "S. Murugan, Senior Biochemist",
        status: "Completed",
        flag: "Borderline",
        summary: "Total cholesterol mildly elevated. Triglycerides and HDL within optimal targets.",
        parameters: [
            { name: "Total Cholesterol", value: 205, unit: "mg/dL", normalRange: "< 200", status: "Borderline High" },
            { name: "HDL Cholesterol (Good)", value: 52, unit: "mg/dL", normalRange: "> 40", status: "Normal" },
            { name: "LDL Cholesterol (Bad)", value: 122, unit: "mg/dL", normalRange: "< 100", status: "Mildly High" },
            { name: "Triglycerides", value: 140, unit: "mg/dL", normalRange: "< 150", status: "Normal" },
            { name: "VLDL Cholesterol", value: 28, unit: "mg/dL", normalRange: "< 30", status: "Normal" }
        ]
    },
    {
        id: "LAB-9802",
        testName: "Complete Blood Count (CBC) with ESR",
        category: "Hematology",
        date: "2026-09-12",
        labTechnician: "R. Kavitha, Lab Technologist",
        status: "Completed",
        flag: "Normal",
        summary: "All red cell, white cell and platelet indices within normal physiological limits.",
        parameters: [
            { name: "Hemoglobin", value: 14.8, unit: "g/dL", normalRange: "13.5 - 17.5", status: "Normal" },
            { name: "Total Leukocyte Count (WBC)", value: 6800, unit: "cells/mcL", normalRange: "4000 - 11000", status: "Normal" },
            { name: "Platelet Count", value: 245000, unit: "/mcL", normalRange: "150000 - 450000", status: "Normal" },
            { name: "RBC Count", value: 5.1, unit: "million/mcL", normalRange: "4.5 - 5.9", status: "Normal" },
            { name: "ESR (Westergren)", value: 8, unit: "mm/hr", normalRange: "0 - 15", status: "Normal" }
        ]
    },
    {
        id: "LAB-9803",
        testName: "Glycated Hemoglobin (HbA1c)",
        category: "Endocrinology",
        date: "2026-09-12",
        labTechnician: "S. Murugan, Senior Biochemist",
        status: "Completed",
        flag: "Normal",
        summary: "Non-diabetic range with excellent glucose regulation over past 90 days.",
        parameters: [
            { name: "HbA1c Level", value: 5.4, unit: "%", normalRange: "< 5.7", status: "Normal" },
            { name: "Estimated Average Glucose (eAG)", value: 108, unit: "mg/dL", normalRange: "< 117", status: "Normal" }
        ]
    },
    {
        id: "LAB-9804",
        testName: "Thyroid Stimulating Hormone (TSH)",
        category: "Immunoassay",
        date: "2026-08-01",
        labTechnician: "R. Kavitha, Lab Technologist",
        status: "Completed",
        flag: "Normal",
        summary: "Thyroid function within euthyroid reference range.",
        parameters: [
            { name: "Ultrasensitive TSH", value: 2.15, unit: "uIU/mL", normalRange: "0.4 - 4.2", status: "Normal" }
        ]
    },
    {
        id: "LAB-9805",
        testName: "Electrocardiogram (12-Lead ECG)",
        category: "Cardiology Diagnostic",
        date: "2026-07-15",
        labTechnician: "Dr. Sarah Jenkins",
        status: "Completed",
        flag: "Normal",
        summary: "Normal sinus rhythm, heart rate 72 bpm. No ST-T changes or arrhythmias noted.",
        parameters: [
            { name: "Rhythm", value: "Normal Sinus", unit: "-", normalRange: "Sinus", status: "Normal" },
            { name: "PR Interval", value: 148, unit: "ms", normalRange: "120 - 200", status: "Normal" },
            { name: "QRS Duration", value: 88, unit: "ms", normalRange: "80 - 120", status: "Normal" },
            { name: "QTc Interval", value: 412, unit: "ms", normalRange: "< 440", status: "Normal" }
        ]
    }
];

const DEFAULT_DOCTORS = [
    {
        id: "DOC-01",
        name: "Dr. Sarah Jenkins",
        department: "Cardiology",
        qualifications: "MBBS, MD (Cardiology), DM, FACC",
        experience: "15+ Years",
        rating: 4.9,
        reviewsCount: 342,
        fee: "₹800",
        avatar: "👩‍⚕️",
        availableDays: "Mon, Wed, Fri",
        nextSlot: "Tomorrow, 10:30 AM",
        bio: "Specialist in non-invasive cardiology, preventive coronary health, and clinical hypertension management."
    },
    {
        id: "DOC-02",
        name: "Dr. Rajesh Kumar",
        department: "General Medicine",
        qualifications: "MBBS, MD (Internal Medicine)",
        experience: "18+ Years",
        rating: 4.8,
        reviewsCount: 512,
        fee: "₹500",
        avatar: "👨‍⚕️",
        availableDays: "Mon to Sat",
        nextSlot: "Today, 04:30 PM",
        bio: "Expert internal medicine physician focusing on adult chronic disease management, diabetes, and preventive checkups."
    },
    {
        id: "DOC-03",
        name: "Dr. Anita Patel",
        department: "Dermatology",
        qualifications: "MBBS, MD (Dermatology, Venereology & Leprosy)",
        experience: "11+ Years",
        rating: 4.9,
        reviewsCount: 280,
        fee: "₹650",
        avatar: "👩‍⚕️",
        availableDays: "Tue, Thu, Sat",
        nextSlot: "Thursday, 11:00 AM",
        bio: "Consultant dermatologist specializing in allergic skin disorders, clinical cosmetics, and scalp health."
    },
    {
        id: "DOC-04",
        name: "Dr. Vikram Malhotra",
        department: "Orthopedics",
        qualifications: "MBBS, MS (Orthopedics), M.Ch (Joint Replacement)",
        experience: "14+ Years",
        rating: 4.7,
        reviewsCount: 219,
        fee: "₹900",
        avatar: "👨‍⚕️",
        availableDays: "Mon, Tue, Thu",
        nextSlot: "Friday, 02:00 PM",
        bio: "Orthopedic surgeon specializing in sports medicine, arthroscopy, and joint preservation treatments."
    },
    {
        id: "DOC-05",
        name: "Dr. Meenakshi Sundaram",
        department: "Neurology",
        qualifications: "MBBS, MD, DM (Neurology)",
        experience: "20+ Years",
        rating: 5.0,
        reviewsCount: 194,
        fee: "₹1,000",
        avatar: "👩‍⚕️",
        availableDays: "Wed, Fri, Sat",
        nextSlot: "Saturday, 09:30 AM",
        bio: "Senior consultant neurologist treating migraine, neuropathies, sleep disorders, and stroke rehabilitation."
    },
    {
        id: "DOC-06",
        name: "Dr. Karthik Raman",
        department: "Pediatrics",
        qualifications: "MBBS, DCH, DNB (Pediatrics)",
        experience: "12+ Years",
        rating: 4.8,
        reviewsCount: 388,
        fee: "₹600",
        avatar: "👨‍⚕️",
        availableDays: "Mon to Fri",
        nextSlot: "Tomorrow, 03:00 PM",
        bio: "Pediatric care specialist focusing on childhood immunization, growth tracking, and adolescent health."
    }
];

const DEFAULT_NOTIFICATIONS = [
    {
        id: "NOTIF-01",
        category: "appointment",
        title: "Welcome to MediMate AI",
        message: "Welcome to MediMate AI! Manage your health records, view assigned prescriptions, and connect with clinical departments.",
        time: "1 hour ago",
        read: false,
        icon: "📅",
        link: "appointments.html"
    },
    {
        id: "NOTIF-02",
        category: "medicine",
        title: "Medication Refill Alert",
        message: "Your Atorvastatin 10mg has only 14 days of supply remaining. Tap to request an easy refill from MediMate Pharmacy.",
        time: "5 hours ago",
        read: false,
        icon: "💊",
        link: "medicines.html"
    },
    {
        id: "NOTIF-03",
        category: "lab",
        title: "Lab Report Ready for Download",
        message: "Your Lipid Profile Comprehensive report from Oct 02 is verified and ready to view.",
        time: "2 days ago",
        read: true,
        icon: "🧪",
        link: "lab-reports.html"
    },
    {
        id: "NOTIF-04",
        category: "system",
        title: "New AI Healthcare Assistant: Preethi AI",
        message: "Preethi AI is now online to help you understand symptoms, medications, and wellness guidelines 24/7.",
        time: "4 days ago",
        read: true,
        icon: "🤖",
        link: "preethi-ai.html"
    }
];

// ============================================================================
// DATA STORE REPOSITORY
// ============================================================================

export class PatientStore {
    static init() {
        if (!localStorage.getItem("patient_profile")) {
            localStorage.setItem("patient_profile", JSON.stringify(DEFAULT_PATIENT_PROFILE));
        }
        if (!localStorage.getItem("patient_appointments")) {
            localStorage.setItem("patient_appointments", JSON.stringify(DEFAULT_APPOINTMENTS));
        }
        if (!localStorage.getItem("patient_medicines")) {
            localStorage.setItem("patient_medicines", JSON.stringify(DEFAULT_MEDICINES));
        }
        if (!localStorage.getItem("patient_vitals")) {
            localStorage.setItem("patient_vitals", JSON.stringify(DEFAULT_VITALS));
        }
        if (!localStorage.getItem("patient_prescriptions")) {
            localStorage.setItem("patient_prescriptions", JSON.stringify(DEFAULT_PRESCRIPTIONS));
        }
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
            // Priority: logged-in currentUser
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
            return { ...DEFAULT_PATIENT_PROFILE, ...prof };
        } catch {
            return DEFAULT_PATIENT_PROFILE;
        }
    }

    static saveProfile(profile) {
        localStorage.setItem("patient_profile", JSON.stringify(profile));
        // Also sync currentUser if exists
        const currentUser = JSON.parse(localStorage.getItem("currentUser") || "{}");
        currentUser.name = profile.name;
        currentUser.email = profile.email;
        currentUser.phone = profile.phone;
        localStorage.setItem("currentUser", JSON.stringify(currentUser));
    }

    // Appointments
    static getAppointments() {
        this.init();
        try {
            return JSON.parse(localStorage.getItem("patient_appointments")) || DEFAULT_APPOINTMENTS;
        } catch {
            return DEFAULT_APPOINTMENTS;
        }
    }

    static addAppointment(apt) {
        const apts = this.getAppointments();
        const newApt = {
            id: "APT-" + (1000 + apts.length + 1),
            status: "Confirmed",
            ...apt
        };
        apts.unshift(newApt);
        localStorage.setItem("patient_appointments", JSON.stringify(apts));
        
        // Add notification
        this.addNotification({
            category: "appointment",
            title: "Appointment Booked Successfully",
            message: `Your appointment with ${newApt.doctorName} for ${newApt.date} at ${newApt.time} is confirmed.`,
            time: "Just now",
            read: false,
            icon: "📅",
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

    // Medicines
    static getMedicines() {
        this.init();
        try {
            return JSON.parse(localStorage.getItem("patient_medicines")) || DEFAULT_MEDICINES;
        } catch {
            return DEFAULT_MEDICINES;
        }
    }

    static toggleMedicineDose(medId, timeOfDay) {
        const meds = this.getMedicines();
        const med = meds.find(m => m.id === medId);
        if (med) {
            if (!med.takenToday) med.takenToday = {};
            med.takenToday[timeOfDay] = !med.takenToday[timeOfDay];
            localStorage.setItem("patient_medicines", JSON.stringify(meds));
            return med;
        }
        return null;
    }

    static requestRefill(medId) {
        const meds = this.getMedicines();
        const med = meds.find(m => m.id === medId);
        if (med) {
            med.refillRequested = true;
            med.refillStatus = "Processing with Pharmacy";
            localStorage.setItem("patient_medicines", JSON.stringify(meds));

            this.addNotification({
                category: "medicine",
                title: "Refill Request Submitted",
                message: `Refill request for ${med.name} sent to MediMate Central Pharmacy.`,
                time: "Just now",
                read: false,
                icon: "💊",
                link: "medicines.html"
            });
            return true;
        }
        return false;
    }

    // Vitals
    static getVitals() {
        this.init();
        try {
            return JSON.parse(localStorage.getItem("patient_vitals")) || DEFAULT_VITALS;
        } catch {
            return DEFAULT_VITALS;
        }
    }

    static logVitals(newVitals) {
        const vitals = this.getVitals();
        if (newVitals.systolic && newVitals.diastolic) {
            vitals.bloodPressure.systolic = Number(newVitals.systolic);
            vitals.bloodPressure.diastolic = Number(newVitals.diastolic);
            vitals.bloodPressure.lastChecked = "Just now";
            if (!vitals.bloodPressure.history) vitals.bloodPressure.history = [];
            vitals.bloodPressure.history.unshift({
                date: "Today",
                value: `${newVitals.systolic}/${newVitals.diastolic}`
            });
        }
        if (newVitals.heartRate) {
            vitals.heartRate.value = Number(newVitals.heartRate);
            vitals.heartRate.lastChecked = "Just now";
        }
        if (newVitals.bloodSugar) {
            vitals.bloodSugar.fasting = Number(newVitals.bloodSugar);
            vitals.bloodSugar.lastChecked = "Just now";
        }
        if (newVitals.oxygenSaturation) {
            vitals.oxygenSaturation.value = Number(newVitals.oxygenSaturation);
            vitals.oxygenSaturation.lastChecked = "Just now";
        }
        if (newVitals.bodyTemp) {
            vitals.bodyTemp.value = Number(newVitals.bodyTemp);
            vitals.bodyTemp.lastChecked = "Just now";
        }
        if (newVitals.weight) {
            vitals.weight.value = Number(newVitals.weight);
            vitals.weight.lastChecked = "Just now";
        }
        localStorage.setItem("patient_vitals", JSON.stringify(vitals));
        return vitals;
    }

    // Prescriptions
    static getPrescriptions() {
        this.init();
        try {
            return JSON.parse(localStorage.getItem("patient_prescriptions")) || DEFAULT_PRESCRIPTIONS;
        } catch {
            return DEFAULT_PRESCRIPTIONS;
        }
    }

    // Lab Reports
    static getLabReports() {
        this.init();
        try {
            return JSON.parse(localStorage.getItem("patient_lab_reports")) || DEFAULT_LAB_REPORTS;
        } catch {
            return DEFAULT_LAB_REPORTS;
        }
    }

    // Doctors
    static getDoctors() {
        this.init();
        try {
            // Check real registered doctors first from medimateDoctors and medimateUsers
            const medimateDocs = JSON.parse(localStorage.getItem("medimateDoctors") || "[]");
            const allUsers = JSON.parse(localStorage.getItem("medimateUsers") || "[]");
            const userDocs = allUsers.filter(u => u.role === "doctor");

            const registry = [];
            const seen = new Set();

            [...medimateDocs, ...userDocs].forEach(d => {
                const em = (d.email || d.id || "").toLowerCase();
                if (em && !seen.has(em)) {
                    seen.add(em);
                    const rawName = (d.name || d.fullName || "Doctor").trim();
                    const docName = rawName.toLowerCase().startsWith("dr.") ? rawName : ("Dr. " + rawName);
                    registry.push({
                        id: d.id || ("DOC-" + Math.floor(1000 + Math.random() * 9000)),
                        name: docName,
                        department: d.department || d.specialization || "General Medicine",
                        qualifications: d.qualifications || "MBBS, MD",
                        experience: d.experience || "10+ Years",
                        rating: d.rating || 5.0,
                        reviewsCount: d.reviewsCount || 1,
                        fee: d.fee || "₹500",
                        avatar: "👨‍⚕️",
                        availableDays: d.availableDays || "Mon to Sat",
                        nextSlot: d.nextSlot || "Today, 10:00 AM",
                        bio: d.bio || `Specialist in ${d.department || d.specialization || "General Medicine"}.`,
                        email: d.email,
                        phone: d.phone
                    });
                }
            });

            // If real doctors are registered, ONLY return real registered doctors!
            if (registry.length > 0) {
                return registry;
            }

            return registry;
        } catch {
            return [];
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

    // Health Documents / PDF Uploads
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
            id: "DOC-PDF-" + Date.now(),
            uploadedAt: new Date().toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' }),
            ...doc
        };
        docs.unshift(newDoc);
        localStorage.setItem("patient_health_documents", JSON.stringify(docs));

        this.addNotification({
            category: "record",
            title: "Medical PDF Uploaded",
            message: `Document "${newDoc.title}" has been securely attached to your health records.`,
            time: "Just now",
            read: false,
            icon: "📄",
            link: "health-records.html"
        });

        return newDoc;
    }

    static deleteHealthDocument(id) {
        let docs = this.getHealthDocuments();
        docs = docs.filter(d => d.id !== id);
        localStorage.setItem("patient_health_documents", JSON.stringify(docs));
        return true;
    }
}

// ============================================================================
// AUTH & HEADER SETUP
// ============================================================================

export function setupPatientAuth(activePageName = "") {
    PatientStore.init();

    // Verify session
    onAuthStateChanged(auth, function (user) {
        const savedUser = JSON.parse(localStorage.getItem("currentUser") || "null");
        const sessionUser = sessionStorage.getItem("medimateUser");

        if (!user && !savedUser && !sessionUser) {
            // Unauthenticated
            window.location.href = "patient-login.html";
            return;
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

        // Update name fields
        const userNameEl = document.getElementById("userName");
        if (userNameEl) userNameEl.textContent = name;

        const welcomeNameEl = document.getElementById("welcomeName");
        if (welcomeNameEl) welcomeNameEl.textContent = name;

        // Update avatar
        const userAvatarEl = document.getElementById("userAvatar");
        if (userAvatarEl) {
            userAvatarEl.textContent = name.charAt(0).toUpperCase();
        }

        // Update notification badge
        updateNotificationBadge();
    });

    // Setup Logout
    const logoutBtn = document.getElementById("logoutBtn");
    if (logoutBtn) {
        logoutBtn.addEventListener("click", async function () {
            if (confirm("Are you sure you want to log out from Patient Portal?")) {
                try {
                    await signOut(auth);
                } catch (e) {
                    console.log("Firebase signout error:", e);
                }
                localStorage.removeItem("currentUser");
                localStorage.removeItem("userRole");
                localStorage.removeItem("userUID");
                sessionStorage.removeItem("medimateRole");
                sessionStorage.removeItem("medimateUser");
                sessionStorage.removeItem("medimateUid");
                window.location.href = "patient-login.html";
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

        // Close when clicking outside
        document.addEventListener("click", function (e) {
            if (!sidebar.contains(e.target) && !toggleBtn.contains(e.target) && sidebar.classList.contains("mobile-open")) {
                sidebar.classList.remove("mobile-open");
            }
        });
    }
}

// ============================================================================
// TOAST NOTIFICATION UTILITY
// ============================================================================

export function showToast(message, type = "success") {
    let toast = document.getElementById("portalToast");
    if (!toast) {
        toast = document.createElement("div");
        toast.id = "portalToast";
        toast.className = "portal-toast";
        document.body.appendChild(toast);
    }

    const icons = {
        success: "✅",
        error: "⚠️",
        info: "ℹ️"
    };

    toast.innerHTML = `<span class="toast-icon">${icons[type] || "ℹ️"}</span><span>${message}</span>`;
    toast.className = `portal-toast show ${type}`;

    setTimeout(() => {
        toast.className = "portal-toast";
    }, 3500);
}
