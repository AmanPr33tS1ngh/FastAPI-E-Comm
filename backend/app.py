from fastapi import FastAPI
from order.routes import order_router
from product.routes import product_router
from user.routes import user_router

app = FastAPI()

@app.get("/")
async def index():
    return {"msg": "Hello World"}

app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(product_router, prefix="/products", tags=["products"])
app.include_router(order_router, prefix="/orders", tags=["orders"])
