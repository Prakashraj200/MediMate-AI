import os, shutil
from PIL import Image

upload_dir = r'C:\Users\DELL\.gemini\antigravity\brain\4a9ee622-b1af-4b4c-9362-e46c9e06f79e\.user_uploaded'
dest_dir = r'c:\Users\DELL\Documents\MediMate-AI\frontend\report_screenshots'
os.makedirs(dest_dir, exist_ok=True)

# Map the 6 key screenshots
# 1. Login & Multi-Role Authentication
# 2. Patient Recovery Dashboard & VAS Slider
# 3. Preethi AI Clinical Conversational Assistant
# 4. Emergency Red-Flag Triage & Hotline Alert
# 5. WebRTC Peer-to-Peer Tele-Consultation Suite
# 6. Physiotherapist Clinical Monitoring & Recovery Analytics

candidates = {
    "screenshot_1_login.png": "media_1792666244219_5c630610.png",
    "screenshot_2_patient_dashboard.png": "media_1792689088716_18633781.png",
    "screenshot_3_preethi_ai_chat.png": "media_1792686106098_4a15623c.png",
    "screenshot_4_tele_consultation_webrtc.png": "media_1792691261218_7c5e8e4f.png",
    "screenshot_5_doctor_admin_portal.png": "media_1792689796637_877c84ca.png",
    "screenshot_6_appointments_recap.png": "media_1792743733492_64965df9.png"
}

for dest_name, src_name in candidates.items():
    src_path = os.path.join(upload_dir, src_name)
    dest_path = os.path.join(dest_dir, dest_name)
    if os.path.exists(src_path):
        shutil.copy(src_path, dest_path)
        im = Image.open(dest_path)
        print(f"Copied {dest_name}: {im.size}")
    else:
        print(f"Source not found: {src_name}")

print("All screenshots successfully copied to frontend/report_screenshots/")
