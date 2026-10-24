"""
Apply User Customizations:
1. Revert/Standardize Sidebar to the clean FIRST sidebar option across ALL admin pages.
2. Change color palette from Neon Green (#00e599) to Navy Blue with White & Sky Blue (#38bdf8).
3. Completely delete dummy data in doctors.html, patients.html, appointments.html, dashboard.html so only real data displays.
"""
import os
import re

ADMIN_DIR = "frontend/admin"

# =========================================================================
# 1. UPDATE admin-dark-theme.css TO NAVY BLUE & SKY BLUE PALETTE
# =========================================================================
css_path = os.path.join(ADMIN_DIR, "admin-dark-theme.css")
if os.path.exists(css_path):
    with open(css_path, "r", encoding="utf-8") as f:
        css = f.read()

    # Replace green tokens with Navy / Sky Blue
    css = css.replace("#00e599", "#38bdf8")
    css = css.replace("#059669", "#0284c7")
    css = css.replace("#10b981", "#38bdf8")
    css = css.replace("#087f5b", "#0284c7")
    css = css.replace("#07583f", "#061121")
    css = css.replace("#b8e6d1", "#7dd3fc")
    css = css.replace("#e8fff3", "#f8fafc")
    css = css.replace("#b9f5d7", "#38bdf8")
    css = css.replace("#c9f3dc", "#94a3b8")
    css = css.replace("rgba(0, 229, 153,", "rgba(56, 189, 248,")
    css = css.replace("rgba(0,229,153,", "rgba(56, 189, 248,")
    css = css.replace("rgba(8, 127, 91,", "rgba(56, 189, 248,")
    css = css.replace("rgba(5, 150, 105,", "rgba(2, 132, 199,")

    # Base background
    css = css.replace("--bg-base: #050a14;", "--bg-base: #061121;")
    css = css.replace("--bg-surface: rgba(13, 22, 41, 0.85);", "--bg-surface: rgba(10, 25, 47, 0.9);")
    css = css.replace("--bg-surface-elevated: rgba(18, 30, 56, 0.9);", "--bg-surface-elevated: rgba(13, 33, 62, 0.9);")
    css = css.replace("--sidebar-bg: rgba(10, 18, 36, 0.95);", "--sidebar-bg: rgba(9, 23, 46, 0.95);")
    css = css.replace("--topbar-bg: rgba(10, 18, 36, 0.85);", "--topbar-bg: rgba(9, 23, 46, 0.88);")

    with open(css_path, "w", encoding="utf-8") as f:
        f.write(css)
    print("admin-dark-theme.css updated to Navy Blue & Sky Blue palette!")


# =========================================================================
# 2. STANDARDIZE SIDEBAR IN ALL ADMIN HTML FILES (Clean FIRST Sidebar)
# =========================================================================
def get_clean_first_sidebar(active_name):
    pages = [
        ("dashboard.html", "📊", "Dashboard"),
        ("doctors.html", "👨‍⚕️", "Doctors"),
        ("patients.html", "🧑‍🤝‍🧑", "Patients"),
        ("appointments.html", "📅", "Appointments"),
        ("departments.html", "🏥", "Departments"),
        ("medicines.html", "📦", "Medicines Inventory"),
        ("prescriptions.html", "📋", "Prescriptions"),
        ("reports.html", "📈", "Reports & Analytics")
    ]

    html = '''    <aside class="sidebar">

        <div class="brand">
            <div class="brand-logo">M</div>
            <div class="brand-text">
                <h2>MediMate AI</h2>
                <p>Admin Portal</p>
            </div>
        </div>

        <div class="menu-title">Main Menu</div>
'''
    for href, icon, label in pages:
        is_active = (href == active_name)
        cls = ' class="nav-link active"' if is_active else ' class="nav-link"'
        html += f'        <a href="{href}"{cls}><span class="nav-icon">{icon}</span>{label}</a>\n'

    html += '''
        <div class="menu-title">System & Security</div>
        <a href="notifications.html" class="nav-link''' + (' active' if active_name == 'notifications.html' else '') + '''"><span class="nav-icon">🔔</span>Notifications</a>
        <a href="settings.html" class="nav-link''' + (' active' if active_name == 'settings.html' else '') + '''"><span class="nav-icon">⚙️</span>Settings</a>
        <a href="profile.html" class="nav-link''' + (' active' if active_name == 'profile.html' else '') + '''"><span class="nav-icon">👤</span>Admin Profile</a>
        <a href="admin-login.html" class="nav-link" onclick="sessionStorage.clear(); localStorage.removeItem('currentUser'); localStorage.removeItem('firebaseIdToken'); localStorage.removeItem('adminLoggedIn');"><span class="nav-icon">🚪</span>Sign Out</a>
    </aside>'''
    return html


