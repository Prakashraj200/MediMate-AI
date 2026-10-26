import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os
import shutil

# 16:9 widescreen presentation layout (High-DPI 300 for HD Projectors & Slides)
fig, ax = plt.subplots(figsize=(16, 9.2), dpi=300)
fig.patch.set_facecolor('#ffffff')
ax.set_facecolor('#ffffff')
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

# Slide Top Title & Subtitle (Huge, Bold & Professional)
ax.text(50, 96.8, "DATABASE DESIGN (ER DIAGRAM)", ha='center', va='center',
        color='#0f172a', fontsize=24, fontweight='bold', family='sans-serif')
ax.text(50, 93.4, "MediMate-AI: Google Cloud Firestore NoSQL Collections & Normalized Relational Schema",
        ha='center', va='center', color='#0284c7', fontsize=12.5, fontweight='bold', family='sans-serif')

def draw_er_table(ax, x, y, w, h, table_name, fields, header_color='#1e3a8a'):
    # Outer container with crisp border
    box = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.15",
                                facecolor='#ffffff', edgecolor='#64748b', linewidth=1.6)
    ax.add_patch(box)
    
    # Table Header Compartment
    header_h = 3.6
    header = patches.FancyBboxPatch((x, y + h - header_h), w, header_h, boxstyle="round,pad=0.15",
                                     facecolor=header_color, edgecolor='#64748b', linewidth=1.6)
    ax.add_patch(header)
    ax.text(x + w / 2, y + h - (header_h / 2), table_name, ha='center', va='center',
            color='white', fontsize=10.2, fontweight='bold', family='sans-serif')
    
    # Fields Compartment
    start_y = y + h - header_h - 1.2
    line_spacing = 2.15
    for i, (fname, ftype, is_key) in enumerate(fields):
        fy = start_y - (i * line_spacing)
        if fy < y + 0.5:
            break
            
        # Key Badge
        if is_key == "PK":
            ax.text(x + 1.0, fy, "PK", color='#b45309', fontsize=8.2, fontweight='bold', family='sans-serif',
                    bbox=dict(boxstyle="round,pad=0.1", facecolor='#fef3c7', edgecolor='#f59e0b', lw=0.8))
        elif is_key == "FK":
            ax.text(x + 1.0, fy, "FK", color='#0284c7', fontsize=8.2, fontweight='bold', family='sans-serif',
                    bbox=dict(boxstyle="round,pad=0.1", facecolor='#e0f2fe', edgecolor='#38bdf8', lw=0.8))
        else:
            ax.text(x + 1.2, fy, "•", color='#94a3b8', fontsize=9.0, fontweight='bold')
            
        # Field Name & Type
        ax.text(x + 3.8, fy, fname, color='#0f172a', fontsize=8.6, fontweight='bold', family='monospace')
        ax.text(x + w - 1.0, fy, ftype, color='#64748b', fontsize=8.0, ha='right', family='sans-serif')

# ==============================================================================
# ROW 1: CORE IDENTITY & USER MODELS (Y = 68.0 to 89.0)
# ==============================================================================

# 1. patients (Left)
draw_er_table(ax, 4.0, 68.0, 26.0, 21.0, "patients (Collection)", [
    ("patient_id", "string", "PK"),
    ("user_id", "string", "FK"),
    ("mrn", "string", ""),
    ("trauma_type", "string (ACL/Menis.)", ""),
    ("days_post_acc", "number", ""),
    ("baseline_vas", "float (0-10)", ""),
    ("physio_id", "string", "FK")
], header_color='#0284c7')

# 2. users (Center - Central Identity Anchor)
draw_er_table(ax, 37.0, 68.0, 26.0, 21.0, "users (Collection)", [
    ("uid", "string", "PK"),
    ("name", "string", ""),
    ("email", "string", ""),
    ("role", "string [patient/physio/admin]", ""),
    ("phone", "string", ""),
    ("is_active", "boolean", ""),
    ("created_at", "timestamp", "")
], header_color='#1e293b')

