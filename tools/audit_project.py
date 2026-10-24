import os
import re
import urllib.request
import urllib.error

base_dir = r"frontend"
roles = ["admin", "doctor", "patient"]

print("==================================================")
print("1. AUDITING SIDEBARS AND LINKS")
print("==================================================")

broken_links_found = []

for role in roles:
    r_dir = os.path.join(base_dir, role)
    if not os.path.exists(r_dir):
        continue
    files = [f for f in os.listdir(r_dir) if f.endswith(".html")]
    print(f"\n--- ROLE: {role.upper()} ({len(files)} files) ---")
    for f in sorted(files):
        p = os.path.join(r_dir, f)
        with open(p, "r", encoding="utf-8", errors="ignore") as fp:
            content = fp.read()

        is_redirect = "http-equiv=\"refresh\"" in content or "window.location.replace" in content
        if is_redirect:
            print(f"  [REDIRECT] {f}")
            continue

        aside_match = re.search(r"<aside[^>]*class=[\"'][^\"']*sidebar[^\"']*[\"'][^>]*>(.*?)</aside>", content, re.DOTALL | re.IGNORECASE)
        if not aside_match:
            aside_match = re.search(r"<aside[^>]*id=[\"']sidebar[\"'][^>]*>(.*?)</aside>", content, re.DOTALL | re.IGNORECASE)

        if aside_match:
            links = re.findall(r'href=[\"\']([^\"\'#]+)[\"\']', aside_match.group(1))
            print(f"  [PAGE] {f} -> Sidebar links count: {len(links)}")
            for l in links:
                if l.startswith("http") or l.startswith("javascript") or l.startswith("mailto"):
                    continue
                clean_link = l.split("?")[0]
                if clean_link.startswith("/"):
                    target = os.path.normpath(os.path.join(base_dir, clean_link.lstrip("/")))
                else:
                    target = os.path.normpath(os.path.join(r_dir, clean_link))

                if not os.path.exists(target):
                    err_msg = f"BROKEN LINK in {role}/{f}: {l} -> {target}"
                    print(f"    [FAIL] {err_msg}")
                    broken_links_found.append(err_msg)
                else:
                    # check if target is a redirect
                    with open(target, "r", encoding="utf-8", errors="ignore") as tf:
                        tcontent = tf.read()
                        if "http-equiv=\"refresh\"" in tcontent:
                            print(f"    [WARN] {l} links to redirect file {os.path.basename(target)}")
        else:
            print(f"  [NO SIDEBAR] {f}")

print("\n==================================================")
print("2. TESTING LIVE BACKEND ENDPOINTS & APIS")
print("==================================================")

endpoints = [
    # Static pages
    "http://127.0.0.1:5000/",
    "http://127.0.0.1:5000/index.html",
    "http://127.0.0.1:5000/login.html",
    "http://127.0.0.1:5000/tele-rehab.html",

    # Admin
    "http://127.0.0.1:5000/admin/dashboard.html",
    "http://127.0.0.1:5000/admin/doctors.html",
    "http://127.0.0.1:5000/admin/patients.html",
    "http://127.0.0.1:5000/admin/appointments.html",
    "http://127.0.0.1:5000/admin/tele-rehab.html",
    "http://127.0.0.1:5000/admin/reports.html",
    "http://127.0.0.1:5000/admin/settings.html",
    "http://127.0.0.1:5000/admin/profile.html",

    # Doctor
    "http://127.0.0.1:5000/doctor/dashboard.html",
    "http://127.0.0.1:5000/doctor/preethi-ai.html",
    "http://127.0.0.1:5000/doctor/appointments.html",
    "http://127.0.0.1:5000/doctor/patients.html",
    "http://127.0.0.1:5000/doctor/patient-records.html",
    "http://127.0.0.1:5000/doctor/profile.html",

    # Patient
    "http://127.0.0.1:5000/patient/dashboard.html",
    "http://127.0.0.1:5000/patient/rehab.html",
    "http://127.0.0.1:5000/patient/preethi-ai.html",
    "http://127.0.0.1:5000/patient/appointments.html",
    "http://127.0.0.1:5000/patient/doctors.html",
    "http://127.0.0.1:5000/patient/health-records.html",
    "http://127.0.0.1:5000/patient/profile.html",

    # APIs
    "http://127.0.0.1:5000/api/admin/metrics",
    "http://127.0.0.1:5000/api/rehab/knowledge-base",
    "http://127.0.0.1:5000/api/rehab/patient-logs",
    "http://127.0.0.1:5000/api/rehab/exercises",
    "http://127.0.0.1:5000/api/tele-rehab/rooms"
]

failed_endpoints = []
for ep in endpoints:
    try:
        req = urllib.request.Request(ep, headers={"User-Agent": "MediMate-Tester/1.0"})
        res = urllib.request.urlopen(req, timeout=5)
        print(f"  [OK] {ep} -> HTTP {res.status} ({len(res.read())} bytes)")
    except urllib.error.HTTPError as he:
        print(f"  [FAIL] {ep} -> HTTP {he.code}")
        failed_endpoints.append((ep, he.code))
    except Exception as ex:
        print(f"  [FAIL] {ep} -> ERROR: {ex}")
        failed_endpoints.append((ep, str(ex)))

print("\n==================================================")
print("AUDIT SUMMARY:")
print(f"Broken links: {len(broken_links_found)}")
print(f"Failed endpoints: {len(failed_endpoints)}")
print("==================================================")
