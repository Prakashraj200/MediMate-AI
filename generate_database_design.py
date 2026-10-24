import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 16:9 widescreen presentation layout
fig, ax = plt.subplots(figsize=(16, 9.5), dpi=300)
fig.patch.set_facecolor('#ffffff')
ax.set_facecolor('#ffffff')
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

# Slide Top Title
ax.text(50, 96.5, "DATABASE DESIGN", ha='center', va='center',
        color='#0f172a', fontsize=22, fontweight='bold', family='sans-serif')
ax.text(50, 93.2, "Entity-Relationship (ER) Schema - Google Cloud Firestore NoSQL Collections (3NF Normalized)",
        ha='center', va='center', color='#0284c7', fontsize=11, fontweight='bold', family='sans-serif')


def draw_table(ax, x, y, w, h, table_name, fields, header_color='#1e3a8a'):
    # Outer container
    box = patches.FancyBboxPatch((x, y), w, h, boxstyle="square,pad=0",
                                facecolor='#ffffff', edgecolor='#64748b', linewidth=1.4)
    ax.add_patch(box)
    
    # Table Header
    header_h = h * 0.22
    header = patches.Rectangle((x, y + h - header_h), w, header_h,
                               facecolor=header_color, edgecolor='#64748b', linewidth=1.4)
    ax.add_patch(header)
    ax.text(x + w / 2, y + h - (header_h / 2), table_name, ha='center', va='center',
            color='white', fontsize=9.2, fontweight='bold', family='sans-serif')
    
    # Fields
    for i, (fname, ftype, is_key) in enumerate(fields):
        fy = y + h - header_h - 1.2 - (i * 2.2)
        if fy < y:
            break
        # Key indicator badge
        if is_key == "PK":
            ax.text(x + 0.8, fy, "PK", color='#b45309', fontsize=7, fontweight='bold', family='sans-serif')
        elif is_key == "FK":
            ax.text(x + 0.8, fy, "FK", color='#0284c7', fontsize=7, fontweight='bold', family='sans-serif')
        else:
            ax.text(x + 1.2, fy, "•", color='#94a3b8', fontsize=7)
            
        ax.text(x + 3.2, fy, fname, color='#1e293b', fontsize=7.2, fontweight='bold', family='sans-serif')
        ax.text(x + w - 0.8, fy, ftype, color='#64748b', fontsize=6.8, ha='right', family='sans-serif')


# ================= ROW 1: PRIMARY ENTITIES (Y = 68 to 89) =================
# 1. users
draw_table(ax, 3, 68, 20, 21, "users (Collection)", [
    ("uid", "string", "PK"),
    ("name", "string", ""),
    ("email", "string", ""),
    ("role", "string", ""),
    ("phone", "string", ""),
    ("is_active", "boolean", ""),
    ("created_at", "timestamp", "")
], header_color='#1e3a8a')

# 2. patients
draw_table(ax, 28, 68, 21, 21, "patients (Collection)", [
    ("id", "string", "PK"),
    ("user_id", "string", "FK"),
    ("mrn", "string", ""),
    ("date_of_birth", "date", ""),
    ("blood_group", "string", ""),
    ("allergies", "array", ""),
    ("chronic_conditions", "array", "")
], header_color='#0284c7')

# 3. doctors
draw_table(ax, 54, 68, 20, 21, "doctors (Collection)", [
    ("id", "string", "PK"),
    ("user_id", "string", "FK"),
    ("license_number", "string", ""),
    ("specialty", "string", ""),
    ("department_id", "string", "FK"),
    ("consultation_fee", "number", ""),
    ("experience_years", "number", "")
], header_color='#0284c7')

# 4. departments
draw_table(ax, 78, 68, 19, 21, "departments", [
    ("id", "string", "PK"),
    ("name", "string", ""),
    ("code", "string", ""),
    ("head_doctor_id", "string", "FK"),
    ("description", "string", ""),
    ("active_staff", "number", "")
], header_color='#1e3a8a')


# ================= ROW 2: CLINICAL TRANSACTIONS (Y = 36 to 57) =================
# 5. appointments
draw_table(ax, 3, 36, 21, 21, "appointments", [
    ("id", "string", "PK"),
    ("patient_id", "string", "FK"),
    ("doctor_id", "string", "FK"),
    ("date", "date", ""),
    ("time", "string", ""),
    ("mode", "string", ""),
    ("reason", "string", ""),
    ("status", "string", "")
], header_color='#0d9488')

