import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os
import shutil

# 16:9 Presentation Canvas (High-DPI 300 for HD Projectors & Slides)
fig, ax = plt.subplots(figsize=(16, 9.2), dpi=300)
fig.patch.set_facecolor('#ffffff')
ax.set_facecolor('#ffffff')
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

# Slide Top Title & Subtitle (Huge, Bold & Professional)
ax.text(50, 96.8, "UML SEQUENCE DIAGRAM", ha='center', va='center',
        color='#0f172a', fontsize=24, fontweight='bold', family='sans-serif')
ax.text(50, 93.4, "MediMate-AI: End-to-End Tele-Rehabilitation, AI Triage & Pain Prognosis Workflow",
        ha='center', va='center', color='#0284c7', fontsize=12.5, fontweight='bold', family='sans-serif')

# Define 6 Lifelines / Participants with well-spaced X coordinates
lifelines = [
    {"name": "Patient\n(Client Web)", "x": 10.5, "bg": "#e0f2fe", "border": "#0284c7", "text_col": "#0369a1"},
    {"name": "Flask REST API\n(Gateway)", "x": 28.5, "bg": "#f1f5f9", "border": "#475569", "text_col": "#1e293b"},
    {"name": "Preethi AI\n(NLP Triage)", "x": 46.0, "bg": "#fef3c7", "border": "#d97706", "text_col": "#92400e"},
    {"name": "Prognosis ML\n(Random Forest)", "x": 62.5, "bg": "#dcfce7", "border": "#16a34a", "text_col": "#15803d"},
    {"name": "Cloud Firestore\n(NoSQL DB)", "x": 78.5, "bg": "#ede9fe", "border": "#7c3aed", "text_col": "#6d28d9"},
    {"name": "Physiotherapist\n(Console)", "x": 93.5, "bg": "#ccfbf1", "border": "#0d9488", "text_col": "#0f766e"}
]

# Draw Lifelines & Header / Footer Boxes
y_top_box = 85.0
y_bot_box = 5.0
box_w = 11.5
box_h = 4.8

for item in lifelines:
    x = item["x"]
    # Top Box
    hdr = patches.FancyBboxPatch((x - box_w/2, y_top_box), box_w, box_h, boxstyle="round,pad=0.2",
                                facecolor=item["bg"], edgecolor=item["border"], linewidth=2.0)
    ax.add_patch(hdr)
    ax.text(x, y_top_box + box_h/2, item["name"], ha='center', va='center',
            color=item["text_col"], fontsize=9.8, fontweight='bold', family='sans-serif')
    
    # Vertical Dashed Lifeline Line
    ax.plot([x, x], [y_bot_box + box_h, y_top_box], color='#94a3b8', linestyle='--', linewidth=1.5, zorder=1)
    
    # Bottom Box
    ftr = patches.FancyBboxPatch((x - box_w/2, y_bot_box), box_w, box_h, boxstyle="round,pad=0.2",
                                facecolor=item["bg"], edgecolor=item["border"], linewidth=2.0)
    ax.add_patch(ftr)
    ax.text(x, y_bot_box + box_h/2, item["name"].replace('\n', ' '), ha='center', va='center',
            color=item["text_col"], fontsize=8.5, fontweight='bold', family='sans-serif')

# Function to draw Activation Bars on Lifelines
def draw_activation_bar(x, y_start, y_end, color='#94a3b8'):
    w = 1.2
    h = y_start - y_end
    bar = patches.Rectangle((x - w/2, y_end), w, h,
                            facecolor='#ffffff', edgecolor=color, linewidth=1.6, zorder=2)
    ax.add_patch(bar)

# Draw Activation Bars for Lifelines
draw_activation_bar(10.5, 83.0, 8.0, '#0284c7')
draw_activation_bar(28.5, 83.0, 10.0, '#475569')
draw_activation_bar(46.0, 69.0, 56.0, '#d97706')
draw_activation_bar(62.5, 54.0, 42.0, '#16a34a')
draw_activation_bar(78.5, 78.0, 13.0, '#7c3aed')
draw_activation_bar(93.5, 48.0, 12.0, '#0d9488')

# Helper function to draw clean, non-overlapping sequence messages
def draw_seq_message(x1, x2, y, label, is_response=False, color='#0284c7', text_offset_y=1.25, custom_mid_x=None):
    ls = '--' if is_response else '-'
    ax.annotate('', xy=(x2, y), xytext=(x1, y),
                arrowprops=dict(arrowstyle="->", color=color, lw=1.8, linestyle=ls), zorder=3)
    
    mid_x = (x1 + x2) / 2 if custom_mid_x is None else custom_mid_x
    ax.text(mid_x, y + text_offset_y, label, ha='center', va='center',
            color='#0f172a', fontsize=8.6, fontweight='bold', family='sans-serif', zorder=4,
            bbox=dict(boxstyle="round,pad=0.26", facecolor='#ffffff', edgecolor='#cbd5e1', lw=1.1, alpha=0.96))

# Helper function for self-calls (internal processing loop)
def draw_self_call(x, y, label, color='#0284c7'):
    ax.annotate('', xy=(x + 0.6, y - 2.5), xytext=(x + 0.6, y),
                arrowprops=dict(arrowstyle="->", color=color, lw=1.8, connectionstyle="arc3,rad=-0.6"), zorder=3)
    ax.text(x + 4.0, y - 1.25, label, ha='left', va='center',
            color='#0f172a', fontsize=8.4, fontweight='bold', family='sans-serif', zorder=4,
            bbox=dict(boxstyle="round,pad=0.25", facecolor='#ffffff', edgecolor='#cbd5e1', lw=1.1, alpha=0.96))

