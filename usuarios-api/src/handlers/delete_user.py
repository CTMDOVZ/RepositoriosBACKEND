from models.user import User
from utils.response import create_response

def delete_user(event, context):
    tenant_id = event['pathParameters']['tenant_id']
    user_id = event['pathParameters']['id_usuario']
    User.delete_user(tenant_id, user_id)
    return create_response(200, 'Usuario eliminado')
