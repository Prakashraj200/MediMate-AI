import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 16:9 widescreen presentation layout matching user's slide
fig, ax = plt.subplots(figsize=(16, 9.2), dpi=300)
fig.patch.set_facecolor('#ffffff')
ax.set_facecolor('#ffffff')
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

# Slide Top Title
ax.text(50, 96.2, "SYSTEM DESIGN", ha='center', va='center',
        color='#0f172a', fontsize=22, fontweight='bold', family='sans-serif')

# ================= MAIN CONTAINER: MODULE-SPECIFIC SEQUENCE FLOWS =================
main_box = patches.FancyBboxPatch((2, 33), 96, 58, boxstyle="round,pad=0.5",
                                 facecolor='#ffffff', edgecolor='#818cf8', linewidth=1.5)
ax.add_patch(main_box)

# Header Tag for Main Container
header_tag = patches.FancyBboxPatch((35, 88.5), 30, 3.2, boxstyle="round,pad=0.2",
                                   facecolor='#1e3a8a', edgecolor='none')
ax.add_patch(header_tag)
ax.text(50, 90.1, "Module-Specific Sequence Flows", ha='center', va='center',
        color='white', fontsize=11, fontweight='bold')

# The 5 Modules Column Specifications
modules = [
    {
        "title": "1. Appointment Flow",
        "header_bg": "#e0f2fe",
        "border": "#38bdf8",
        "x": 3.5, "w": 18,
        "parts": [("Patient", 5.5, "#dcfce7", "#22c55e"),
                  ("Frontend", 11.5, "#dcfce7", "#22c55e"),
                  ("Backend +\nFirestore", 18.5, "#ede9fe", "#8b5cf6")],
        "steps": [
            (5.5, 11.5, 74, "1. Book appointment", False, "#16a34a"),
            (11.5, 18.5, 62, "2. Save appointment\n    record", False, "#8b5cf6"),
            (18.5, 5.5, 48, "3. Confirmation\n    & status", True, "#16a34a")
        ],
        "bars": [(5.5, 48, 74, "#86efac"), (11.5, 62, 74, "#86efac"), (18.5, 48, 62, "#c4b5fd")]
    },
    {
        "title": "2. Prescription Flow",
        "header_bg": "#dcfce7",
        "border": "#4ade80",
        "x": 22.5, "w": 18,
        "parts": [("Doctor", 24.5, "#dcfce7", "#22c55e"),
                  ("Frontend", 30.5, "#dcfce7", "#22c55e"),
                  ("Backend +\nFirestore", 37.5, "#ede9fe", "#8b5cf6")],
        "steps": [
            (24.5, 30.5, 74, "1. Create prescription", False, "#0284c7"),
            (30.5, 37.5, 62, "2. Save prescription\n    & link to patient", False, "#8b5cf6"),
            (37.5, 24.5, 48, "3. Notify patient\n    & pharmacy", True, "#0284c7")
        ],
        "bars": [(24.5, 48, 74, "#7dd3fc"), (30.5, 62, 74, "#7dd3fc"), (37.5, 48, 62, "#c4b5fd")]
    },
    {
        "title": "3. Laboratory Flow",
        "header_bg": "#fef9c3",
        "border": "#facc15",
        "x": 41.5, "w": 18,
        "parts": [("Laboratory", 43.5, "#fef08a", "#eab308"),
                  ("Frontend", 49.5, "#dcfce7", "#22c55e"),
                  ("Backend +\nFirestore", 56.5, "#ede9fe", "#8b5cf6")],
        "steps": [
            (43.5, 49.5, 74, "1. Add test request", False, "#ca8a04"),
            (49.5, 56.5, 62, "2. Save test record", False, "#8b5cf6"),
            (56.5, 43.5, 48, "3. Update result\n    & notify doctor/patient", True, "#ca8a04")
        ],
        "bars": [(43.5, 48, 74, "#fde047"), (49.5, 62, 74, "#86efac"), (56.5, 48, 62, "#c4b5fd")]
    },
    {
        "title": "4. Pharmacy Flow",
        "header_bg": "#fee2e2",
        "border": "#f87171",
        "x": 60.5, "w": 18,
        "parts": [("Pharmacy", 62.5, "#fecaca", "#ef4444"),
                  ("Frontend", 68.5, "#dcfce7", "#22c55e"),
                  ("Backend +\nFirestore", 75.5, "#ede9fe", "#8b5cf6")],
        "steps": [
            (62.5, 68.5, 74, "1. View prescription", False, "#dc2626"),
            (68.5, 75.5, 62, "2. Check stock &\n    dispense medicine", False, "#8b5cf6"),
            (75.5, 62.5, 48, "3. Update stock\n    & status", True, "#dc2626")
        ],
        "bars": [(62.5, 48, 74, "#fca5a5"), (68.5, 62, 74, "#86efac"), (75.5, 48, 62, "#c4b5fd")]
    },
    {
        "title": "5. ML Model Flow",
        "header_bg": "#ede9fe",
        "border": "#a78bfa",
        "x": 79.5, "w": 17.5,
        "parts": [("Backend", 81.5, "#ede9fe", "#8b5cf6"),
                  ("Colab /\nTraining", 87.5, "#fef08a", "#eab308"),
                  ("Model API\n(Inference)", 94.5, "#dcfce7", "#22c55e")],
        "steps": [
            (81.5, 87.5, 76, "1. Train model\n    (with dataset)", False, "#7c3aed"),
            (87.5, 81.5, 68, "2. Save model\n    (export)", True, "#ca8a04"),
            (81.5, 94.5, 58, "3. Use model for\n    inference", False, "#7c3aed"),
            (94.5, 81.5, 46, "4. Return prediction\n    (or result)", True, "#16a34a")
        ],
        "bars": [(81.5, 46, 76, "#c4b5fd"), (87.5, 68, 76, "#fde047"), (94.5, 46, 58, "#86efac")]
    }
]

