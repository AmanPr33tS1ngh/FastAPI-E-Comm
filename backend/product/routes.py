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
    return db.query(Product).all()

@product_router.get("/{product_id}/", response_model=ProductSchema)
async def get_products(product_id: int, db: Session = Depends(get_db)):
    return db.query(Product).filter(Product.id == product_id).first()

@product_router.put("/{product_id}/", response_model=ProductSchema)
async def update_products(product_id: int, updated_product: ProductSchema, user: Depends(get_token_auth), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == user.get('id')).first()
    if user is None or not user.is_admin:
        raise HTTPException(status_code=404, detail="You are not authorised to update products!")

    product = db.query(Product).filter(Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found!")

    product.name = updated_product.name
    product.price = updated_product.price
    product.url = updated_product.url
    product.image = updated_product.image
    product.description = updated_product.description
    db.commit()
    return product

@product_router.delete("/{product_id}/", response_model=ProductSchema)
async def delete_products(product_id: int, user: Depends(get_token_auth), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == user.get('id')).first()
    if user is None or not user.is_admin:
        raise HTTPException(status_code=404, detail="You are not authorised to update products!")

    product = db.query(Product).filter(Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found!")

    db.delete(product)
    db.commit()
    return product

@product_router.post("/", response_model=ProductSchema)
async def create_product(product: ProductSchema, user: dict = Depends(get_token_auth), db: Session = Depends(get_db)):
    if user is None:
        raise HTTPException(status_code=404, detail="You are not authorised to add products!")

    user = db.query(User).filter(User.id == user.get('id')).first()
    if not user.is_admin:
        raise HTTPException(status_code=404, detail="You are not authorised to add products!")

    product = Product(**product.model_dump())
    db.add(product)
    db.commit()
    db.refresh(product)
    return product
