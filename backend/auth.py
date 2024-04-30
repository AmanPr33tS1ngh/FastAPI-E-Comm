import jwt
from fastapi import Header, HTTPException
from schema import AuthSchema
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

load_dotenv()
JWT_SECRET = os.getenv('JWT_SECRET')
JWT_ALGORITHM = os.getenv('JWT_ALGORITHM')

def get_expiry():
    return (datetime.now() + timedelta(hours=30)).isoformat()

def get_token(user: AuthSchema) -> str:
    payload = {
        "user": user,
        "expires": get_expiry()
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token

def decode_token(token: str) -> dict:
    decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    expiration = decoded_token.get("expires")
    return decoded_token if datetime.fromisoformat(expiration) >= datetime.now() else None

async def get_token_auth(token: str = Header(...)):
    if not token:
        raise HTTPException(status_code=401, detail="Authentication required")

    decoded_token = decode_token(token)
    if not decoded_token:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return token
