from html2image import Html2Image
import os, zipfile, time

dest_dir = r"c:\Users\DELL\Documents\MediMate-AI\frontend\report_screenshots"
os.makedirs(dest_dir, exist_ok=True)

hti = Html2Image(
    browser_executable=r'C:\Program Files\Google\Chrome\Application\chrome.exe',
    output_path=dest_dir,
    custom_flags=['--no-sandbox', '--disable-gpu', '--hide-scrollbars']
)
hti.size = (1366, 768)

targets = [
    ('http://127.0.0.1:5000/login.html', 'screenshot_1_login.png'),
    ('http://127.0.0.1:5000/patient/dashboard.html', 'screenshot_2_patient_dashboard.png'),
    ('http://127.0.0.1:5000/patient/preethi-ai.html', 'screenshot_3_preethi_ai_chat.png'),
    ('http://127.0.0.1:5000/patient/rehab.html', 'screenshot_4_patient_rehab.png'),
    ('http://127.0.0.1:5000/doctor/dashboard.html', 'screenshot_5_doctor_dashboard.png'),
    ('http://127.0.0.1:5000/admin/dashboard.html', 'screenshot_6_admin_dashboard.png')
]

for url, filename in targets:
    print(f"Capturing fresh {url} -> {filename}...")
    try:
        hti.screenshot(url=url, save_as=filename)
        out_fp = os.path.join(dest_dir, filename)
        if os.path.exists(out_fp):
            print(f"  [SUCCESS] {filename} created ({os.path.getsize(out_fp)} bytes)")
        else:
            print(f"  [FAILED] {filename} not found!")
    except Exception as e:
        print(f"  [ERROR] {e}")

# Rebuild ZIP
zip_path = r"c:\Users\DELL\Documents\MediMate-AI\frontend\MediMate_AI_Report_Screenshots.zip"
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
    for _, f in targets:
        fp = os.path.join(dest_dir, f)
        if os.path.exists(fp):
            z.write(fp, arcname=f)

print(f"Rebuilt {zip_path} with fresh screenshots! Size: {os.path.getsize(zip_path)} bytes")
