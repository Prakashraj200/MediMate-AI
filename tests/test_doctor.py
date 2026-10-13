"""
Unit tests for Doctor Routes (/api/doctors)
"""

import unittest
from app import app


class TestDoctorRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()

    def test_doctors_list(self):
        response = self.client.get("/api/doctors/")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(data.get("success"))

    def test_single_doctor_not_found(self):
        response = self.client.get("/api/doctors/invalid-doc-id-999")
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
