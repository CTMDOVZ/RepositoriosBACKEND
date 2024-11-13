import json
from models.user import User
from utils.response import create_response
from utils.auth import generate_token
import bcrypt

def login_user(event, context):
    data = json.loads(event['body'])
    user = User.get_user(data['tenant_id'], data['email'])
    if user and bcrypt.checkpw(data['password'].encode('utf-8'), user['password'].encode('utf-8')):
        token = generate_token({"tenant_id": data['tenant_id'], "id_usuario": user['id_usuario']})
        return create_response(200, {"token": token})
    return create_response(401, 'Credenciales inválidas')
