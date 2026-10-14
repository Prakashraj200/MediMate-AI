import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Setup figure with clean 16:9 presentation aspect ratio
fig, ax = plt.subplots(figsize=(14, 8.5), dpi=300)
fig.patch.set_facecolor('#f8fafc')
ax.set_facecolor('#f8fafc')
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

# Title Box
title_box = patches.FancyBboxPatch((5, 91), 90, 7.5, boxstyle="round,pad=0.3",
                                  facecolor='#1e3a8a', edgecolor='none')
ax.add_patch(title_box)
ax.text(50, 94.75, "MEDIMATE-AI: SYSTEM ARCHITECTURE", ha='center', va='center',
        color='white', fontsize=18, fontweight='bold', family='sans-serif')

# ================= TIER 1: CLIENT PRESENTATION LAYER =================
tier1_bg = patches.FancyBboxPatch((5, 68), 90, 20, boxstyle="round,pad=0.5",
                                 facecolor='white', edgecolor='#cbd5e1', linewidth=1.5)
ax.add_patch(tier1_bg)

tier1_tag = patches.FancyBboxPatch((7, 85), 32, 3.2, boxstyle="round,pad=0.2",
                                  facecolor='#0284c7', edgecolor='none')
ax.add_patch(tier1_tag)
ax.text(23, 86.6, "TIER 1: USER PRESENTATION LAYER", ha='center', va='center',
        color='white', fontsize=10, fontweight='bold')

# 5 User Portals
portals = [
    ("Patient Portal", "Vitals, Triage & Booking", 7),
    ("Doctor Portal", "EHR & e-Prescriptions", 25),
    ("Laboratory Portal", "Specimens & Lab Reports", 43),
    ("Pharmacy Portal", "Dispensing & Inventory", 61),
    ("Admin Portal", "Hospital Analytics & Staff", 79)
]

for title, sub, x in portals:
    box = patches.FancyBboxPatch((x, 70.5), 14, 12, boxstyle="round,pad=0.3",
                                 facecolor='#eff6ff', edgecolor='#93c5fd', linewidth=1.2)
    ax.add_patch(box)
    ax.text(x + 7, 78, title, ha='center', va='center', color='#1e3a8a', fontsize=10.5, fontweight='bold')
    ax.text(x + 7, 73.5, sub, ha='center', va='center', color='#475569', fontsize=8)

# Bidirectional Connector Tier 1 <-> Tier 2
ax.annotate('', xy=(50, 64), xytext=(50, 68),
            arrowprops=dict(arrowstyle="<->", color='#0284c7', lw=2.5, mutation_scale=15))
ax.text(55, 66, "HTTP / REST (JSON)", ha='left', va='center', color='#0369a1', fontsize=9.5, fontweight='bold')

# ================= TIER 2: APPLICATION & AI ENGINE =================
tier2_bg = patches.FancyBboxPatch((5, 36), 90, 26, boxstyle="round,pad=0.5",
                                 facecolor='white', edgecolor='#cbd5e1', linewidth=1.5)
ax.add_patch(tier2_bg)

tier2_tag = patches.FancyBboxPatch((7, 58.8), 35, 3.2, boxstyle="round,pad=0.2",
                                  facecolor='#0284c7', edgecolor='none')
ax.add_patch(tier2_tag)
ax.text(24.5, 60.4, "TIER 2: APPLICATION & AI ENGINE (FLASK)", ha='center', va='center',
        color='white', fontsize=10, fontweight='bold')

# Flask REST Server Box
b1 = patches.FancyBboxPatch((7.5, 38.5), 26.5, 18, boxstyle="round,pad=0.3",
                            facecolor='#f0fdf4', edgecolor='#86efac', linewidth=1.2)
ax.add_patch(b1)
ax.text(20.75, 52, "Flask REST Gateway", ha='center', va='center', color='#15803d', fontsize=12, fontweight='bold')
ax.text(20.75, 47, "• 15 Modular Blueprints\n• Route Security & CORS\n• WSGI Microframework", ha='center', va='center', color='#334155', fontsize=8.5)