# 3. physiotherapists (Right)
draw_er_table(ax, 70.0, 68.0, 26.0, 21.0, "physiotherapists (Collection)", [
    ("physio_id", "string", "PK"),
    ("user_id", "string", "FK"),
    ("license_no", "string", ""),
    ("specialization", "string", ""),
    ("experience_yrs", "number", ""),
    ("active_patients", "number", ""),
    ("consult_fee", "number", "")
], header_color='#0f766e')

# Clean Horizontal Connections in Row 1 (No Overlaps!):
# users -> patients
ax.annotate('', xy=(30.0, 78.5), xytext=(37.0, 78.5),
            arrowprops=dict(arrowstyle="->", color='#0284c7', lw=2.0))
ax.text(33.5, 80.5, "1 : 1", ha='center', fontsize=8.5, color='#0284c7', fontweight='bold',
        bbox=dict(boxstyle="round,pad=0.15", facecolor='#ffffff', edgecolor='#cbd5e1'))

# users -> physiotherapists
ax.annotate('', xy=(70.0, 78.5), xytext=(63.0, 78.5),
            arrowprops=dict(arrowstyle="->", color='#0f766e', lw=2.0))
ax.text(66.5, 80.5, "1 : 1", ha='center', fontsize=8.5, color='#0f766e', fontweight='bold',
        bbox=dict(boxstyle="round,pad=0.15", facecolor='#ffffff', edgecolor='#cbd5e1'))


# ==============================================================================
# ROW 2: TELEMETRY, ML PROGNOSIS & CONVERSATIONAL AI (Y = 38.0 to 59.0)
# ==============================================================================

# 4. vitals_telemetry (Left - Aligned under patients)
draw_er_table(ax, 4.0, 38.0, 26.0, 21.0, "vitals_telemetry", [
    ("telemetry_id", "string", "PK"),
    ("patient_id", "string", "FK"),
    ("vas_score", "float (0-10)", ""),
    ("rom_deficit", "float (degrees)", ""),
    ("swelling_grade", "string", ""),
    ("logged_at", "timestamp", ""),
    ("sync_status", "string", "")
], header_color='#7c3aed')

# 5. preethi_ai_logs (Center - NLP Triage)
draw_er_table(ax, 37.0, 38.0, 26.0, 21.0, "preethi_ai_logs (NLP Triage)", [
    ("log_id", "string", "PK"),
    ("patient_id", "string", "FK"),
    ("symptom_query", "string", ""),
    ("intent_label", "string", ""),
    ("triage_level", "string (Red/Yellow)", ""),
    ("recommended_rx", "string", ""),
    ("timestamp", "timestamp", "")
], header_color='#d97706')

# 6. recovery_traces (Right - Aligned under physiotherapists)
draw_er_table(ax, 70.0, 38.0, 26.0, 21.0, "recovery_traces (ML Prognosis)", [
    ("trace_id", "string", "PK"),
    ("patient_id", "string", "FK"),
    ("predicted_days", "float (R²=0.941)", ""),
    ("phi_chronic", "float (0-1)", ""),
    ("plateau_flag", "boolean", ""),
    ("model_version", "string (RF_v1.5)", ""),
    ("forecast_at", "timestamp", "")
], header_color='#059669')

# Connections Row 1 to Row 2:
# patients -> vitals_telemetry (Direct straight down line on left)
ax.annotate('', xy=(17.0, 59.0), xytext=(17.0, 68.0),
            arrowprops=dict(arrowstyle="->", color='#7c3aed', lw=2.0))
ax.text(17.0, 63.5, "1 : N (Daily Telemetry)", ha='center', fontsize=8.5, color='#7c3aed', fontweight='bold',
        bbox=dict(boxstyle="round,pad=0.15", facecolor='#ffffff', edgecolor='#cbd5e1'))

# patients -> preethi_ai_logs
ax.annotate('', xy=(37.0, 52.0), xytext=(30.0, 68.0),
            arrowprops=dict(arrowstyle="->", color='#d97706', lw=2.0))
ax.text(32.0, 58.5, "1 : N (AI Chats)", ha='center', fontsize=8.5, color='#d97706', fontweight='bold',
        bbox=dict(boxstyle="round,pad=0.15", facecolor='#ffffff', edgecolor='#cbd5e1'))

