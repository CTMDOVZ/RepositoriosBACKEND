import unittest
from src.handlers.get_user import get_user
from unittest.mock import patch

class TestGetUser(unittest.TestCase):
    @patch('src.models.user.User.get_user')
    def test_get_user_success(self, mock_get_user):
        mock_get_user.return_value = {"nombre": "John", "apellido": "Doe"}
        event = {"pathParameters": {"tenant_id": "tenant1", "id_usuario": "user1"}}
        context = {}
        response = get_user(event, context)
        self.assertEqual(response['statusCode'], 200)
        self.assertIn("John", response['body'])

    @patch('src.models.user.User.get_user')
    def test_get_user_not_found(self, mock_get_user):
        mock_get_user.return_value = None
        event = {"pathParameters": {"tenant_id": "tenant1", "id_usuario": "user1"}}
        context = {}
        response = get_user(event, context)
        self.assertEqual(response['statusCode'], 404)
        self.assertIn("Usuario no encontrado", response['body'])

if __name__ == '__main__':
    unittest.main()
