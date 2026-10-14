import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 16:9 widescreen presentation layout
fig, ax = plt.subplots(figsize=(16, 9.2), dpi=300)
fig.patch.set_facecolor('#ffffff')
ax.set_facecolor('#ffffff')
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

# Slide Top Title
ax.text(50, 96.5, "SYSTEM DESIGN", ha='center', va='center',
        color='#0f172a', fontsize=22, fontweight='bold', family='sans-serif')
ax.text(50, 93.2, "MediMate-AI - Integrated Clinical Decision-Support & Healthcare Management System",
        ha='center', va='center', color='#0284c7', fontsize=11.5, fontweight='bold', family='sans-serif')

# ================= 1. LEFT CONTAINER: CLIENT LAYER =================
# Outer container box with dashed blue border
c1 = patches.FancyBboxPatch((2, 10), 16.5, 79, boxstyle="round,pad=0.4",
                            facecolor='#f8fafc', edgecolor='#38bdf8', linestyle='--', linewidth=1.5)
ax.add_patch(c1)
# Header tag
h1 = patches.FancyBboxPatch((4, 85.5), 12.5, 3.2, boxstyle="round,pad=0.2",
                            facecolor='#0284c7', edgecolor='none')
ax.add_patch(h1)
ax.text(10.25, 87.1, "Client Layer", ha='center', va='center', color='white', fontsize=10.5, fontweight='bold')

# Card 1: Web Browser / Client
b_web = patches.FancyBboxPatch((3.5, 52), 13.5, 28, boxstyle="round,pad=0.4",
                              facecolor='#eff6ff', edgecolor='#93c5fd', linewidth=1.2)
ax.add_patch(b_web)
ax.text(10.25, 73, "[ Web Browser ]", ha='center', va='center', color='#1d4ed8', fontsize=11, fontweight='bold')
ax.text(10.25, 65, "Responsive Web App\n& Healthcare Portal", ha='center', va='center',
        color='#0f172a', fontsize=9.5, fontweight='bold')
ax.text(10.25, 56, "(Desktop & Mobile PWA)", ha='center', va='center', color='#64748b', fontsize=8)

# Vertical Arrow between Web and Roles
ax.annotate('', xy=(10.25, 45), xytext=(10.25, 52),
            arrowprops=dict(arrowstyle="<->", color='#0284c7', lw=1.8))

# Card 2: 5 Roles
b_roles = patches.FancyBboxPatch((3.5, 14), 13.5, 30, boxstyle="round,pad=0.4",
                                facecolor='#faf5ff', edgecolor='#d8b4fe', linewidth=1.2)
ax.add_patch(b_roles)
ax.text(10.25, 39, "[ Roles: 5 Portals ]", ha='center', va='center', color='#7e22ce', fontsize=10, fontweight='bold')
ax.text(10.25, 32.5, "• Patient / Caregiver", ha='center', va='center', color='#334155', fontsize=8.5)
ax.text(10.25, 27.5, "• Doctor / Specialist", ha='center', va='center', color='#334155', fontsize=8.5)
ax.text(10.25, 22.5, "• Laboratory Tech", ha='center', va='center', color='#334155', fontsize=8.5)
ax.text(10.25, 17.5, "• Pharmacist", ha='center', va='center', color='#334155', fontsize=8.5)
ax.text(10.25, 12.5, "• Hospital Admin", ha='center', va='center', color='#334155', fontsize=8.5)

# HTTPS Arrow (Client -> Application Layer)
ax.annotate('', xy=(20.5, 66), xytext=(17, 66),
            arrowprops=dict(arrowstyle="<->", color='#0284c7', lw=2))
ax.text(18.75, 68, "HTTPS", ha='center', va='center', color='#0369a1', fontsize=8.5, fontweight='bold')


