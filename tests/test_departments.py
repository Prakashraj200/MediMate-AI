"""
Unit tests for Department Routes (/api/departments)
"""

import unittest
from app import app


class TestDepartmentRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()

    def test_list_departments(self):
        response = self.client.get("/api/departments/")
        self.assertIn(response.status_code, [200, 401])
        if response.status_code == 200:
            data = response.get_json()
            self.assertTrue(data.get("success"))


if __name__ == "__main__":
    unittest.main()
