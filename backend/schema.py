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

class ProductSchema(BaseModel):
    price: int
    name: str
    url: str
    image: str
    category: str
    description: str

class OrderSchema(BaseModel):
    quantity: int
    user_id: int  # Use int instead of str for user_id and product_id
    product_id: int
    order_amount: int
    transaction_id: str
    is_delivered: bool
    created_at: str  # Serialize datetime as string
