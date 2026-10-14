import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Setup figure with 16:9 widescreen aspect ratio
fig, ax = plt.subplots(figsize=(16, 10), dpi=300)
fig.patch.set_facecolor('#f8fafc')
ax.set_facecolor('#f8fafc')
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

# Title Box
title_box = patches.FancyBboxPatch((5, 93), 90, 6, boxstyle="round,pad=0.3",
                                  facecolor='#1e3a8a', edgecolor='none')
ax.add_patch(title_box)
ax.text(50, 96, "MEDIMATE-AI: UML USE CASE DIAGRAM", ha='center', va='center',
        color='white', fontsize=18, fontweight='bold', family='sans-serif')

# System Boundary Rectangle
boundary = patches.FancyBboxPatch((20, 5), 60, 85, boxstyle="square,pad=0",
                                  facecolor='#ffffff', edgecolor='#0284c7', linewidth=2)
ax.add_patch(boundary)
ax.text(50, 87.5, "System Boundary: MediMate-AI Healthcare Platform", ha='center', va='center',
        color='#0369a1', fontsize=13, fontweight='bold', family='sans-serif')


def draw_actor(ax, x, y, name, color='#1e3a8a'):
    # Head
    head = patches.Circle((x, y + 3.2), 1.6, facecolor='#eff6ff', edgecolor=color, linewidth=2)
    ax.add_patch(head)
    # Body
    ax.plot([x, x], [y + 1.6, y - 2.2], color=color, linewidth=2)
    # Arms
    ax.plot([x - 2.5, x + 2.5], [y + 0.4, y + 0.4], color=color, linewidth=2)
    # Legs
    ax.plot([x, x - 2], [y - 2.2, y - 5.5], color=color, linewidth=2)
    ax.plot([x, x + 2], [y - 2.2, y - 5.5], color=color, linewidth=2)
    # Label Box
    tag = patches.FancyBboxPatch((x - 6, y - 9), 12, 2.8, boxstyle="round,pad=0.2",
                                 facecolor='#eff6ff', edgecolor=color, linewidth=1)
    ax.add_patch(tag)
    ax.text(x, y - 7.6, name, ha='center', va='center', color=color, fontsize=9.5, fontweight='bold')


# Actors Left Side
draw_actor(ax, 10, 75, "Patient", '#0369a1')
draw_actor(ax, 10, 45, "Doctor", '#0369a1')
draw_actor(ax, 10, 18, "Laboratory Tech", '#0369a1')

# Actors Right Side
draw_actor(ax, 90, 75, "Preethi AI Bot", '#b45309')
draw_actor(ax, 90, 45, "Pharmacist", '#0369a1')
draw_actor(ax, 90, 18, "Administrator", '#0369a1')


def draw_usecase(ax, x, y, w, h, text, bg_color='#f0fdf4', border_color='#22c55e'):
    ellipse = patches.Ellipse((x, y), w, h, facecolor=bg_color, edgecolor=border_color, linewidth=1.5)
    ax.add_patch(ellipse)
    ax.text(x, y, text, ha='center', va='center', color='#0f172a', fontsize=8.8, fontweight='bold', family='sans-serif')


# Use Cases inside Boundary (Center Column)
usecases = [
    (50, 81, 26, 4.8, "Register & Authenticate (RBAC)", '#eff6ff', '#3b82f6'),
    (36, 73, 24, 4.6, "Chat with Preethi AI Triage", '#fefce8', '#eab308'),
    (64, 73, 24, 4.6, "Trigger Emergency (108 Alert)", '#fef2f2', '#ef4444'),
    (36, 64, 25, 4.6, "Book / Reschedule Consultation", '#f0fdf4', '#22c55e'),
    (64, 64, 24, 4.6, "Conduct Video Consultation", '#f0fdf4', '#22c55e'),
    (36, 54, 25, 4.6, "Log Vitals (BP, Sugar, HR)", '#faf5ff', '#a855f7'),
    (64, 54, 24, 4.6, "Predict Risk Level (ML)", '#faf5ff', '#a855f7'),
    (50, 44, 26, 4.8, "Author e-Prescription (SHA-256)", '#ecfeff', '#06b6d4'),
    (36, 34, 24, 4.6, "Order Diagnostic Lab Test", '#f0fdf4', '#22c55e'),
    (64, 34, 25, 4.6, "Verify & Dispense Medicines", '#fffbeb', '#f59e0b'),
    (36, 24, 25, 4.6, "Barcode Accession & Test Entry", '#f0fdf4', '#22c55e'),
    (64, 24, 25, 4.6, "Pharmacy Stock & Expiry Alert", '#fffbeb', '#f59e0b'),
    (36, 14, 24, 4.6, "Download Lab Report (PDF)", '#f0fdf4', '#22c55e'),
    (64, 14, 25, 4.6, "Manage Staff Roles & Analytics", '#eff6ff', '#3b82f6')
]

