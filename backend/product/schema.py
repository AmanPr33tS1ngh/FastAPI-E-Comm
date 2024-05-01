from pydantic import BaseModel

class ProductSchema(BaseModel):
    price: int
    name: str
    url: str
    image: str
    category: str
    description: str
