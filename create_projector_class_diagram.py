import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os
import shutil

# 16:9 Presentation Canvas (High-DPI for HD Projector)
fig, ax = plt.subplots(figsize=(16, 9.2), dpi=300)
fig.patch.set_facecolor('#ffffff')
ax.set_facecolor('#ffffff')
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

# Slide Top Title & Subtitle (Huge, Bold & Professional)
ax.text(50, 96.8, "UML CLASS DIAGRAM", ha='center', va='center',
        color='#0f172a', fontsize=24, fontweight='bold', family='sans-serif')
ax.text(50, 93.2, "MediMate-AI: Object-Oriented Domain Model, Clinical Classes & Core Methods",
        ha='center', va='center', color='#0284c7', fontsize=12.5, fontweight='bold', family='sans-serif')

# Helper function to draw standard 3-compartment UML Class Boxes
def draw_uml_class(ax, x, y, w, h, class_name, attributes, methods, header_bg='#0284c7', is_abstract=False):
    # Outer box
    box = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.2",
                                facecolor='#ffffff', edgecolor='#334155', linewidth=1.8)
    ax.add_patch(box)
    
    # 1. Header Compartment
    header_h = 3.6
    header = patches.FancyBboxPatch((x, y + h - header_h), w, header_h, boxstyle="round,pad=0.2",
                                    facecolor=header_bg, edgecolor='#334155', linewidth=1.8)
    ax.add_patch(header)
    
    title_text = f"«abstract»\n{class_name}" if is_abstract else class_name
    ax.text(x + w/2, y + h - header_h/2, title_text, ha='center', va='center',
            color='white', fontsize=11.5, fontweight='bold', family='sans-serif')
    
    # 2. Attributes Compartment
    attr_count = len(attributes)
    attr_h = attr_count * 2.1 + 1.0
    attr_y = y + h - header_h - 1.2
    
    for idx, attr in enumerate(attributes):
        ax.text(x + 1.2, attr_y - (idx * 2.1), attr, ha='left', va='center',
                color='#1e293b', fontsize=9.2, family='monospace')
        
    # Divider between attributes and methods
    sep_y = y + h - header_h - attr_h - 0.5
    ax.plot([x, x + w], [sep_y, sep_y], color='#94a3b8', linewidth=1.2)
    
    # 3. Methods Compartment
    meth_y = sep_y - 1.4
    for idx, meth in enumerate(methods):
        ax.text(x + 1.2, meth_y - (idx * 2.1), meth, ha='left', va='center',
                color='#0369a1', fontsize=9.2, family='monospace', fontweight='bold')

# ==============================================================================
# ROW 1: USER HIERARCHY (Top Row)
# ==============================================================================

# 1. Base Class: User (Center Top)
draw_uml_class(ax, 38.0, 68.0, 24.0, 20.0, "User (Base Model)",
               ["+ uid: String [PK]",
                "+ name: String",
                "+ email: String",
                "+ role: RoleType",
                "+ is_active: Boolean"],
               ["+ register(): Boolean",
                "+ authenticate(): JWTToken",
                "+ updateProfile(): Boolean"],
               header_bg='#1e293b')

# 2. Subclass: Patient (Left Top)
draw_uml_class(ax, 5.0, 68.0, 26.0, 20.0, "Patient",
               ["+ patient_id: String [FK]",
                "+ trauma_type: String",
                "+ days_post_accident: Int",
                "+ current_vas: Float (0-10)",
                "+ recovery_status: String"],
               ["+ logVASTelemetry(): Boolean",
                "+ consultPreethiAI(): String",
                "+ joinWebRTCSession(): Void"],
               header_bg='#0369a1')

# 3. Subclass: Physiotherapist (Right Top)
draw_uml_class(ax, 69.0, 68.0, 26.0, 20.0, "Physiotherapist",
               ["+ physio_id: String [FK]",
                "+ license_no: String",
                "+ specialization: String",
                "+ assigned_patients: List",
                "+ clinical_rating: Float"],
               ["+ reviewRecoveryCohort(): List",
                "+ forecastPrognosis(): Float",
                "+ dispatchPrescription(): Void"],
               header_bg='#0f766e')

# Inheritance Arrows (Patient -> User and Physio -> User)
ax.annotate('', xy=(38.0, 78.0), xytext=(31.0, 78.0),
            arrowprops=dict(arrowstyle="->", color='#0f172a', lw=2.0))
ax.text(34.5, 79.5, "«extends»", ha='center', va='center', fontsize=9, color='#475569', fontweight='bold')

ax.annotate('', xy=(62.0, 78.0), xytext=(69.0, 78.0),
            arrowprops=dict(arrowstyle="->", color='#0f172a', lw=2.0))
ax.text(65.5, 79.5, "«extends»", ha='center', va='center', fontsize=9, color='#475569', fontweight='bold')

# ==============================================================================
# ROW 2: CORE CLINICAL & AI DOMAIN CLASSES (Bottom Row)
# ==============================================================================