for x, y, w, h, text, bg, border in usecases:
    draw_usecase(ax, x, y, w, h, text, bg, border)

# Associations: Patient
ax.plot([10, 37], [75, 81], color='#64748b', lw=1.2)   # Auth
ax.plot([10, 24], [75, 73], color='#64748b', lw=1.2)   # Preethi AI
ax.plot([10, 23.5], [75, 64], color='#64748b', lw=1.2) # Book
ax.plot([10, 23.5], [75, 54], color='#64748b', lw=1.2) # Vitals
ax.plot([10, 24], [75, 14], color='#64748b', lw=1.2)   # Download Lab

# Associations: Doctor
ax.plot([10, 37], [45, 81], color='#64748b', lw=1.2)   # Auth
ax.plot([10, 52], [45, 64], color='#64748b', lw=1.2)   # Video
ax.plot([10, 37], [45, 44], color='#64748b', lw=1.2)   # e-Rx
ax.plot([10, 24], [45, 34], color='#64748b', lw=1.2)   # Order Lab

# Associations: Lab Tech
ax.plot([10, 37], [18, 81], color='#64748b', lw=1.2)   # Auth
ax.plot([10, 23.5], [18, 24], color='#64748b', lw=1.2) # Barcode
ax.plot([10, 24], [18, 14], color='#64748b', lw=1.2)   # Publish Report

# Associations: Preethi AI Bot
ax.plot([90, 48], [75, 73], color='#b45309', lw=1.5)   # AI Triage
ax.plot([90, 76], [75, 73], color='#b45309', lw=1.5)   # Emergency Trigger
ax.plot([90, 76], [75, 54], color='#b45309', lw=1.5)   # ML Risk

# Associations: Pharmacist
ax.plot([90, 63], [45, 81], color='#64748b', lw=1.2)   # Auth
ax.plot([90, 63], [45, 44], color='#64748b', lw=1.2)   # Verify e-Rx
ax.plot([90, 76.5], [45, 34], color='#64748b', lw=1.2) # Dispense
ax.plot([90, 76.5], [45, 24], color='#64748b', lw=1.2) # Expiry

# Associations: Administrator
ax.plot([90, 63], [18, 81], color='#64748b', lw=1.2)   # Auth
ax.plot([90, 76.5], [18, 14], color='#64748b', lw=1.2) # Manage Staff

# Include / Extend Relations (Dashed arrows)
# Preethi AI extends Emergency
ax.annotate('', xy=(52, 73), xytext=(48, 73),
            arrowprops=dict(arrowstyle="->", linestyle='dashed', color='#dc2626', lw=1.5))
ax.text(50, 74.2, "<<extend>>", ha='center', va='bottom', fontsize=7.5, color='#dc2626', fontweight='bold')

# Vitals includes ML Risk
ax.annotate('', xy=(52, 54), xytext=(48.5, 54),
            arrowprops=dict(arrowstyle="->", linestyle='dashed', color='#7c3aed', lw=1.5))
ax.text(50, 55.2, "<<include>>", ha='center', va='bottom', fontsize=7.5, color='#7c3aed', fontweight='bold')

# Order Lab extends Barcode Accession
ax.annotate('', xy=(36, 26.5), xytext=(36, 31.5),
            arrowprops=dict(arrowstyle="->", linestyle='dashed', color='#059669', lw=1.5))
ax.text(37, 29, "<<include>>", ha='left', va='center', fontsize=7.5, color='#059669', fontweight='bold')

plt.tight_layout()
output_path = r"c:\Users\DELL\Documents\MediMate-AI\medimate_usecase_diagram.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print("Use Case Diagram generated successfully at:", output_path)