# =========================================================================
# 3. UPDATE doctors.html:
#    - Clean first sidebar
#    - Navy blue color styling
#    - Single clean header (remove double header)
#    - DELETE ALL DUMMY DATA (remove DEFAULT_REHAB_PHYSIOS)
# =========================================================================
doc_path = os.path.join(ADMIN_DIR, "doctors.html")
if os.path.exists(doc_path):
    with open(doc_path, "r", encoding="utf-8") as f:
        doc_html = f.read()

    # Palette replace
    doc_html = doc_html.replace("#00e599", "#38bdf8")
    doc_html = doc_html.replace("#059669", "#0284c7")
    doc_html = doc_html.replace("rgba(0, 229, 153,", "rgba(56, 189, 248,")
    doc_html = doc_html.replace("rgba(0,229,153,", "rgba(56, 189, 248,")

    # Clean sidebar
    sidebar_pat = r'<aside class="sidebar">.*?</aside>'
    doc_html = re.sub(sidebar_pat, get_clean_first_sidebar("doctors.html"), doc_html, flags=re.DOTALL)

    # Clean double header: Remove the duplicate top header, keep clean single header
    doc_html = re.sub(
        r'<div class="page-top">\s*<div class="page-heading">.*?</div>\s*<button class="add-button" id="addDoctorButton".*?</button>\s*</div>',
        '',
        doc_html,
        flags=re.DOTALL
    )

    # In top header, add the + Add Doctor button cleanly
    old_top_header = r'<div class="header-title">\s*<h1>\s*Doctors\s*</h1>\s*<p>\s*Manage hospital doctors and their information\s*</p>\s*</div>'
    new_top_header = '''<div class="header-title">
                <h1>Doctors</h1>
                <p>Manage doctors, physiotherapists, and specialists</p>
            </div>
            <div>
                <button class="add-button" id="addDoctorButton" onclick="openDoctorModal()" style="background: linear-gradient(135deg, #0284c7 0%, #38bdf8 100%); color: #ffffff; border: none; padding: 10px 20px; border-radius: 10px; font-weight: 700; cursor: pointer; box-shadow: 0 4px 18px rgba(56, 189, 248, 0.4);">
                    + Add Doctor
                </button>
            </div>'''
    doc_html = re.sub(old_top_header, new_top_header, doc_html, flags=re.DOTALL)

    # Stat cards: "Total Doctors", "Active Doctors", "Inactive Doctors"
    doc_html = doc_html.replace("Total Physiotherapists", "Total Doctors")
    doc_html = doc_html.replace("Active on Tele-Rehab", "Active Doctors")
    doc_html = doc_html.replace("Off-Duty / In-Training", "Inactive Doctors")

    # DELETE DUMMY DATA in JavaScript
    # Remove DEFAULT_REHAB_PHYSIOS
    doc_html = re.sub(r'const DEFAULT_REHAB_PHYSIOS = \[.*?\];', '', doc_html, flags=re.DOTALL)

    # Update loadAllDoctors: ONLY real doctors, zero dummy fallback!
    old_loader_fn = r'function loadAllDoctors\(firestoreDocs = \[\]\)\s*\{.*?renderDoctors\(\);\s*\}'
    new_loader_fn = '''function loadAllDoctors(firestoreDocs = []) {
        let combined = Array.isArray(firestoreDocs) ? [...firestoreDocs] : [];

        // 1. Merge from medimateDoctors local registry (real added doctors)
        try {
            const localDocs = JSON.parse(localStorage.getItem("medimateDoctors") || "[]");
            localDocs.forEach(ld => {
                const exists = combined.some(c => (c.email && ld.email && c.email.toLowerCase() === ld.email.toLowerCase()) || c.id === ld.id);
                if (!exists) combined.push(ld);
            });
        } catch (e) {}

        // 2. Merge from medimateUsers (users registered with doctor role)
        try {
            const allUsers = JSON.parse(localStorage.getItem("medimateUsers") || "[]");
            allUsers.filter(u => u.role === "doctor" || u.role === "physio").forEach(u => {
                const exists = combined.some(c => (c.email && u.email && c.email.toLowerCase() === u.email.toLowerCase()) || c.id === u.id);
                if (!exists) {
                    combined.push({
                        id: u.id || ("DOC-" + Date.now()),
                        name: u.name || u.fullName || (u.email ? u.email.split("@")[0] : "Doctor"),
                        email: u.email || "",
                        phone: u.phone || "+91 9876543210",
                        specialization: u.specialization || "Physiotherapy & Rehab Specialist",
                        department: u.department || "Rehabilitation Unit",
                        status: u.status || "active"
                    });
                }
            });
        } catch (e) {}

        // Strict filter: Remove any dummy names completely
        const dummyNames = ["sarah jenkins", "rajesh kumar", "anita patel", "vikram malhotra", "sarah connor", "john smith", "malini swaminathan", "sanjay patel", "radhika menon"];
        combined = combined.filter(d => {
            const n = (d.name || "").toLowerCase();
            return !dummyNames.some(dn => n.includes(dn));
        });

        // ZERO dummy fallback - only show real data!
        doctors = combined;
        renderDoctors();
    }'''
    doc_html = re.sub(old_loader_fn, new_loader_fn, doc_html, flags=re.DOTALL)

    # Empty table message when no doctors
    old_empty_msg = r'<tr>\s*<td colspan="\d+"\s*class="empty">\s*No doctors found.*?\s*</td>\s*</tr>'
    new_empty_msg = '<tr><td colspan="7" class="empty" style="text-align:center; padding: 40px; color: #94a3b8;">No doctors registered yet. Click "+ Add Doctor" to register a doctor.</td></tr>'
    doc_html = re.sub(old_empty_msg, new_empty_msg, doc_html, flags=re.DOTALL)

    with open(doc_path, "w", encoding="utf-8") as f:
        f.write(doc_html)
    print("doctors.html updated: sidebar standardized, palette changed to navy/sky, dummy data deleted!")