# 6. prescriptions
draw_table(ax, 28, 36, 21, 21, "prescriptions", [
    ("id", "string", "PK"),
    ("rx_number", "string", ""),
    ("patient_id", "string", "FK"),
    ("doctor_id", "string", "FK"),
    ("medications", "array", ""),
    ("digital_signature", "string (SHA256)", ""),
    ("status", "string", "")
], header_color='#0d9488')

# 7. lab_tests
draw_table(ax, 54, 36, 20, 21, "lab_tests", [
    ("id", "string", "PK"),
    ("test_id", "string", ""),
    ("patient_id", "string", "FK"),
    ("doctor_id", "string", "FK"),
    ("barcode", "string", ""),
    ("test_name", "string", ""),
    ("status", "string", "")
], header_color='#0d9488')

# 8. vitals
draw_table(ax, 78, 36, 19, 21, "vitals (Telemetry)", [
    ("id", "string", "PK"),
    ("patient_id", "string", "FK"),
    ("systolic", "number", ""),
    ("diastolic", "number", ""),
    ("heart_rate", "number", ""),
    ("blood_glucose", "number", ""),
    ("risk_level", "number [0,1,2]", "")
], header_color='#7c3aed')


# ================= ROW 3: PHARMACY & INVENTORY (Y = 11 to 28) =================
# 9. medicines
draw_table(ax, 28, 11, 46, 17, "medicines (Dispensary Stock & Formulary)", [
    ("id [PK]", "string", "PK"),
    ("batch_code", "string", ""),
    ("name", "string", ""),
    ("generic_name", "string", ""),
    ("category", "string", ""),
    ("stock_quantity", "number", ""),
    ("expiry_date", "date", "")
], header_color='#b45309')


# ================= RELATIONSHIP CONNECTORS =================
# users -> patients (1 to 1)
ax.annotate('', xy=(28, 78.5), xytext=(23, 78.5),
            arrowprops=dict(arrowstyle="->", color='#0284c7', lw=1.5))
ax.text(25.5, 80, "1 : 1", ha='center', fontsize=7.5, color='#0284c7', fontweight='bold')

# users -> doctors (1 to 1) - top curve
ax.plot([13, 13, 64, 64], [89, 91.5, 91.5, 89], color='#0284c7', lw=1.2)
ax.text(38.5, 92, "1 : 1 identifies doctor profile", ha='center', fontsize=7, color='#0284c7', fontweight='bold')

# departments -> doctors (1 to N)
ax.annotate('', xy=(74, 78.5), xytext=(78, 78.5),
            arrowprops=dict(arrowstyle="->", color='#1e3a8a', lw=1.5))
ax.text(76, 80, "1 : N", ha='center', fontsize=7.5, color='#1e3a8a', fontweight='bold')

# patients -> appointments (1 to N)
ax.annotate('', xy=(13.5, 57), xytext=(32, 68),
            arrowprops=dict(arrowstyle="->", color='#0d9488', lw=1.3))
ax.text(18, 63.5, "1 : N books", fontsize=7.2, color='#0d9488', fontweight='bold',
        bbox=dict(boxstyle="round,pad=0.15", facecolor='#ffffff', edgecolor='#cbd5e1'))

# doctors -> appointments (1 to N)
ax.annotate('', xy=(24, 46.5), xytext=(54, 68),
            arrowprops=dict(arrowstyle="->", color='#0d9488', lw=1.3))
ax.text(38, 59, "1 : N conducts", fontsize=7.2, color='#0d9488', fontweight='bold',
        bbox=dict(boxstyle="round,pad=0.15", facecolor='#ffffff', edgecolor='#cbd5e1'))

# patients -> prescriptions (1 to N)
ax.annotate('', xy=(34, 57), xytext=(34, 68),
            arrowprops=dict(arrowstyle="->", color='#0d9488', lw=1.4))
ax.text(35, 62.5, "1 : N receives", fontsize=7.2, color='#0d9488', fontweight='bold',
        bbox=dict(boxstyle="round,pad=0.15", facecolor='#ffffff', edgecolor='#cbd5e1'))