# ================= 2. MIDDLE CONTAINER: APPLICATION LAYER =================
c2 = patches.FancyBboxPatch((20.5, 10), 55, 79, boxstyle="round,pad=0.4",
                            facecolor='#f8fafc', edgecolor='#38bdf8', linestyle='--', linewidth=1.5)
ax.add_patch(c2)
# Header tag
h2 = patches.FancyBboxPatch((35, 85.5), 26, 3.2, boxstyle="round,pad=0.2",
                            facecolor='#0284c7', edgecolor='none')
ax.add_patch(h2)
ax.text(48, 87.1, "MediMate-AI Application Layer", ha='center', va='center', color='white', fontsize=10.5, fontweight='bold')

# Row 1: Frontend UI <-> Backend API
b_fe = patches.FancyBboxPatch((22.5, 67), 23, 14, boxstyle="round,pad=0.4",
                             facecolor='#f0fdf4', edgecolor='#86efac', linewidth=1.2)
ax.add_patch(b_fe)
ax.text(34, 76.5, "[ Frontend UI ]", ha='center', va='center', color='#15803d', fontsize=11, fontweight='bold')
ax.text(34, 71, "(HTML5, CSS3, Vanilla JS ES6+)\n5 Modular Role Portals", ha='center', va='center',
        color='#334155', fontsize=8.5)

# Arrow FE <-> BE
ax.annotate('', xy=(50.5, 74), xytext=(45.5, 74),
            arrowprops=dict(arrowstyle="<->", color='#0284c7', lw=1.8))
ax.text(48, 76, "REST API", ha='center', va='center', color='#0369a1', fontsize=7.5, fontweight='bold')

b_be = patches.FancyBboxPatch((50.5, 67), 23, 14, boxstyle="round,pad=0.4",
                             facecolor='#eff6ff', edgecolor='#93c5fd', linewidth=1.2)
ax.add_patch(b_be)
ax.text(62, 76.5, "[ Backend API Gateway ]", ha='center', va='center', color='#1d4ed8', fontsize=11, fontweight='bold')
ax.text(62, 71, "(Flask Microframework)\n15 REST Blueprints & RBAC Auth", ha='center', va='center',
        color='#334155', fontsize=8.5)

# Vertical Arrow BE -> Down to Core Modules
ax.annotate('', xy=(62, 60.5), xytext=(62, 67),
            arrowprops=dict(arrowstyle="->", color='#0284c7', lw=1.5))

# Row 2: Preethi AI Engine + ML Risk Classifier
b_ai = patches.FancyBboxPatch((22.5, 47), 25, 13.5, boxstyle="round,pad=0.4",
                             facecolor='#fefce8', edgecolor='#fde047', linewidth=1.2)
ax.add_patch(b_ai)
ax.text(35, 56.5, "Preethi AI Clinical Engine", ha='center', va='center', color='#a16207', fontsize=10, fontweight='bold')
ax.text(35, 51.5, "• NLP Symptom Parser & Triage\n• Emergency 108 Red Alert", ha='center', va='center',
        color='#334155', fontsize=8)

b_ml = patches.FancyBboxPatch((49.5, 47), 24, 13.5, boxstyle="round,pad=0.4",
                             facecolor='#faf5ff', edgecolor='#d8b4fe', linewidth=1.2)
ax.add_patch(b_ml)
ax.text(61.5, 56.5, "ML Risk Classifier", ha='center', va='center', color='#7e22ce', fontsize=10, fontweight='bold')
ax.text(61.5, 51.5, "• Random Forest (100 Trees)\n• Vitals Telemetry (BP/Sugar/HR)", ha='center', va='center',
        color='#334155', fontsize=8)

# Arrow AI <-> ML
ax.annotate('', xy=(49.5, 53.7), xytext=(47.5, 53.7),
            arrowprops=dict(arrowstyle="<->", color='#7e22ce', lw=1.2))