# physiotherapists -> recovery_traces (Direct straight down line on right)
ax.annotate('', xy=(83.0, 59.0), xytext=(83.0, 68.0),
            arrowprops=dict(arrowstyle="->", color='#059669', lw=2.0))
ax.text(83.0, 63.5, "1 : N (Prognosis Cohort)", ha='center', fontsize=8.5, color='#059669', fontweight='bold',
        bbox=dict(boxstyle="round,pad=0.15", facecolor='#ffffff', edgecolor='#cbd5e1'))


# ==============================================================================
# ROW 3: REHAB PRESCRIPTIONS & WEBRTC SESSIONS (Y = 8.0 to 28.0)
# ==============================================================================

# 7. rehab_prescriptions
draw_er_table(ax, 16.0, 8.0, 31.0, 20.0, "rehab_prescriptions (Clinical Regimens)", [
    ("rx_id", "string", "PK"),
    ("patient_id", "string", "FK"),
    ("physio_id", "string", "FK"),
    ("protocols", "array<string>", ""),
    ("hold_duration_sec", "number", ""),
    ("sets_reps_spec", "string", ""),
    ("sha256_signature", "string", "")
], header_color='#e11d48')

# 8. webrtc_sessions
draw_er_table(ax, 53.0, 8.0, 31.0, 20.0, "webrtc_sessions (Tele-Rehab P2P)", [
    ("session_id", "string", "PK"),
    ("room_code", "string", ""),
    ("patient_id", "string", "FK"),
    ("physio_id", "string", "FK"),
    ("sdp_offer", "map", ""),
    ("sdp_answer", "map", ""),
    ("session_status", "string (active/ended)", "")
], header_color='#2563eb')

# Connections to Row 3:
# vitals_telemetry -> rehab_prescriptions
ax.annotate('', xy=(31.0, 28.0), xytext=(22.0, 38.0),
            arrowprops=dict(arrowstyle="->", color='#e11d48', lw=2.0))
ax.text(25.0, 33.0, "1 : N (Prescriptions)", ha='center', fontsize=8.5, color='#e11d48', fontweight='bold',
        bbox=dict(boxstyle="round,pad=0.15", facecolor='#ffffff', edgecolor='#cbd5e1'))

# recovery_traces -> webrtc_sessions
ax.annotate('', xy=(69.0, 28.0), xytext=(78.0, 38.0),
            arrowprops=dict(arrowstyle="->", color='#2563eb', lw=2.0))
ax.text(75.0, 33.0, "1 : N (Video Rooms)", ha='center', fontsize=8.5, color='#2563eb', fontweight='bold',
        bbox=dict(boxstyle="round,pad=0.15", facecolor='#ffffff', edgecolor='#cbd5e1'))

# Save outputs to both report_diagrams and artifacts
dest_path = r"c:\Users\DELL\Documents\MediMate-AI\frontend\report_diagrams\database_design_er.png"
fig_dest = r"c:\Users\DELL\Documents\MediMate-AI\frontend\report_diagrams\medimate_database_design.png"
legacy_dest = r"c:\Users\DELL\Documents\MediMate-AI\frontend\report_diagrams\fig_3_7_er_diagram.png"
art_dest = r"C:\Users\DELL\.gemini\antigravity\brain\4a9ee622-b1af-4b4c-9362-e46c9e06f79e\database_design_er.png"
art_fig = r"C:\Users\DELL\.gemini\antigravity\brain\4a9ee622-b1af-4b4c-9362-e46c9e06f79e\medimate_database_design.png"

plt.savefig(dest_path, format='png', dpi=300, bbox_inches='tight', facecolor='#ffffff')
plt.savefig(fig_dest, format='png', dpi=300, bbox_inches='tight', facecolor='#ffffff')
plt.savefig(legacy_dest, format='png', dpi=300, bbox_inches='tight', facecolor='#ffffff')
plt.close(fig)

shutil.copy(dest_path, art_dest)
shutil.copy(dest_path, art_fig)

print(f"SUCCESS: Redesigned ER Database Diagram generated! Size: {os.path.getsize(dest_path)} bytes")