# 4. PreethiAIEngine (Bottom Left)
draw_uml_class(ax, 5.0, 37.0, 26.0, 21.0, "PreethiAIEngine",
               ["+ protocols_count: Int = 105",
                "+ vectorizer: TfidfVectorizer",
                "+ classifier: LinearSVC",
                "+ accuracy: Float = 0.968",
                "+ red_flag_recall: Float = 1.0"],
               ["+ sublinearTransform(): Matrix",
                "+ classifyTriageIntent(): String",
                "+ evaluateThermalProtocol(): Void",
                "+ triggerEmergencyER(): Alert"],
               header_bg='#0284c7')

# 5. RecoveryPrognosisRegressor (Bottom Center)
draw_uml_class(ax, 37.0, 37.0, 26.0, 21.0, "RecoveryPrognosisModel",
               ["+ n_estimators: Int = 100",
                "+ max_depth: Int = 12",
                "+ r2_score: Float = 0.941",
                "+ mae_days: Float = 2.14",
                "+ plateau_threshold: Float = 0.65"],
               ["+ extractTelemetryVector(): Array",
                "+ predictRecoveryDays(): Float",
                "+ computeChronicScore(): Float",
                "+ evaluateFeatureGini(): Dict"],
               header_bg='#059669')

# 6. WebRTCTeleRehab (Bottom Right)
draw_uml_class(ax, 69.0, 37.0, 26.0, 21.0, "WebRTCTeleRehabSession",
               ["+ room_id: String [PK]",
                "+ sdp_offer: Dict",
                "+ ice_candidates: List",
                "+ encryption: String = DTLS/SRTP",
                "+ repetition_timer: Int"],
               ["+ generateRoomCode(): String",
                "+ exchangeSDPOfferAnswer(): Void",
                "+ transmitLiveTelemetry(): Void",
                "+ endConsultation(): Log"],
               header_bg='#2563eb')

# ==============================================================================
# ROW 3: REHAB PRESCRIPTION & CLINICAL AUDIT (Very Bottom)
# ==============================================================================
draw_uml_class(ax, 20.0, 7.0, 28.0, 20.0, "RehabPrescription",
               ["+ prescription_id: String [PK]",
                "+ patient_id: String [FK]",
                "+ physio_id: String [FK]",
                "+ exercise_protocols: List<String>",
                "+ hold_duration_sec: Int",
                "+ daily_adherence_rate: Float"],
               ["+ assignIsometricExercise(): Void",
                "+ verifyPatientCompliance(): Float",
                "+ exportDigitalSummary(): PDF"],
               header_bg='#0d9488')

draw_uml_class(ax, 52.0, 7.0, 28.0, 20.0, "ClinicalTelemetryRecord",
               ["+ record_id: String [PK]",
                "+ patient_id: String [FK]",
                "+ timestamp: DateTime",
                "+ vas_pain_score: Float (0-10)",
                "+ joint_rom_deficit: Float",
                "+ swelling_grade: String"],
               ["+ recordDailyPain(): Boolean",
                "+ generateLongitudinalCurve(): Plot",
                "+ triggerPlateauWarning(): Void"],
               header_bg='#6366f1')

# Association Lines
# Patient connects to PreethiAI
ax.annotate('', xy=(18.0, 58.0), xytext=(18.0, 68.0),
            arrowprops=dict(arrowstyle="->", color='#0284c7', lw=1.8))
ax.text(19.0, 63.0, "1..* consults", fontsize=8.5, color='#0284c7', fontweight='bold')

# Physio connects to ML Regressor
ax.annotate('', xy=(50.0, 58.0), xytext=(72.0, 68.0),
            arrowprops=dict(arrowstyle="->", color='#059669', lw=1.8))
ax.text(62.0, 61.5, "1..* evaluates", fontsize=8.5, color='#059669', fontweight='bold')

# Patient & Physio connect to WebRTC
ax.annotate('', xy=(82.0, 58.0), xytext=(82.0, 68.0),
            arrowprops=dict(arrowstyle="<->", color='#2563eb', lw=1.8))
ax.text(83.0, 63.0, "1..1 video p2p", fontsize=8.5, color='#2563eb', fontweight='bold')

# Save outputs
dest_path = r"c:\Users\DELL\Documents\MediMate-AI\frontend\report_diagrams\uml_class_diagram.png"
fig_dest = r"c:\Users\DELL\Documents\MediMate-AI\frontend\report_diagrams\medimate_class_diagram.png"
art_dest = r"C:\Users\DELL\.gemini\antigravity\brain\4a9ee622-b1af-4b4c-9362-e46c9e06f79e\uml_class_diagram.png"
art_fig = r"C:\Users\DELL\.gemini\antigravity\brain\4a9ee622-b1af-4b4c-9362-e46c9e06f79e\medimate_class_diagram.png"

plt.savefig(dest_path, format='png', dpi=300, bbox_inches='tight', facecolor='#ffffff')
plt.savefig(fig_dest, format='png', dpi=300, bbox_inches='tight', facecolor='#ffffff')
plt.close(fig)

shutil.copy(dest_path, art_dest)
shutil.copy(dest_path, art_fig)

print(f"SUCCESS: UML Class Diagram generated! Size: {os.path.getsize(dest_path)} bytes")
