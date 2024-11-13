import unittest
from src.handlers.update_user import update_user
from unittest.mock import patch

class TestUpdateUser(unittest.TestCase):
    @patch('src.models.user.User.update_user')
    def test_update_user_success(self, mock_update_user):
        mock_update_user.return_value = {"nombre": "John Updated"}
        event = {
            "pathParameters": {"tenant_id": "tenant1", "id_usuario": "user1"},
            "body": '{"nombre": "John Updated"}'
        }
        context = {}
        response = update_user(event, context)
        self.assertEqual(response['statusCode'], 200)
        self.assertIn("John Updated", response['body'])

    @patch('src.models.user.User.update_user')
    def test_update_user_not_found(self, mock_update_user):
        mock_update_user.side_effect = Exception("Usuario no encontrado")
        event = {
            "pathParameters": {"tenant_id": "tenant1", "id_usuario": "user1"},
            "body": '{"nombre": "John Updated"}'
        }
        context = {}
        response = update_user(event, context)
        self.assertEqual(response['statusCode'], 404)
        self.assertIn("Usuario no encontrado", response['body'])

if __name__ == '__main__':
    unittest.main()
