import os

admin_dir = r"frontend/admin"
files = [
    "dashboard.html",
    "doctors.html",
    "patients.html",
    "appointments.html",
    "tele-rehab.html",
    "reports.html",
    "settings.html",
    "profile.html"
]

for f in files:
    p = os.path.join(admin_dir, f)
    if not os.path.exists(p):
        continue
    with open(p, "r", encoding="utf-8") as fp:
        content = fp.read()
    
    updated = content.replace('href="admin-login.html"', 'href="/login.html"')
    updated = updated.replace('window.location.href = "admin-login.html"', 'window.location.href = "/login.html"')
    updated = updated.replace('window.location.href = "admin-login.html";', 'window.location.href = "/login.html";')
    
    with open(p, "w", encoding="utf-8") as fp:
        fp.write(updated)
    print(f"Updated logout links in {f}")
