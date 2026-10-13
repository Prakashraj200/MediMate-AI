"""
Unit tests for Admin Routes (/api/admin)
"""

import unittest
from app import app


class TestAdminRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()

    def test_admin_users_list(self):
        response = self.client.get("/api/admin/users")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(data.get("success"))

    def test_admin_user_not_found(self):
        response = self.client.get("/api/admin/users/non-existent-id-999")
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
