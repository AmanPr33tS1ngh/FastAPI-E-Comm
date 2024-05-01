import sqlalchemy as sql
from database import Base

class Product(Base):
    __tablename__ = "products"
    id = sql.Column(sql.Integer, primary_key=True, index=True)
    price = sql.Column(sql.Integer, default=0)
    name = sql.Column(sql.String(100), unique=True, index=True)
    url = sql.Column(sql.String(100), unique=True, index=True)
    image = sql.Column(sql.String)
    category = sql.Column(sql.String(25))
    description = sql.Column(sql.String(255))
