from typing import List
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db, SessionLocal
from models import User, Product, Order
from schema import UserSchema, ProductSchema, OrderSchema, AuthSchema, TokenSchema
from auth import get_token, decode_token, get_token_auth

app = FastAPI()

@app.get("/", response_model=List[ProductSchema])
async def get_products(db: Session = Depends(get_db)):
    products = db.query(Product).all()
    return products

@app.post("/create_product/", response_model=ProductSchema)
async def create_product(product: ProductSchema, user: dict = Depends(get_token_auth), db: Session = Depends(get_db)):
    db_product = Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@app.get("/orders/", response_model=List[OrderSchema])
async def get_orders(user_id: int, user: dict = Depends(get_token_auth), db: Session = Depends(get_db)):
    orders = db.query(Order).filter(Order.user_id == user_id).all()
    return orders

@app.get("/order/", response_model=OrderSchema)
async def get_order(user_id: int, order_id: int, user: dict = Depends(get_token_auth), db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.user_id == user_id, Order.id == order_id).first()
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@app.post("/create_order/", response_model=OrderSchema)
async def create_order(order: OrderSchema, user: dict = Depends(get_token_auth), db: Session = Depends(get_db)):
    db_order = Order(**order.model_dump())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

@app.post("/api/token/")
async def auth_token(req_user: AuthSchema, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == req_user.username,
                                 User.hashed_password == req_user.hashed_password).first()
    if not user:
        return {"success": False, "msg": "wrong username or password"}
    token = get_token(req_user.model_dump())

    return {"success": True, "token": token, "user": user}

@app.post("/signin/") # sign in
async def sign_in(req_token: TokenSchema, db: Session = Depends(get_db)):
    decoded_user = decode_token(req_token.token)
    if not decoded_user:
        return {"success": False, "msg": "Auth failed"}

    _user = decoded_user.get('user')
    user = db.query(User).filter(User.username == _user.get('username'),
                                 User.hashed_password == _user.get('hashed_password')).first()
    if not user:
        return {"success": False, "msg": "wrong username or password"}
    return {"success": True, 'user': user}

@app.post("/signup/")
async def sign_up(user: UserSchema, db: Session = Depends(get_db)):
    try:
        db_user = User(**user.model_dump())
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except Exception as e:
        return {"success": False, "msg": str(e)}
