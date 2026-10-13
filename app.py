import os
from flask import Flask, jsonify, send_from_directory
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

app = Flask(
    __name__,
    static_folder=FRONTEND_DIR,
    static_url_path=""
)

CORS(app)


# =========================
# REGISTER ALL BLUEPRINTS
# =========================

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


# =========================
# FRONTEND STATIC ROUTES
# =========================

@app.route("/")
def home():
    return send_from_directory(FRONTEND_DIR, "index.html")


@app.route("/<path:path>")
def serve_static(path):
    if path.startswith("frontend/"):
        path = path[len("frontend/"):]
    target_path = os.path.join(FRONTEND_DIR, path)
    if os.path.isfile(target_path):
        return send_from_directory(FRONTEND_DIR, path)
    if os.path.isfile(target_path + ".html"):
        return send_from_directory(FRONTEND_DIR, path + ".html")
    if os.path.isdir(target_path):
        if os.path.isfile(os.path.join(target_path, "dashboard.html")):
            return send_from_directory(target_path, "dashboard.html")
        if os.path.isfile(os.path.join(target_path, "index.html")):
            return send_from_directory(target_path, "index.html")
    return send_from_directory(FRONTEND_DIR, "index.html")


@app.route("/favicon.ico")
def favicon():
    return ("", 204)


# =========================
# HEALTH CHECK
# =========================

@app.route("/api/health")
def health():
    return jsonify({
        "success": True,
        "message": "MediMate-AI Full Clinical Ecosystem Server is running",
        "registered_blueprints": len(app.blueprints)
    })


# =========================
# RUN SERVER
# =========================

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)