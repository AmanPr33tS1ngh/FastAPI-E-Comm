from pydantic import BaseModel
from datetime import datetime 

class UserSchema(BaseModel):
    name: str
    username: str
    email: str
    hashed_password: str
    
class ProductSchema(BaseModel):
    price: int
    name: str
    url: str
    image: str
    category: str
    description: str
    
    
class OrderSchema(BaseModel):
    quantity: int
    user_id: str
    product_id: str
    order_amount: int
    transaction_id: str
    is_delivered: bool
    created_at: datetime