# Preethi AI Box
b2 = patches.FancyBboxPatch((36.5, 38.5), 27, 18, boxstyle="round,pad=0.3",
                            facecolor='#fefce8', edgecolor='#fde047', linewidth=1.2)
ax.add_patch(b2)
ax.text(50, 52, "Preethi AI Engine", ha='center', va='center', color='#a16207', fontsize=12, fontweight='bold')
ax.text(50, 47, "• Clinical Symptom NLP\n• Emergency Keyword Filter\n• Specialist Routing", ha='center', va='center', color='#334155', fontsize=8.5)
ax.text(50, 41, "🚨 Instant 108/ER Alert", ha='center', va='center', color='#dc2626', fontsize=8.5, fontweight='bold')

# ML Classifier Box
b3 = patches.FancyBboxPatch((66, 38.5), 26.5, 18, boxstyle="round,pad=0.3",
                            facecolor='#faf5ff', edgecolor='#d8b4fe', linewidth=1.2)
ax.add_patch(b3)
ax.text(79.25, 52, "ML Risk Classifier", ha='center', va='center', color='#7e22ce', fontsize=12, fontweight='bold')
ax.text(79.25, 47, "• Random Forest (100 Trees)\n• Vitals Telemetry (BP/Sugar/HR)\n• Low / Mod / High Risk Tiers", ha='center', va='center', color='#334155', fontsize=8.5)

# Bidirectional Connector Tier 2 <-> Tier 3
ax.annotate('', xy=(50, 32), xytext=(50, 36),
            arrowprops=dict(arrowstyle="<->", color='#0284c7', lw=2.5, mutation_scale=15))
ax.text(55, 34, "Read / Write Sync", ha='left', va='center', color='#0369a1', fontsize=9.5, fontweight='bold')

# ================= TIER 3: DATA PERSISTENCE & SECURITY =================
tier3_bg = patches.FancyBboxPatch((5, 8), 90, 22, boxstyle="round,pad=0.5",
                                 facecolor='white', edgecolor='#cbd5e1', linewidth=1.5)
ax.add_patch(tier3_bg)

tier3_tag = patches.FancyBboxPatch((7, 26.8), 35, 3.2, boxstyle="round,pad=0.2",
                                  facecolor='#0284c7', edgecolor='none')
ax.add_patch(tier3_tag)
ax.text(24.5, 28.4, "TIER 3: PERSISTENCE & CLOUD STORAGE", ha='center', va='center',
        color='white', fontsize=10, fontweight='bold')

# Firebase Auth Box
db1 = patches.FancyBboxPatch((10, 11), 37, 13.5, boxstyle="round,pad=0.3",
                             facecolor='#eff6ff', edgecolor='#93c5fd', linewidth=1.2)
ax.add_patch(db1)
ax.text(28.5, 20.5, "Firebase Authentication", ha='center', va='center', color='#1e3a8a', fontsize=12, fontweight='bold')
ax.text(28.5, 15, "• Role-Based Access Control (RBAC)\n• Secure JWT RS256 Tokens", ha='center', va='center', color='#475569', fontsize=9)

# Cloud Firestore Box
db2 = patches.FancyBboxPatch((53, 11), 37, 13.5, boxstyle="round,pad=0.3",
                             facecolor='#eff6ff', edgecolor='#93c5fd', linewidth=1.2)
ax.add_patch(db2)
ax.text(71.5, 20.5, "Google Cloud Firestore", ha='center', va='center', color='#1e3a8a', fontsize=12, fontweight='bold')
ax.text(71.5, 15, "• NoSQL Real-Time Database Collections\n• EHR, Prescriptions, Labs & Vitals Logs", ha='center', va='center', color='#475569', fontsize=9)

plt.tight_layout()
output_path = r"c:\Users\DELL\Documents\MediMate-AI\medimate_architecture_diagram.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print("Architecture Diagram successfully saved as high-res PNG at:", output_path)
