import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Setup figure with 16:9 widescreen aspect ratio
fig, ax = plt.subplots(figsize=(15, 9.5), dpi=300)
fig.patch.set_facecolor('#f8fafc')
ax.set_facecolor('#f8fafc')
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

# Title Header Box
title_box = patches.FancyBboxPatch((5, 92), 90, 6.5, boxstyle="round,pad=0.3",
                                  facecolor='#1e3a8a', edgecolor='none')
ax.add_patch(title_box)
ax.text(50, 95.25, "MEDIMATE-AI: UML CLASS DIAGRAM", ha='center', va='center',
        color='white', fontsize=18, fontweight='bold', family='sans-serif')


def draw_class_box(ax, x, y, w, h, class_name, attributes, methods, bg_color='#ffffff', header_color='#1e3a8a'):
    # Outer box
    box = patches.FancyBboxPatch((x, y), w, h, boxstyle="square,pad=0",
                                facecolor=bg_color, edgecolor='#64748b', linewidth=1.5)
    ax.add_patch(box)
    
    # Header bar
    header_h = h * 0.22
    header = patches.Rectangle((x, y + h - header_h), w, header_h,
                               facecolor=header_color, edgecolor='#64748b', linewidth=1.5)
    ax.add_patch(header)
    ax.text(x + w / 2, y + h - (header_h / 2), class_name, ha='center', va='center',
            color='white', fontsize=10.5, fontweight='bold', family='sans-serif')
    
    # Attributes section
    attr_h = (h - header_h) * 0.52
    line_y = y + h - header_h - attr_h
    ax.plot([x, x + w], [line_y, line_y], color='#94a3b8', linewidth=1)
    
    attr_text = "\n".join(attributes)
    ax.text(x + 0.8, y + h - header_h - 1, attr_text, ha='left', va='top',
            color='#1e293b', fontsize=7.8, family='monospace')
    
    # Methods section
    meth_text = "\n".join(methods)
    ax.text(x + 0.8, line_y - 1, meth_text, ha='left', va='top',
            color='#0f172a', fontsize=7.8, family='monospace', fontweight='500')


# 1. Base Class: User (Top Center)
draw_class_box(ax, 38, 68, 24, 21, "User (Base Class)",
               ["+ String uid [PK]", "+ String name", "+ String email", "+ String role", "+ Boolean is_active"],
               ["+ register()", "+ login()", "+ updateProfile()"],
               header_color='#1e40af')

# 2. Derived Class: Patient (Left)
draw_class_box(ax, 6, 68, 25, 21, "Patient",
               ["+ String mrn [MRN-XXXX]", "+ String blood_group", "+ List<String> allergies", "+ List<String> chronic_diseases"],
               ["+ bookAppointment()", "+ chatPreethiAI()", "+ viewLabReports()"],
               header_color='#0284c7')

# 3. Derived Class: Doctor (Right)
draw_class_box(ax, 69, 68, 25, 21, "Doctor",
               ["+ String license_number", "+ String specialty", "+ String department_id", "+ Float consultation_fee"],
               ["+ conductConsultation()", "+ authorPrescription()", "+ orderLabTest()"],
               header_color='#0284c7')

# 4. Appointment (Mid Left)
draw_class_box(ax, 6, 38, 25, 23, "Appointment",
               ["+ String id [APT-XXXX]", "+ String patient_id [FK]", "+ String doctor_id [FK]", "+ Date date", "+ String status [confirmed]"],
               ["+ schedule()", "+ reschedule()", "+ cancel()"],
               header_color='#0d9488')

# 5. Prescription (Mid Center)
draw_class_box(ax, 37.5, 38, 25, 23, "Prescription",
               ["+ String rx_number [PK]", "+ String patient_id [FK]", "+ String doctor_id [FK]", "+ String digital_signature (SHA256)", "+ String status [dispensed]"],
               ["+ authorDigitalSignature()", "+ verifySignature()", "+ markDispensed()"],
               header_color='#0d9488')

# 6. LabTest (Mid Right)
draw_class_box(ax, 69, 38, 25, 23, "LabTest",
               ["+ String test_id [PK]", "+ String patient_id [FK]", "+ String barcode [BAR-XXXX]", "+ Dict analyte_results", "+ String status [certified]"],
               ["+ assignBarcode()", "+ recordAnalyte()", "+ certifyReport()"],
               header_color='#0d9488')

