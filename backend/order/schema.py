from pydantic import BaseModel

class OrderSchema(BaseModel):
    quantity: int
    user_id: int
    product_id: int
    order_amount: int
    transaction_id: str
    is_delivered: bool
    created_at: str
