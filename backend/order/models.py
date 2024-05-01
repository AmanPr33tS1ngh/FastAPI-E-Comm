from datetime import datetime
import sqlalchemy as sql
from database import Base

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
