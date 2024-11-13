import json
from models.user import User
from utils.response import create_response

def get_user(event, context):
    tenant_id = event['pathParameters']['tenant_id']
    user_id = event['pathParameters']['id_usuario']
    user = User.get_user(tenant_id, user_id)
    if user:
        return create_response(200, user)
    return create_response(404, 'Usuario no encontrado')