# Row 3: Stakeholder Dashboards & Modules
# Patient Dashboard
b_pat = patches.FancyBboxPatch((22, 27), 16.5, 16.5, boxstyle="round,pad=0.3",
                              facecolor='#ecfeff', edgecolor='#67e8f9', linewidth=1.2)
ax.add_patch(b_pat)
ax.text(30.25, 39.5, "Patient Portal", ha='center', va='center', color='#0e7490', fontsize=9.5, fontweight='bold')
ax.text(30.25, 33, "• Vitals Telemetry\n• Preethi AI Chat\n• Lab Reports PDF\n• Emergency ID", ha='center', va='center',
        color='#334155', fontsize=7.5)

# Doctor Dashboard
b_doc = patches.FancyBboxPatch((39.5, 27), 17.5, 16.5, boxstyle="round,pad=0.3",
                              facecolor='#eff6ff', edgecolor='#93c5fd', linewidth=1.2)
ax.add_patch(b_doc)
ax.text(48.25, 39.5, "Doctor Workspace", ha='center', va='center', color='#1d4ed8', fontsize=9.5, fontweight='bold')
ax.text(48.25, 33, "• Patient Queue\n• WebRTC Video\n• Longitudinal EHR\n• SHA-256 e-Rx", ha='center', va='center',
        color='#334155', fontsize=7.5)

# Appointment Module
b_apt = patches.FancyBboxPatch((58, 27), 16, 16.5, boxstyle="round,pad=0.3",
                              facecolor='#fef2f2', edgecolor='#fca5a5', linewidth=1.2)
ax.add_patch(b_apt)
ax.text(66, 39.5, "Appointments", ha='center', va='center', color='#b91c1c', fontsize=9.5, fontweight='bold')
ax.text(66, 33, "• Slot Booking\n• Telehealth Queue\n• Reschedule / Cancel\n• Status Sync", ha='center', va='center',
        color='#334155', fontsize=7.5)

# Row 4 (Bottom of Application Layer): Lab, Pharmacy & Admin
b_lab = patches.FancyBboxPatch((22, 12), 16.5, 12.5, boxstyle="round,pad=0.3",
                              facecolor='#f0fdf4', edgecolor='#86efac', linewidth=1.2)
ax.add_patch(b_lab)
ax.text(30.25, 20.5, "Laboratory Portal", ha='center', va='center', color='#15803d', fontsize=9, fontweight='bold')
ax.text(30.25, 15.5, "• Barcode Accession\n• Analyte Results", ha='center', va='center', color='#334155', fontsize=7.5)

b_pharma = patches.FancyBboxPatch((39.5, 12), 17.5, 12.5, boxstyle="round,pad=0.3",
                                 facecolor='#fffbeb', edgecolor='#fcd34d', linewidth=1.2)
ax.add_patch(b_pharma)
ax.text(48.25, 20.5, "Pharmacy Portal", ha='center', va='center', color='#b45309', fontsize=9, fontweight='bold')
ax.text(48.25, 15.5, "• e-Rx Dispensation\n• Auto Stock & Expiry", ha='center', va='center', color='#334155', fontsize=7.5)

b_adm = patches.FancyBboxPatch((58, 12), 16, 12.5, boxstyle="round,pad=0.3",
                              facecolor='#f8fafc', edgecolor='#cbd5e1', linewidth=1.2)
ax.add_patch(b_adm)
ax.text(66, 20.5, "Admin Dashboard", ha='center', va='center', color='#475569', fontsize=9, fontweight='bold')
ax.text(66, 15.5, "• Hospital Analytics\n• Staff Roles & Alerts", ha='center', va='center', color='#334155', fontsize=7.5)


# ================= 3. RIGHT CONTAINER: DATA & EXTERNAL SERVICES =================
c3 = patches.FancyBboxPatch((78, 10), 20, 79, boxstyle="round,pad=0.4",
                            facecolor='#f8fafc', edgecolor='#38bdf8', linestyle='--', linewidth=1.5)
