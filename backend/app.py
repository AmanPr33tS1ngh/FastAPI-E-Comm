from typing import List
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db, SessionLocal
from models import User, Product, Order
from schema import UserSchema, ProductSchema, OrderSchema

app = FastAPI()

@app.get("/", response_model=List[ProductSchema])
async def get_products(db: Session = Depends(get_db)):
    products = db.query(Product).all()
    return products

@app.post("/create_product", response_model=ProductSchema)
async def create_product(product: ProductSchema, db: Session = Depends(get_db)):
    db_product = Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@app.get("/orders/", response_model=List[OrderSchema])
async def get_orders(user_id: int, db: Session = Depends(get_db)):
    orders = db.query(Order).filter(Order.user_id == user_id).all()
    return orders

@app.get("/order/", response_model=OrderSchema)
async def get_order(user_id: int, order_id: int, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.user_id == user_id, Order.id == order_id).first()
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@app.post("/create_order", response_model=OrderSchema)
async def create_order(order: OrderSchema, db: Session = Depends(get_db)):
    db_order = Order(**order.model_dump())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order
