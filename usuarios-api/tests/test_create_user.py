import unittest
from src.handlers.create_user import create_user
from unittest.mock import patch

class TestCreateUser(unittest.TestCase):
    @patch('src.models.user.User.create_user')
    def test_create_user_success(self, mock_create_user):
        event = {
            "body": '{"tenant_id": "tenant1", "nombre": "John", "apellido": "Doe", "email": "johndoe@example.com", "password": "password123"}'
        }
        context = {}
        response = create_user(event, context)
        self.assertEqual(response['statusCode'], 201)
        self.assertEqual(response['body'], 'Usuario creado con éxito')

    @patch('src.models.user.User.create_user')
    def test_create_user_existing_email(self, mock_create_user):
        mock_create_user.side_effect = Exception("Usuario ya existe")
        event = {
            "body": '{"tenant_id": "tenant1", "nombre": "John", "apellido": "Doe", "email": "johndoe@example.com", "password": "password123"}'
        }
        context = {}
        response = create_user(event, context)
        self.assertEqual(response['statusCode'], 400)
        self.assertIn("Usuario ya existe", response['body'])

if __name__ == '__main__':
    unittest.main()