# Draw each of the 5 Columns
for m in modules:
    # Outer Column Box
    col_box = patches.FancyBboxPatch((m["x"], 35), m["w"], 51, boxstyle="round,pad=0.3",
                                    facecolor='#ffffff', edgecolor=m["border"], linewidth=1.2)
    ax.add_patch(col_box)
    
    # Title Tag
    t_tag = patches.FancyBboxPatch((m["x"] + 1, 82), m["w"] - 2, 3.2, boxstyle="round,pad=0.2",
                                  facecolor=m["header_bg"], edgecolor=m["border"], linewidth=1)
    ax.add_patch(t_tag)
    ax.text(m["x"] + m["w"]/2, 83.6, m["title"], ha='center', va='center',
            color='#0f172a', fontsize=8.5, fontweight='bold')
    
    # Participant boxes
    for p_name, px, p_bg, p_border in m["parts"]:
        p_box = patches.FancyBboxPatch((px - 2.3, 76.8), 4.6, 4.2, boxstyle="round,pad=0.2",
                                      facecolor=p_bg, edgecolor=p_border, linewidth=1)
        ax.add_patch(p_box)
        ax.text(px, 78.9, p_name, ha='center', va='center', color='#0f172a', fontsize=6.8, fontweight='bold')
        # Dashed Lifeline
        ax.plot([px, px], [37, 76.8], color='#cbd5e1', linestyle='--', linewidth=1, zorder=1)
    
    # Activation Bars
    for bx, by1, by2, b_col in m["bars"]:
        act_bar = patches.Rectangle((bx - 0.4, by1), 0.8, by2 - by1,
                                    facecolor=b_col, edgecolor='#64748b', linewidth=0.8, zorder=2)
        ax.add_patch(act_bar)
    
    # Arrows & Steps
    for x1, x2, y, label, is_dash, a_col in m["steps"]:
        style = "--" if is_dash else "-"
        # Small offset so arrow touches edge of bar
        x1_adj = x1 + 0.4 if x2 > x1 else x1 - 0.4
        x2_adj = x2 - 0.4 if x2 > x1 else x2 + 0.4
        ax.annotate('', xy=(x2_adj, y), xytext=(x1_adj, y),
                    arrowprops=dict(arrowstyle="->", color=a_col, lw=1.2, linestyle=style), zorder=3)
        mid_x = (x1 + x2) / 2
        ax.text(mid_x, y + 1.2, label, ha='center', va='bottom',
                color='#0f172a', fontsize=6.5, fontweight='bold', family='sans-serif', zorder=4)


# ================= BOTTOM SECTION: TWO NOTES BOXES =================
# Left Box: Key Components
box_l = patches.FancyBboxPatch((2, 5.5), 46.5, 25.5, boxstyle="round,pad=0.4",
                              facecolor='#f0fdf4', edgecolor='#86efac', linewidth=1.2)
ax.add_patch(box_l)
ax.text(3.5, 28.5, "Key Components", color='#15803d', fontsize=11, fontweight='bold')

comp_texts = [
    "• Frontend: HTML, CSS, JavaScript (user interface & dashboards)",
    "• Backend: Python (API & business logic)",
    "• Authentication: Firebase Authentication (email/password)",
    "• Database: Cloud Firestore (NoSQL)",
    "• AI: Preethi AI (chatbot / support)",
    "• ML: Trained model in Google Colab and integrated as API"
]
for i, line in enumerate(comp_texts):
    ax.text(3.5, 24.5 - (i * 3.4), line, color='#1e293b', fontsize=8.2, family='sans-serif')

# Right Box: Sequence Diagram Notes
box_r = patches.FancyBboxPatch((51.5, 5.5), 46.5, 25.5, boxstyle="round,pad=0.4",
                              facecolor='#eff6ff', edgecolor='#93c5fd', linewidth=1.2)
ax.add_patch(box_r)
ax.text(53, 28.5, "Sequence Diagram Notes", color='#1d4ed8', fontsize=11, fontweight='bold')

notes_texts = [
    "1. The user logs in using Firebase Authentication.",
    "2. The backend reads the user role from Firestore and routes to the correct dashboard.",
    "3. Each module (appointment, prescription, lab, pharmacy) interacts with the backend and Firestore.",
    "4. Preethi AI handles AI-based support with proper validation and safety checks.",
    "5. The ML model is trained in Google Colab and exposed as an API for inference.",
    "6. All data access is protected using Firebase Security Rules and role-based authorization."
]
for i, line in enumerate(notes_texts):
    ax.text(53, 24.5 - (i * 3.4), line, color='#1e293b', fontsize=8.2, family='sans-serif')

# Footer
ax.text(3, 2, "15-10-2026", color='#94a3b8', fontsize=8)
ax.text(50, 2, "MediMate AI", color='#94a3b8', fontsize=8, ha='center')
ax.text(97, 2, "17", color='#94a3b8', fontsize=8, ha='right')

plt.tight_layout()
output_path = r"c:\Users\DELL\Documents\MediMate-AI\medimate_module_sequence_diagram.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print("Successfully generated exact Module-Specific Sequence Diagram at:", output_path)