ax.add_patch(c3)
# Header tag
h3 = patches.FancyBboxPatch((79.5, 85.5), 17, 3.2, boxstyle="round,pad=0.2",
                            facecolor='#0284c7', edgecolor='none')
ax.add_patch(h3)
ax.text(88, 87.1, "Data & Services", ha='center', va='center', color='white', fontsize=10.5, fontweight='bold')

# Box 1: Database
b_db = patches.FancyBboxPatch((79.5, 59), 17, 22, boxstyle="round,pad=0.4",
                             facecolor='#faf5ff', edgecolor='#d8b4fe', linewidth=1.2)
ax.add_patch(b_db)
ax.text(88, 76.5, "[ Cloud Database ]", ha='center', va='center', color='#7e22ce', fontsize=10, fontweight='bold')
ax.text(88, 67.5, "Google Cloud Firestore\n• Users & Patients\n• Doctors & EHR\n• Prescriptions & Labs\n• Vitals Telemetry",
        ha='center', va='center', color='#334155', fontsize=7.8)

# Box 2: Auth Service
b_auth = patches.FancyBboxPatch((79.5, 36), 17, 19, boxstyle="round,pad=0.4",
                               facecolor='#eff6ff', edgecolor='#93c5fd', linewidth=1.2)
ax.add_patch(b_auth)
ax.text(88, 50.5, "[ Security & Auth ]", ha='center', va='center', color='#1d4ed8', fontsize=10, fontweight='bold')
ax.text(88, 43, "Firebase Auth SDK\n• Multi-Role RBAC\n• JWT RS256 Tokens\n• Encrypted Passwords",
        ha='center', va='center', color='#334155', fontsize=7.8)

# Box 3: Notification & Models
b_ext = patches.FancyBboxPatch((79.5, 14), 17, 18, boxstyle="round,pad=0.4",
                              facecolor='#eff6ff', edgecolor='#93c5fd', linewidth=1.2)
ax.add_patch(b_ext)
ax.text(88, 27.5, "[ External Services ]", ha='center', va='center', color='#0369a1', fontsize=10, fontweight='bold')
ax.text(88, 20, "• In-App / System Alerts\n• 108 Emergency Alerts\n• Joblib ML Models\n• WebRTC Video Rooms",
        ha='center', va='center', color='#334155', fontsize=7.8)

# Connectors: Application Layer -> Data Layer
# Read/Write Data
ax.annotate('', xy=(79.5, 71), xytext=(73.5, 71),
            arrowprops=dict(arrowstyle="<->", color='#0284c7', lw=1.8))
ax.text(76.5, 73, "read/write", ha='center', va='center', color='#0369a1', fontsize=7.5, fontweight='bold')

# Auth Requests
ax.annotate('', xy=(79.5, 46), xytext=(73.5, 46),
            arrowprops=dict(arrowstyle="<->", color='#0284c7', lw=1.8))
ax.text(76.5, 48, "auth verify", ha='center', va='center', color='#0369a1', fontsize=7.5, fontweight='bold')

# Send Alerts
ax.annotate('', xy=(79.5, 23), xytext=(73.5, 23),
            arrowprops=dict(arrowstyle="->", color='#0284c7', lw=1.8))
ax.text(76.5, 25, "send alerts", ha='center', va='center', color='#0369a1', fontsize=7.5, fontweight='bold')

# Bottom Caption
ax.text(50, 4.5, "System Architecture", ha='center', va='center',
        color='#0f172a', fontsize=14, fontweight='bold', family='sans-serif')
ax.text(50, 2, "MediMate AI - Integrated Clinical Decision-Support & Healthcare Management System",
        ha='center', va='center', color='#64748b', fontsize=9)

plt.tight_layout()
output_path = r"c:\Users\DELL\Documents\MediMate-AI\medimate_system_design_diagram.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print("Successfully generated exact system design diagram at:", output_path)
