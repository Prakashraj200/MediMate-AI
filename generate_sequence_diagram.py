import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 16:9 widescreen presentation layout
fig, ax = plt.subplots(figsize=(16, 9.5), dpi=300)
fig.patch.set_facecolor('#ffffff')
ax.set_facecolor('#ffffff')
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

# Title Box
ax.text(50, 96.5, "MEDIMATE-AI: UML SEQUENCE DIAGRAM", ha='center', va='center',
        color='#0f172a', fontsize=21, fontweight='bold', family='sans-serif')
ax.text(50, 93.2, "End-to-End Clinical Triage, Doctor Consultation & Pharmacy Dispensation Workflow",
        ha='center', va='center', color='#0284c7', fontsize=11, fontweight='bold', family='sans-serif')

# Participants (Lifelines)
participants = [
    ("Patient", 9, '#eff6ff', '#3b82f6'),
    ("Preethi AI Engine", 25.5, '#fefce8', '#eab308'),
    ("Flask API Gateway", 42, '#f0fdf4', '#22c55e'),
    ("Doctor", 58.5, '#eff6ff', '#3b82f6'),
    ("Cloud Firestore", 75, '#faf5ff', '#a855f7'),
    ("Pharmacist", 91.5, '#fffbeb', '#f59e0b')
]

# Draw Lifelines & Header Boxes
for name, x, bg, border in participants:
    # Header Box
    box = patches.FancyBboxPatch((x - 6.5, 84.5), 13, 6, boxstyle="round,pad=0.2",
                                facecolor=bg, edgecolor=border, linewidth=1.5)
    ax.add_patch(box)
    ax.text(x, 87.5, name, ha='center', va='center', color='#0f172a', fontsize=9.5, fontweight='bold')
    
    # Vertical Dashed Lifeline
    ax.plot([x, x], [10, 84.5], color='#cbd5e1', linestyle='--', linewidth=1.2, zorder=1)
    
    # Bottom Box
    box_b = patches.FancyBboxPatch((x - 6.5, 5.5), 13, 4, boxstyle="round,pad=0.2",
                                  facecolor=bg, edgecolor=border, linewidth=1.5)
    ax.add_patch(box_b)
    ax.text(x, 7.5, name, ha='center', va='center', color='#0f172a', fontsize=8.5, fontweight='bold')


def draw_message(ax, x1, x2, y, num_label, is_dashed=False, color='#0284c7'):
    style = "--" if is_dashed else "-"
    ax.annotate('', xy=(x2, y), xytext=(x1, y),
                arrowprops=dict(arrowstyle="->", color=color, lw=1.5, linestyle=style))
    mid_x = (x1 + x2) / 2
    # Background pill for text readability
    ax.text(mid_x, y + 1.2, num_label, ha='center', va='center',
            color='#0f172a', fontsize=8.2, fontweight='bold', family='sans-serif',
            bbox=dict(boxstyle="round,pad=0.2", facecolor='#ffffff', edgecolor='#e2e8f0', alpha=0.9))


# Sequence Steps
steps = [
    (9, 25.5, 80, "1. Submits symptoms ('chest pain, shortness of breath')", False, '#0284c7'),
    (25.5, 25.5, 75, "2. Evaluates emergency keywords & rules", False, '#b45309'),  # Self call
    (25.5, 9, 71, "3. Returns Critical Emergency / Cardiologist Referral", True, '#dc2626'),
    (9, 42, 65, "4. POST /api/appointments (Book Consultation)", False, '#0284c7'),
    (42, 75, 60, "5. Stores appointment record (status: confirmed)", False, '#059669'),
    (75, 58.5, 55, "6. Real-time sync: Doctor Daily Consultation Queue", True, '#7c3aed'),
    (58.5, 42, 49, "7. Initiates WebRTC Video Consultation & Reviews EHR", False, '#0284c7'),
    (58.5, 42, 43, "8. Authors e-Prescription (Meds, Dosage, Frequency)", False, '#0284c7'),
    (42, 42, 38, "9. Calculates SHA-256 Tamper-Proof Digital Signature", False, '#059669'), # Self call
    (42, 75, 33, "10. Inserts signed prescription into Firestore", False, '#059669'),
    (75, 91.5, 28, "11. Real-time alert: Prescriptions Pending Queue", True, '#7c3aed'),
    (91.5, 42, 23, "12. PUT /api/prescriptions/dispense (Verify & Fill)", False, '#b45309'),
    (42, 75, 18, "13. Decrements inventory stock & logs audit trail", False, '#059669'),
    (42, 9, 13, "14. Notifies Patient with medication adherence schedule", True, '#0284c7')
]

for x1, x2, y, label, is_ret, col in steps:
    if x1 == x2:
        # Self call loop
        ax.annotate('', xy=(x1, y - 2.5), xytext=(x1 + 4, y),
                    arrowprops=dict(arrowstyle="->", color=col, lw=1.5, connectionstyle="arc3,rad=-0.5"))
        ax.plot([x1, x1 + 4], [y, y], color=col, lw=1.5)
        ax.text(x1 + 4.5, y - 1.2, label, ha='left', va='center',
                color='#0f172a', fontsize=8, fontweight='bold',
                bbox=dict(boxstyle="round,pad=0.2", facecolor='#ffffff', edgecolor='#e2e8f0'))
    else:
        draw_message(ax, x1, x2, y, label, is_dashed=is_ret, color=col)

plt.tight_layout()
output_path = r"c:\Users\DELL\Documents\MediMate-AI\medimate_sequence_diagram.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print("Successfully generated UML Sequence Diagram at:", output_path)
