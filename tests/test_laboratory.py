"""
Unit tests for Laboratory Routes (/api/laboratories)
"""

import unittest
from app import app


class TestLaboratoryRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()

    def test_laboratories_list(self):
        response = self.client.get("/api/laboratories/")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(data.get("success"))

    def test_single_laboratory_not_found(self):
        response = self.client.get("/api/laboratories/invalid-lab-id-999")
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