# ==============================================================================
# SEQUENCE STEPS (Chronological Flow)
# ==============================================================================

# 1. Auth & Daily Telemetry Submission
draw_seq_message(10.5, 28.5, 80.5, "1: POST /api/telemetry (VAS: 7/10, ROM: 25°, Swelling: Gr.II)", False, '#0284c7')
draw_seq_message(28.5, 78.5, 76.5, "2: Insert Telemetry Record (vitals_telemetry collection)", False, '#7c3aed')
draw_seq_message(78.5, 28.5, 72.8, "3: 201 Created (Telemetry ID: vitals_9024)", True, '#7c3aed')

# 2. Conversational Triage with Preethi AI
draw_seq_message(10.5, 28.5, 68.5, "4: Patient Query: \"Severe joint throbbing & knee effusion\"", False, '#0284c7')
draw_seq_message(28.5, 46.0, 64.8, "5: invoke_triage_pipeline(symptom_text)", False, '#d97706')
draw_self_call(46.0, 62.0, "TF-IDF + LinearSVC Intent Triage\n(100% Red-Flag Recall / Cryotherapy Protocol)", '#d97706')
draw_seq_message(46.0, 28.5, 56.5, "6: Return Cryotherapy Protocol & Red-Flag Escalation Alert", True, '#d97706')
draw_seq_message(28.5, 10.5, 52.8, "7: Immediate Patient Guidance: Apply RICE & Physio notified", True, '#0284c7')

# 3. Machine Learning Prognosis Evaluation
draw_seq_message(28.5, 62.5, 48.5, "8: predict_recovery_trajectory(VAS=7, ROM=25°, Age=38)", False, '#16a34a')
draw_self_call(62.5, 46.0, "Random Forest Regressor (R²=0.941)\nForecast: 24.5 Days | Φ_chronic: 0.72", '#16a34a')
draw_seq_message(62.5, 78.5, 40.5, "9: Store Prognosis & Plateau Risk (recovery_traces collection)", False, '#16a34a')

# 4. Clinician Alert & WebRTC Consultation
draw_seq_message(78.5, 93.5, 36.5, "10: Push Red-Flag Alert & High Plateau Risk", True, '#7c3aed')
draw_seq_message(93.5, 28.5, 32.5, "11: POST /api/webrtc/create-session (Emergency Tele-Rehab)", False, '#0d9488')
draw_seq_message(28.5, 10.5, 28.5, "12: Push WebRTC Invite (Room: REHAB-941, STUN/TURN)", True, '#0284c7')

# Direct WebRTC P2P Stream Between Patient & Physio
ax.annotate('', xy=(93.5, 24.5), xytext=(10.5, 24.5),
            arrowprops=dict(arrowstyle="<->", color='#2563eb', lw=2.2, linestyle='-'), zorder=3)
ax.text(50.0, 25.7, "13: WebRTC P2P Video Tele-Rehab Stream (DTLS/SRTP Encrypted + Sync Timer)", ha='center', va='center',
        color='#1e40af', fontsize=9.2, fontweight='bold', family='sans-serif', zorder=4,
        bbox=dict(boxstyle="round,pad=0.28", facecolor='#eff6ff', edgecolor='#3b82f6', lw=1.2))

# 5. Prescription Dispatch & Adherence Sync
draw_seq_message(93.5, 28.5, 20.5, "14: Issue Rehab Prescription (Quad Isometric: 15s Hold, 3 Sets)", False, '#0d9488')
draw_seq_message(28.5, 78.5, 16.5, "15: Save Signed Prescription (rehab_prescriptions / SHA-256)", False, '#7c3aed')
draw_seq_message(28.5, 10.5, 12.5, "16: 200 OK: Synchronized Exercise Protocol Updated on Portal", True, '#0284c7')

# Save outputs to both report_diagrams and artifacts
dest_path = r"c:\Users\DELL\Documents\MediMate-AI\frontend\report_diagrams\uml_sequence_diagram.png"
fig_dest = r"c:\Users\DELL\Documents\MediMate-AI\frontend\report_diagrams\medimate_module_sequence_diagram.png"
legacy_dest = r"c:\Users\DELL\Documents\MediMate-AI\frontend\report_diagrams\fig_3_5_uml_sequence.png"
art_dest = r"C:\Users\DELL\.gemini\antigravity\brain\4a9ee622-b1af-4b4c-9362-e46c9e06f79e\uml_sequence_diagram.png"
art_fig = r"C:\Users\DELL\.gemini\antigravity\brain\4a9ee622-b1af-4b4c-9362-e46c9e06f79e\medimate_module_sequence_diagram.png"

plt.savefig(dest_path, format='png', dpi=300, bbox_inches='tight', facecolor='#ffffff')
plt.savefig(fig_dest, format='png', dpi=300, bbox_inches='tight', facecolor='#ffffff')
plt.savefig(legacy_dest, format='png', dpi=300, bbox_inches='tight', facecolor='#ffffff')
plt.close(fig)

shutil.copy(dest_path, art_dest)
shutil.copy(dest_path, art_fig)

print(f"SUCCESS: UML Sequence Diagram regenerated! Size: {os.path.getsize(dest_path)} bytes")
