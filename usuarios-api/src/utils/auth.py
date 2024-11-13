import jwt
import os
from datetime import datetime, timedelta

SECRET_KEY = os.environ['JWT_SECRET']

def generate_token(data):
    expiration = datetime.utcnow() + timedelta(hours=1)
    data.update({"exp": expiration})
    return jwt.encode(data, SECRET_KEY, algorithm="HS256")

def verify_token(token):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return None
