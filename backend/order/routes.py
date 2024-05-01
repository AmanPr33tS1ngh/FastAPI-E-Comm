from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from .models import Order
from .schema import OrderSchema
from auth import get_token_auth

# Order Router
order_router = APIRouter()

@order_router.get("/", response_model=List[OrderSchema])
async def get_orders(user: dict = Depends(get_token_auth), db: Session = Depends(get_db)):
    if user is None:
        raise HTTPException(status_code=404, detail="User not found. Please login again to get orders")

    orders = db.query(Order).filter(Order.user_id == user.get('id')).all()
    return orders

@order_router.post("/", response_model=OrderSchema)
async def create_order(order: OrderSchema, user: dict = Depends(get_token_auth), db: Session = Depends(get_db)):
    if user is None:
        raise HTTPException(status_code=404, detail="Please log in again to create an order")

    db_order = Order(**order.model_dump())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

@order_router.get("/{order_id}/", response_model=OrderSchema)
async def get_order(order_id: int, user: dict = Depends(get_token_auth), db: Session = Depends(get_db)):
    if user is None:
        raise HTTPException(status_code=404, detail="User not found. Please login again to get orders")

    order = db.query(Order).filter(Order.user_id == user.get('id'), Order.id == order_id).first()
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@order_router.put("/{order_id}/")
async def get_order(order_id: int, updated_order: OrderSchema, user: dict = Depends(get_token_auth), db: Session = Depends(get_db)):
    if user is None:
        raise HTTPException(status_code=404, detail="User not found. Please login again to get orders")

    order = db.query(Order).filter(Order.user_id == user.get('id'), Order.id == order_id).first()
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")

    if order.is_delivered:
        raise HTTPException(status_code=400, detail="Order is already delivered")

    order.quantity = updated_order.quantity
    order.order_amount = updated_order.order_amount
    db.commit()
    return {'success': True, 'msg': 'Deleted'}

@order_router.delete("/{order_id}/")
async def get_order(order_id: int, user: dict = Depends(get_token_auth), db: Session = Depends(get_db)):
    if user is None:
        raise HTTPException(status_code=404, detail="User not found. Please login again to get orders")

    order = db.query(Order).filter(Order.user_id == user.get('id'), Order.id == order_id).first()
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    db.delete(order)
    db.commit()

    return {'success': True, 'msg': 'Deleted'}
