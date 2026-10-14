import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import app

client = app.app.test_client()

routes_to_test = [
    # Top-level & Auth
    '/',
    '/index.html',
    '/register.html',
    '/forgot-password.html',

    # Admin Portal
    '/admin',
    '/admin/',
    '/admin/login',
    '/admin/admin-login.html',
    '/admin/dashboard.html',
    '/admin/doctors.html',
    '/admin/patients.html',
    '/admin/appointments.html',
    '/admin/departments.html',
    '/admin/medicines.html',
    '/admin/pharmacy.html',
    '/admin/laboratory.html',
    '/admin/prescriptions.html',
    '/admin/reports.html',
    '/admin/notifications.html',
    '/admin/settings.html',
    '/admin/profile.html',

    # Doctor Portal
    '/doctor',
    '/doctor/',
    '/doctor/login',
    '/doctor/doctor-login.html',
    '/doctor/dashboard.html',
    '/doctor/appointments.html',
    '/doctor/patients.html',
    '/doctor/prescriptions.html',
    '/doctor/patient-records.html',
    '/doctor/health-monitoring.html',
    '/doctor/notifications.html',
    '/doctor/profile.html',

    # Patient Portal
    '/patient',
    '/patient/',
    '/patient/login',
    '/patient/patient-login.html',
    '/patient/dashboard.html',
    '/patient/appointments.html',
    '/patient/doctors.html',
    '/patient/health-records.html',
    '/patient/lab-reports.html',
    '/patient/medicines.html',
    '/patient/notifications.html',
    '/patient/preethi-ai.html',
    '/patient/prescriptions.html',
    '/patient/profile.html',
    '/patient/vitals.html',

    # Pharmacy Portal
    '/pharmacy',
    '/pharmacy/',
    '/pharmacy/login',
    '/pharmacy/pharmacy-login.html',
    '/pharmacy/dashboard.html',
    '/pharmacy/inventory.html',
    '/pharmacy/medicines.html',
    '/pharmacy/prescriptions.html',
    '/pharmacy/stock-management.html',
    '/pharmacy/expiry-management.html',
    '/pharmacy/notifications.html',
    '/pharmacy/profile.html',

    # Laboratory Portal
    '/laboratory',
    '/laboratory/',
    '/laboratory/login',
    '/laboratory/lab-login.html',
    '/laboratory/dashboard.html',
    '/laboratory/test-management.html',
    '/laboratory/test-requests.html',
    '/laboratory/test-results.html',
    '/laboratory/lab-reports.html',
    '/laboratory/notifications.html',
    '/laboratory/profile.html',

    # Backend APIs
    '/api/health',
    '/api/admin/metrics',
    '/api/admin/dashboard-metrics',
    '/api/doctors/',
    '/api/patients/',
    '/api/patient/patients/',
    '/api/appointments/',
    '/api/appointment/appointments/',
    '/api/departments/',
    '/api/department/departments/',
    '/api/medicines/',
    '/api/pharmacy/pharmacies/',
    '/api/prescriptions/',
    '/api/laboratories/',
    '/api/laboratory/laboratories/',
    '/api/vitals/'
]

print("Testing routes:")
all_ok = True
for r in routes_to_test:
    res = client.get(r, follow_redirects=True)
    status = res.status_code
    print(f"{r:36} -> {status} ({len(res.data)} bytes)")
    if status != 200:
        all_ok = False

print(f"\nOverall route status: {'ALL ROUTES OK!' if all_ok else 'SOME ROUTES FAILED'}")
