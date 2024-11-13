import json
from models.user import User
from utils.response import create_response

def update_user(event, context):
    tenant_id = event['pathParameters']['tenant_id']
    user_id = event['pathParameters']['id_usuario']
    data = json.loads(event['body'])
    response = User.update_user(tenant_id, user_id, data)
    return create_response(200, response)
