from pydantic import BaseModel

class UserSchema(BaseModel):
    name: str
    username: str
    email: str
    hashed_password: str

class TokenSchema(BaseModel):
    token: str

class AuthSchema(BaseModel):
    username: str
    hashed_password: str
