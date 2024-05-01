from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from .models import User
from .schema import UserSchema, AuthSchema, TokenSchema
from auth import get_token, decode_token, get_token_auth

# User Router
user_router = APIRouter()

@user_router.post("/api/token/")
async def auth_token(req_user: AuthSchema, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == req_user.username,
                                 User.hashed_password == req_user.hashed_password).first()
    if not user:
        raise HTTPException(status_code=404, message="Wrong username or password")

    token = get_token(req_user.model_dump())

    return {"success": True, "token": token, "user": user}

@user_router.post("/signin/") # sign in
async def sign_in(req_token: TokenSchema, db: Session = Depends(get_db)):
    decoded_user = decode_token(req_token.token)
    if not decoded_user:
        raise HTTPException(status_code=404, message="Auth failed")

    _user = decoded_user.get('user')
    user = db.query(User).filter(User.username == _user.get('username'),
                                 User.hashed_password == _user.get('hashed_password')).first()
    if not user:
        raise HTTPException(status_code=404, message="Wrong username or password")
    return user

@user_router.post("/signup/")
async def sign_up(user: UserSchema, db: Session = Depends(get_db)):
    if db.query(User).filter(User.username == user.username).exists():
        raise HTTPException(status_code=404, message="User with same username already exists. "
                                                     "Please use some other username")

    db_user = User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@user_router.get("/profile/")
async def get_order(user: dict = Depends(get_token_auth), db: Session = Depends(get_db)):
    if user is None or user.get('username'):
        raise HTTPException(status_code=404, detail="User not found")

    user_found = db.query(User).filter(User.username == user.get('username')).first()
    if not user_found:
        raise HTTPException(status_code=404, detail="User not found")
    return user_found

@user_router.put("/update_profile/", response_model=UserSchema)
async def get_order(updated_profile: UserSchema, user: dict = Depends(get_token_auth), db: Session = Depends(get_db)):
    if user is None or user.get('username'):
        raise HTTPException(status_code=404, detail="User not found")

    existing_user = db.query(User).filter(User.username == user.get('username')).first()
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")

    existing_user.name = updated_profile.name
    existing_user.username = updated_profile.username
    existing_user.email = updated_profile.email
    db.commit()
    return existing_user