# 7. VitalsRecord (Bottom Left)
draw_class_box(ax, 16, 8, 28, 23, "VitalsRecord",
               ["+ String record_id", "+ String patient_id [FK]", "+ Float systolic_bp", "+ Float diastolic_bp", "+ Float blood_glucose", "+ Int risk_level [0, 1, 2]"],
               ["+ recordTelemetry()", "+ predictRiskLevel(RandomForest)", "+ triggerEmergencyAlert()"],
               header_color='#7c3aed')

# 8. Medicine / Inventory (Bottom Right)
draw_class_box(ax, 56, 8, 28, 23, "Medicine (Inventory)",
               ["+ String batch_code [PK]", "+ String name", "+ String generic_name", "+ Int stock_quantity", "+ Date expiry_date", "+ Int reorder_threshold"],
               ["+ updateStock()", "+ checkNearExpiry()", "+ decrementUponDispense()"],
               header_color='#b45309')

# ================= RELATIONSHIP ARROWS =================
# Inheritance: Patient -> User (Left to Center)
ax.annotate('', xy=(38, 78.5), xytext=(31, 78.5),
            arrowprops=dict(facecolor='white', edgecolor='#1e40af', lw=1.8, width=1.5, headwidth=9, headlength=9))
ax.text(34.5, 80, "is-a", ha='center', va='bottom', fontsize=8, color='#1e40af', fontweight='bold')

# Inheritance: Doctor -> User (Right to Center)
ax.annotate('', xy=(62, 78.5), xytext=(69, 78.5),
            arrowprops=dict(facecolor='white', edgecolor='#1e40af', lw=1.8, width=1.5, headwidth=9, headlength=9))
ax.text(65.5, 80, "is-a", ha='center', va='bottom', fontsize=8, color='#1e40af', fontweight='bold')

# Association: Patient -> Appointment (Vertical)
ax.annotate('', xy=(18.5, 61), xytext=(18.5, 68),
            arrowprops=dict(arrowstyle="->", color='#0f766e', lw=1.5))
ax.text(19.5, 64.5, "1 .. * books", fontsize=8, color='#0f766e', fontweight='bold')

# Association: Doctor -> Appointment (Diagonal)
ax.annotate('', xy=(31, 55), xytext=(69, 69),
            arrowprops=dict(arrowstyle="->", color='#0f766e', lw=1.5))
ax.text(50, 62, "1 .. * conducts", fontsize=8, color='#0f766e', fontweight='bold')

# Association: Doctor -> Prescription
ax.annotate('', xy=(50, 61), xytext=(72, 68),
            arrowprops=dict(arrowstyle="->", color='#0f766e', lw=1.5))
ax.text(61, 64.5, "1 .. * authors", fontsize=8, color='#0f766e', fontweight='bold')

# Association: Patient -> Prescription
ax.annotate('', xy=(42, 61), xytext=(28, 68),
            arrowprops=dict(arrowstyle="->", color='#0f766e', lw=1.5))
ax.text(32, 64.5, "1 .. * receives", fontsize=8, color='#0f766e', fontweight='bold')

# Association: Doctor -> LabTest
ax.annotate('', xy=(81.5, 61), xytext=(81.5, 68),
            arrowprops=dict(arrowstyle="->", color='#0f766e', lw=1.5))
ax.text(82.5, 64.5, "1 .. * orders", fontsize=8, color='#0f766e', fontweight='bold')

# Association: Patient -> VitalsRecord
ax.annotate('', xy=(25, 31), xytext=(18.5, 38),
            arrowprops=dict(arrowstyle="->", color='#7c3aed', lw=1.5))
ax.text(23, 34, "1 .. * tracks", fontsize=8, color='#7c3aed', fontweight='bold')

# Association: Prescription -> Medicine
ax.annotate('', xy=(66, 31), xytext=(55, 38),
            arrowprops=dict(arrowstyle="->", color='#b45309', lw=1.5))
ax.text(62, 34, "* .. * dispenses", fontsize=8, color='#b45309', fontweight='bold')

plt.tight_layout()
output_path = r"c:\Users\DELL\Documents\MediMate-AI\medimate_class_diagram.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print("Class Diagram successfully generated at:", output_path)
