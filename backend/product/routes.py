from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from .models import Product
from .schema import ProductSchema
from auth import get_token_auth
from user.models import User

# Product Router
product_router = APIRouter()

@product_router.get("/", response_model=List[ProductSchema])
async def get_products(db: Session = Depends(get_db)):
    products = db.query(Product).all()
    return products

@product_router.get("/{product_id}/", response_model=List[ProductSchema])
async def get_products(product_id: int, db: Session = Depends(get_db)):
    return db.query(Product).filter(Product.id == product_id).first()

@product_router.post("/", response_model=ProductSchema)
async def create_product(product: ProductSchema, user: dict = Depends(get_token_auth), db: Session = Depends(get_db)):
    if user is None:
        raise HTTPException(status_code=404, detail="You are not authorised to add products!")

    user = db.query(User).filter(User.id == user.get('id')).first()
    if not user.is_admin:
        raise HTTPException(status_code=404, detail="You are not authorised to add products!")

    db_product = Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product
