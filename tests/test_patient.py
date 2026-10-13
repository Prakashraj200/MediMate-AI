"""
Unit tests for Patient Routes (/api/patients)
"""

import unittest
from app import app


class TestPatientRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()

    def test_patients_list(self):
        response = self.client.get("/api/patients/")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(data.get("success"))

    def test_single_patient_not_found(self):
        response = self.client.get("/api/patients/invalid-patient-id-999")
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
