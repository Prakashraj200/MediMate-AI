"""
Unit tests for Authentication Routes (/api/auth)
"""

import unittest
from app import app


class TestAuthRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()

    def test_register_missing_fields(self):
        response = self.client.post("/api/auth/register", json={"email": "incomplete@medimate.ai"})
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertFalse(data.get("success"))

    def test_verify_token_missing_token(self):
        response = self.client.post("/api/auth/verify-token", json={})
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertFalse(data.get("success"))


if __name__ == "__main__":
    unittest.main()
