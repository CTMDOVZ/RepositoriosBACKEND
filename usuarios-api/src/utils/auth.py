import jwt
import os
from datetime import datetime, timedelta

SECRET_KEY = os.environ['JWT_SECRET']

def generate_token(data):
    """
    Genera un token JWT que incluye user_id en el payload.
    """
    expiration = datetime.utcnow() + timedelta(hours=1)
   
    payload = {
        "user_id": data["id_usuario"],  
        "tenant_id": data["tenant_id"],
        "exp": expiration
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")
