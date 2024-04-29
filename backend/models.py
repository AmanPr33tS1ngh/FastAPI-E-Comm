from datetime import datetime
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

    def verify_password(self, password: str):
        return bcrypt.verify(password, self.hashed_password)

class Product(Base):
    __tablename__ = "products"
    id = sql.Column(sql.Integer, primary_key=True, index=True)
    price = sql.Column(sql.Integer, default=0)
    name = sql.Column(sql.String(100), unique=True, index=True)
    url = sql.Column(sql.String(100), unique=True, index=True)
    image = sql.Column(sql.String)
    category = sql.Column(sql.String(25))
    description = sql.Column(sql.String(255))

class Order(Base):
    __tablename__ = "orders"
    id = sql.Column(sql.Integer, primary_key=True, index=True)
    quantity = sql.Column(sql.Integer, nullable=False)
    user_id = sql.Column(sql.Integer, sql.ForeignKey("users.id"))
    product_id = sql.Column(sql.Integer, sql.ForeignKey("products.id"))
    order_amount = sql.Column(sql.Integer, nullable=False)
    transaction_id = sql.Column(sql.String, unique=True)
    is_delivered = sql.Column(sql.Boolean, default=False)
    created_at = sql.Column(sql.DateTime, default=datetime.utcnow)
