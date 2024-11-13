import unittest
from src.handlers.delete_user import delete_user
from unittest.mock import patch

class TestDeleteUser(unittest.TestCase):
    @patch('src.models.user.User.delete_user')
    def test_delete_user_success(self, mock_delete_user):
        event = {
            "pathParameters": {"tenant_id": "tenant1", "id_usuario": "user1"}
        }
        context = {}
        response = delete_user(event, context)
        self.assertEqual(response['statusCode'], 200)
        self.assertIn("Usuario eliminado", response['body'])

    @patch('src.models.user.User.delete_user')
    def test_delete_user_not_found(self, mock_delete_user):
        mock_delete_user.side_effect = Exception("Usuario no encontrado")
        event = {
            "pathParameters": {"tenant_id": "tenant1", "id_usuario": "user1"}
        }
        context = {}
        response = delete_user(event, context)
        self.assertEqual(response['statusCode'], 404)
        self.assertIn("Usuario no encontrado", response['body'])

if __name__ == '__main__':
    unittest.main()
