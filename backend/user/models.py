import sqlalchemy as sql
from passlib.hash import bcrypt  # Correct import path
from database import Base

class User(Base):
    __tablename__ = "users"
    id = sql.Column(sql.Integer, primary_key=True, index=True)
    name = sql.Column(sql.String, index=True)
    username = sql.Column(sql.String, unique=True, index=True)
    email = sql.Column(sql.String, unique=True, index=True)
    hashed_password = sql.Column(sql.String)
    is_admin = sql.Column(sql.Boolean)

    def verify_password(self, password: str):
        return bcrypt.verify(password, self.hashed_password)
