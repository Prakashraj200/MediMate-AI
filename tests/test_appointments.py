"""
Unit tests for Appointments Routes (/api/appointments)
"""

import unittest
from app import app


class TestAppointmentRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()

    def test_list_appointments(self):
        response = self.client.get("/api/appointments/")
        self.assertIn(response.status_code, [200, 401])

    def test_create_appointment_missing_fields(self):
        response = self.client.post("/api/appointments/", json={})
        self.assertIn(response.status_code, [400, 401])


if __name__ == "__main__":
    unittest.main()