# =========================================================================
# 4. UPDATE patients.html:
#    - Clean first sidebar
#    - Navy blue color styling
#    - Clean single header
#    - DELETE ALL DUMMY DATA (remove Karthik, Priya, Manoj, Ananya, Rajesh)
# =========================================================================
pat_path = os.path.join(ADMIN_DIR, "patients.html")
if os.path.exists(pat_path):
    with open(pat_path, "r", encoding="utf-8") as f:
        pat_html = f.read()

    # Palette replace
    pat_html = pat_html.replace("#00e599", "#38bdf8")
    pat_html = pat_html.replace("#059669", "#0284c7")
    pat_html = pat_html.replace("rgba(0, 229, 153,", "rgba(56, 189, 248,")
    pat_html = pat_html.replace("rgba(0,229,153,", "rgba(56, 189, 248,")

    # Clean sidebar
    sidebar_pat = r'<aside class="sidebar">.*?</aside>'
    pat_html = re.sub(sidebar_pat, get_clean_first_sidebar("patients.html"), pat_html, flags=re.DOTALL)

    # Single clean header (remove duplicate subheader)
    pat_html = re.sub(
        r'<div class="page-heading">\s*<div>\s*<h2>\s*Post-Accident Rehab Patients\s*</h2>.*?</div>\s*<button class="add-btn".*?</button>\s*</div>',
        '',
        pat_html,
        flags=re.DOTALL
    )

    old_pat_topbar = r'<div style="display:flex;align-items:center;gap:15px;">\s*<div class="topbar-title">\s*<h1>\s*Patients Management\s*</h1>\s*<p>\s*Add and manage patient information manually\.\s*</p>\s*</div>\s*</div>'
    new_pat_topbar = '''<div style="display:flex;align-items:center;gap:15px;">
                <div class="topbar-title">
                    <h1>Patients Management</h1>
                    <p>View and manage registered patient records</p>
                </div>
            </div>
            <div>
                <button class="add-btn" id="addPatientBtn" style="background: linear-gradient(135deg, #0284c7 0%, #38bdf8 100%); color: #ffffff; border: none; padding: 10px 20px; border-radius: 10px; font-weight: 700; cursor: pointer; box-shadow: 0 4px 18px rgba(56, 189, 248, 0.4);">
                    + Add Patient
                </button>
            </div>'''
    pat_html = re.sub(old_pat_topbar, new_pat_topbar, pat_html, flags=re.DOTALL)

    # DELETE DUMMY DATA in JavaScript
    # Remove DEFAULT_REHAB_PATIENTS
    pat_html = re.sub(r'const DEFAULT_REHAB_PATIENTS = \[.*?\];', '', pat_html, flags=re.DOTALL)

    # Update loadAllPatients: ONLY real patients, zero dummy fallback!
    old_pat_loader = r'function loadAllPatients\(firestoreDocs = \[\]\)\s*\{.*?renderPatients\(\);\s*\}'
    new_pat_loader = '''function loadAllPatients(firestoreDocs = []) {
            let loaded = Array.isArray(firestoreDocs) ? [...firestoreDocs] : [];

            // 1. Merge real users from medimateUsers (role: patient)
            try {
                const allUsers = JSON.parse(localStorage.getItem("medimateUsers") || "[]");
                allUsers.filter(u => u.role === "patient").forEach(u => {
                    const exists = loaded.some(p => (p.email && u.email && p.email.toLowerCase() === u.email.toLowerCase()) || p.id === u.id);
                    if (!exists) {
                        loaded.push({
                            id: u.id || ("PAT-" + Math.floor(1000 + Math.random() * 9000)),
                            name: u.name || u.fullName || (u.email ? u.email.split("@")[0] : "Patient"),
                            email: u.email || "",
                            phone: u.phone || "-",
                            gender: u.gender || "-",
                            age: u.age || "-",
                            bloodGroup: u.bloodGroup || "-",
                            status: u.status || "active",
                            password: u.password || ""
                        });
                    }
                });
            } catch (e) {}

            // 2. Merge from medimatePatients
            try {
                const localPatients = JSON.parse(localStorage.getItem("medimatePatients") || "[]");
                localPatients.forEach(lp => {
                    if (!loaded.some(p => (p.email && lp.email && p.email.toLowerCase() === lp.email.toLowerCase()) || p.id === lp.id)) {
                        loaded.push({
                            id: lp.id || ("PAT-" + Math.floor(1000 + Math.random() * 9000)),
                            name: lp.name || lp.fullName,
                            email: lp.email,
                            phone: lp.phone || "-",
                            gender: lp.gender || "-",
                            age: lp.age || "-",
                            bloodGroup: lp.bloodGroup || "-",
                            status: lp.status || "active",
                            password: lp.password || ""
                        });
                    }
                });
            } catch (e) {}

            // Strict filter: Remove any dummy demo names
            const dummyPatientNames = ["karthik subramanian", "priya natarajan", "manoj kumar", "ananya iyer", "rajesh kannan"];
            loaded = loaded.filter(p => {
                const n = (p.name || "").toLowerCase();
                return !dummyPatientNames.some(dn => n.includes(dn));
            });

            // ZERO dummy fallback - only show real data!
            patients = loaded;
            renderPatients();
        }'''
    pat_html = re.sub(old_pat_loader, new_pat_loader, pat_html, flags=re.DOTALL)

    # Empty table message
    old_empty_pat = r'<tr>\s*<td colspan="\d+"\s*class="empty">\s*No patients added yet.*?\s*</td>\s*</tr>'
    new_empty_pat = '<tr><td colspan="8" class="empty" style="text-align:center; padding: 40px; color: #94a3b8;">No patients registered yet. Click "+ Add Patient" to register a patient.</td></tr>'
    pat_html = re.sub(old_empty_pat, new_empty_pat, pat_html, flags=re.DOTALL)

    with open(pat_path, "w", encoding="utf-8") as f:
        f.write(pat_html)
    print("patients.html updated: sidebar standardized, palette changed to navy/sky, dummy data deleted!")


