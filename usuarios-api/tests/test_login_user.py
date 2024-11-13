import unittest
from src.handlers.login_user import login_user
from unittest.mock import patch

class TestLoginUser(unittest.TestCase):
    @patch('src.models.user.User.get_user')
    def test_login_success(self, mock_get_user):
        mock_get_user.return_value = {"password": "hashed_password"}
        event = {
            "body": '{"tenant_id": "tenant1", "email": "johndoe@example.com", "password": "password123"}'
        }
        context = {}
        with patch('src.utils.auth.generate_token', return_value="mock_token"):
            response = login_user(event, context)
            self.assertEqual(response['statusCode'], 200)
            self.assertIn("token", response['body'])

    @patch('src.models.user.User.get_user')
    def test_login_invalid_credentials(self, mock_get_user):
        mock_get_user.return_value = None
        event = {
            "body": '{"tenant_id": "tenant1", "email": "johndoe@example.com", "password": "wrong_password"}'
        }
        context = {}
        response = login_user(event, context)
        self.assertEqual(response['statusCode'], 401)
        self.assertIn("Credenciales inválidas", response['body'])

if __name__ == '__main__':
    unittest.main()
