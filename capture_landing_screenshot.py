import subprocess
import os
import time
import shutil

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
html_path = r'c:\Users\DELL\Documents\MediMate-AI\frontend\index.html'
dest_dir = r"c:\Users\DELL\Documents\MediMate-AI\frontend\report_screenshots"
out_img = os.path.join(dest_dir, "screenshot_0_landing_page.png")
art_img = r"C:\Users\DELL\.gemini\antigravity\brain\4a9ee622-b1af-4b4c-9362-e46c9e06f79e\screenshot_0_landing_page.png"
temp_profile = r"C:\Users\DELL\Documents\MediMate-AI\temp_chrome_landing"

cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--hide-scrollbars",
    "--window-size=1920,1080",
    f"--user-data-dir={temp_profile}",
    f"--screenshot={out_img}",
    f"file:///{html_path.replace(os.sep, '/')}"
]

print("Running command:", " ".join(cmd))
proc = subprocess.Popen(cmd)
proc.wait(timeout=15)

if os.path.exists(out_img):
    shutil.copy(out_img, art_img)
    print(f"SUCCESS: Landing page screenshot captured! Size: {os.path.getsize(out_img)} bytes")
else:
    print("FAILED to create landing page screenshot")
