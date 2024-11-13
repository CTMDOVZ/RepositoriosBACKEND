import json
from models.user import User
from utils.response import create_response
from utils.auth import generate_token
import uuid
import bcrypt

def create_user(event, context):
    data = json.loads(event['body'])
    hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
    item = {
        'tenant_id': data['tenant_id'],
        'id_usuario': str(uuid.uuid4()),
        'nombre': data['nombre'],
        'apellido': data['apellido'],
        'email': data['email'],
        'password': hashed_password.decode('utf-8')
    }
    User.create_user(item)
    return create_response(201, 'Usuario creado con éxito')