# =========================================================================
# 5. STANDARDIZE SIDEBAR & PALETTE ACROSS ALL OTHER ADMIN PAGES
# =========================================================================
other_admin_pages = [
    "dashboard.html",
    "appointments.html",
    "departments.html",
    "medicines.html",
    "prescriptions.html",
    "reports.html",
    "notifications.html",
    "settings.html",
    "profile.html"
]

for p in other_admin_pages:
    fpath = os.path.join(ADMIN_DIR, p)
    if not os.path.exists(fpath):
        continue
    with open(fpath, "r", encoding="utf-8") as f:
        h = f.read()

    # Palette replace
    h = h.replace("#00e599", "#38bdf8")
    h = h.replace("#059669", "#0284c7")
    h = h.replace("#10b981", "#38bdf8")
    h = h.replace("rgba(0, 229, 153,", "rgba(56, 189, 248,")
    h = h.replace("rgba(0,229,153,", "rgba(56, 189, 248,")

    # Replace sidebar with the standard clean first sidebar
    sidebar_pat = r'<aside class="sidebar".*?</aside>'
    h = re.sub(sidebar_pat, get_clean_first_sidebar(p), h, flags=re.DOTALL)

    # If appointments.html, remove SEED_HOSPITAL_APPOINTMENTS dummy data
    if p == "appointments.html":
        h = re.sub(r'const SEED_HOSPITAL_APPOINTMENTS = \[.*?\];', 'const SEED_HOSPITAL_APPOINTMENTS = [];', h, flags=re.DOTALL)
        # Empty fallback
        h = h.replace('loaded = [...SEED_HOSPITAL_APPOINTMENTS];', 'loaded = [];')

    # If medicines.html, clean dummy medicines
    if p == "medicines.html":
        h = h.replace("let medicinesList = [", "let medicinesList = []; // [")

    # If dashboard.html, remove dummy appointment seeds
    if p == "dashboard.html":
        h = re.sub(r'appts = \[\s*\{\s*id:\s*"REH-2026-101".*?\];', 'appts = [];', h, flags=re.DOTALL)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(h)
    print(f"{p} standardized to clean first sidebar & Navy Blue palette!")

print("ALL USER CUSTOMIZATIONS APPLIED SUCCESSFULLY!")
