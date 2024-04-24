from typing import List
from fastapi import FastAPI, Depends
from .database import get_db
from .models import User, Product, Order
from .schema import UserSchema, ProductSchema, OrderSchema
from sqlalchemy.orm import Session

app = FastAPI()

@app.get("/", response_model=List[Product])
async def get_products(db: Session):
    products = db.query(Product).all()
    print(products)
    return products

@app.post("/create_product", response_model=Product)
async def create_product(product: ProductSchema, db: Session = Depends(get_db)):
    product = Product(product)
    db.add(product)
    db.commit()
    db.refresh(product) 
    return product

@app.get("/orders", response_model=List[Order])
async def get_orders(user_id: int, db: Session):
    orders = db.query(Order).filter(Order.user_id==user_id).all()
    print(orders)
    return orders

@app.post("/create_order", response_model=Order)
async def create_order(order: OrderSchema, db: Session = Depends(get_db)):
    order = Order(order)
    db.add(order)
    db.commit()
    db.refresh(order) 
    return order