# doctors -> prescriptions (1 to N)
ax.annotate('', xy=(45, 57), xytext=(56, 68),
            arrowprops=dict(arrowstyle="->", color='#0d9488', lw=1.3))
ax.text(51.5, 62.5, "1 : N authors", fontsize=7.2, color='#0d9488', fontweight='bold',
        bbox=dict(boxstyle="round,pad=0.15", facecolor='#ffffff', edgecolor='#cbd5e1'))

# patients -> lab_tests (1 to N)
ax.annotate('', xy=(64, 57), xytext=(45, 68),
            arrowprops=dict(arrowstyle="->", color='#0d9488', lw=1.3))
ax.text(57, 62.5, "1 : N undergoes", fontsize=7.2, color='#0d9488', fontweight='bold',
        bbox=dict(boxstyle="round,pad=0.15", facecolor='#ffffff', edgecolor='#cbd5e1'))

# patients -> vitals (1 to N)
ax.plot([49, 49, 87.5, 87.5], [68, 60, 60, 57], color='#7c3aed', lw=1.3)
ax.text(68, 60.5, "1 : N logs vitals", ha='center', fontsize=7.2, color='#7c3aed', fontweight='bold',
        bbox=dict(boxstyle="round,pad=0.15", facecolor='#ffffff', edgecolor='#cbd5e1'))

# prescriptions -> medicines (N to M dispenses)
ax.annotate('', xy=(42, 28), xytext=(38.5, 36),
            arrowprops=dict(arrowstyle="->", color='#b45309', lw=1.4))
ax.text(35, 31.5, "N : M dispenses", fontsize=7.5, color='#b45309', fontweight='bold',
        bbox=dict(boxstyle="round,pad=0.15", facecolor='#ffffff', edgecolor='#cbd5e1'))


# ================= BOTTOM NOTE BOXES =================
# Left Box: Normalization Highlights
note_l = patches.FancyBboxPatch((3, 11), 22, 17, boxstyle="round,pad=0.3",
                               facecolor='#f0fdf4', edgecolor='#86efac', linewidth=1.2)
ax.add_patch(note_l)
ax.text(4, 25.5, "Normalization Features", color='#15803d', fontsize=8.5, fontweight='bold')
ax.text(4, 22.5, "• 1NF: Atomic attributes & unique IDs", color='#1e293b', fontsize=7)
ax.text(4, 20, "• 2NF: No partial key dependency", color='#1e293b', fontsize=7)
ax.text(4, 17.5, "• 3NF: No transitive dependency", color='#1e293b', fontsize=7)
ax.text(4, 15, "• NoSQL Subcollections in Firestore", color='#1e293b', fontsize=7)
ax.text(4, 12.5, "• Zero data redundancy across EHR", color='#1e293b', fontsize=7)

# Right Box: Security & Integrity Notes
note_r = patches.FancyBboxPatch((76, 11), 21, 17, boxstyle="round,pad=0.3",
                               facecolor='#eff6ff', edgecolor='#93c5fd', linewidth=1.2)
ax.add_patch(note_r)
ax.text(77, 25.5, "Integrity & Security", color='#1d4ed8', fontsize=8.5, fontweight='bold')
ax.text(77, 22.5, "• SHA-256 e-Rx Cryptographic Stamp", color='#1e293b', fontsize=7)
ax.text(77, 20, "• Role-Based Security Rules", color='#1e293b', fontsize=7)
ax.text(77, 17.5, "• Auto Stock Decrement Triggers", color='#1e293b', fontsize=7)
ax.text(77, 15, "• Specimen Barcode Accessioning", color='#1e293b', fontsize=7)
ax.text(77, 12.5, "• HIPAA Compliant Audit Trails", color='#1e293b', fontsize=7)

# Slide Footer
ax.text(3, 3, "15-10-2026", color='#94a3b8', fontsize=8)
ax.text(50, 3, "MediMate AI", color='#94a3b8', fontsize=8, ha='center')
ax.text(97, 3, "18", color='#94a3b8', fontsize=8, ha='right')

plt.tight_layout()
output_path = r"c:\Users\DELL\Documents\MediMate-AI\medimate_database_design.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print("Successfully generated refined Database Design ER Diagram at:", output_path)
