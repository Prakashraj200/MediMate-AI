"""
Unit tests for Pharmacy Routes (/api/pharmacies)
"""

import unittest
from app import app


class TestPharmacyRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()

    def test_pharmacies_list(self):
        response = self.client.get("/api/pharmacies/")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(data.get("success"))

    def test_single_pharmacy_not_found(self):
        response = self.client.get("/api/pharmacies/invalid-pharm-id-999")
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
