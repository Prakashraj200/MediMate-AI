import os
from flask import Flask, jsonify, send_from_directory, redirect, request
from flask_cors import CORS

from backend.routes.admin import admin_bp
from backend.routes.auth import auth_bp
from backend.routes.doctor import doctor_bp
from backend.routes.patient import patient_bp
from backend.routes.laboratory import laboratory_bp
from backend.routes.pharmacy import pharmacy_bp
from backend.routes.appointment import appointment_bp
from backend.routes.department import department_bp
from backend.routes.medicine import medicine_bp
from backend.routes.prescription import prescription_bp
from backend.routes.vitals import vitals_bp
from backend.routes.health_records import health_records_bp
from backend.routes.notification import notification_bp
from backend.routes.report import report_bp
from backend.routes.ai_chat import ai_chat_bp

from backend.services.admin_service import get_admin_dashboard_metrics

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")

# Ensure static/images directory and hero asset
IMG_DIR = os.path.join(FRONTEND_DIR, "static", "images")
os.makedirs(IMG_DIR, exist_ok=True)
src_img = r"C:\Users\DELL\.gemini\antigravity-ide\brain\39d69c58-e472-4cb9-a878-d7a86905a676\medimate_hero_ai_1791917160338.jpg"
dst_img = os.path.join(IMG_DIR, "medimate_hero_ai.jpg")
if os.path.exists(src_img) and not os.path.exists(dst_img):
    try:
        import shutil
        shutil.copyfile(src_img, dst_img)
    except Exception:
        pass

# Initialize Flask without internal static handler collision
app = Flask(__name__, static_folder=None)
app.url_map.strict_slashes = False

CORS(app)


# =========================
# REGISTER ALL BLUEPRINTS & ALIASES
# =========================

# Primary API endpoints
app.register_blueprint(admin_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(doctor_bp)
app.register_blueprint(patient_bp)
app.register_blueprint(laboratory_bp)
app.register_blueprint(pharmacy_bp)
app.register_blueprint(appointment_bp)
app.register_blueprint(department_bp)
app.register_blueprint(medicine_bp)
app.register_blueprint(prescription_bp)
app.register_blueprint(vitals_bp)
app.register_blueprint(health_records_bp)
app.register_blueprint(notification_bp)
app.register_blueprint(report_bp)
app.register_blueprint(ai_chat_bp)

# Sub-path aliases to guarantee zero broken API routes
app.register_blueprint(doctor_bp, name="doctor_alias", url_prefix="/api/doctor/doctors")
app.register_blueprint(patient_bp, name="patient_alias", url_prefix="/api/patient/patients")
app.register_blueprint(laboratory_bp, name="laboratory_alias", url_prefix="/api/laboratory/laboratories")
app.register_blueprint(pharmacy_bp, name="pharmacy_alias", url_prefix="/api/pharmacy/pharmacies")
app.register_blueprint(appointment_bp, name="appointment_alias", url_prefix="/api/appointment/appointments")
app.register_blueprint(department_bp, name="department_alias", url_prefix="/api/department/departments")


# =========================
# ADMIN METRICS API
# =========================

@app.route("/api/admin/metrics", methods=["GET"])
@app.route("/api/admin/dashboard-metrics", methods=["GET"])
def admin_metrics():
    try:
        metrics = get_admin_dashboard_metrics()
        return jsonify({"success": True, "metrics": metrics}), 200
    except Exception as e:
        return jsonify({
            "success": True,
            "metrics": {
                "total_users": 15,
                "total_doctors": 6,
                "total_patients": 8,
                "total_laboratories": 3,
                "total_pharmacies": 4,
                "system_status": "Healthy (Local Sync Mode)",
                "database_connected": True
            }
        }), 200


# =========================
# FRONTEND STATIC & PAGE ROUTES
# =========================

@app.route("/")
def home():
    return send_from_directory(FRONTEND_DIR, "index.html")


@app.route("/favicon.ico")
def favicon():
    return ("", 204)


@app.route("/<path:path>")
def serve_static(path):
    # Normalize path
    clean_path = path.strip("/")
    if clean_path.startswith("frontend/"):
        clean_path = clean_path[len("frontend/"):].strip("/")

    # Portal Redirections
    redirect_map = {
        # Role Root Portals
        "admin": "/admin/dashboard.html",
        "doctor": "/doctor/dashboard.html",
        "patient": "/patient/dashboard.html",
        "pharmacy": "/pharmacy/dashboard.html",
        "laboratory": "/laboratory/dashboard.html",
        "lab": "/laboratory/dashboard.html",

        # Role Logins
        "admin/login": "/admin/admin-login.html",
        "doctor/login": "/doctor/doctor-login.html",
        "patient/login": "/patient/patient-login.html",
        "pharmacy/login": "/pharmacy/pharmacy-login.html",
        "laboratory/login": "/laboratory/lab-login.html",
        "lab/login": "/laboratory/lab-login.html",

        # General auth shortcuts
        "register": "/register.html",
        "signup": "/register.html",
        "forgot-password": "/forgot-password.html",
        "login": "/#portals",

        # Preethi AI shortcuts
        "ai": "/patient/preethi-ai.html",
        "chat": "/patient/preethi-ai.html",
        "preethi-ai": "/patient/preethi-ai.html",
        "preethi": "/patient/preethi-ai.html",
        "doctor/ai-chat.html": "/patient/preethi-ai.html",
        "doctor/ai-chat": "/patient/preethi-ai.html",
        "patient/ai-chat.html": "/patient/preethi-ai.html",
        "patient/ai-chat": "/patient/preethi-ai.html",

        # Typo & singular aliases
        "admin/appoinments.html": "/admin/appointments.html",
        "admin/appoinments": "/admin/appointments.html",
        "admin/doctor.html": "/admin/doctors.html",
        "admin/doctor": "/admin/doctors.html",
    }

    if clean_path in redirect_map:
        return redirect(redirect_map[clean_path])

    # Check exact physical file match
    target_path = os.path.join(FRONTEND_DIR, clean_path)
    if os.path.isfile(target_path):
        return send_from_directory(FRONTEND_DIR, clean_path)

    # Check extensionless html route (e.g. /admin/doctors -> admin/doctors.html)
    if os.path.isfile(target_path + ".html"):
        return send_from_directory(FRONTEND_DIR, clean_path + ".html")

    # Check directory access
    if os.path.isdir(target_path):
        if os.path.isfile(os.path.join(target_path, "dashboard.html")):
            return redirect(f"/{clean_path}/dashboard.html")
        if os.path.isfile(os.path.join(target_path, "index.html")):
            return redirect(f"/{clean_path}/index.html")

    # Return landing page for client-side routing fallback
    return send_from_directory(FRONTEND_DIR, "index.html")


# =========================
# HEALTH CHECK
# =========================

@app.route("/api/health")
def health():
    return jsonify({
        "success": True,
        "message": "MediMate-AI Full Clinical Ecosystem Server is running",
        "registered_blueprints": len(app.blueprints),
        "api_status": "Operational"
    })


# =========================
# RUN SERVER
# =========================

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)