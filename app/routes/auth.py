from fastapi import APIRouter, HTTPException
from app.schemas.user import UserCreate, UserLogin
from app.database.connection import users_collection
from app.utils.password import hash_password, verify_password
from app.utils.jwt import create_access_token

router = APIRouter()

@router.post("/auth/register")
def register_user(user: UserCreate):
    

    existing_user = users_collection.find_one({
        "$or" : [
            {"email": user.email},
            {"username": user.username}
              ]
    })

    if existing_user:
        raise HTTPException(
        status_code=400,
        detail="Email already registered"
    )

    hashed_password = hash_password(user.password)

    users_collection.insert_one({
        "username": user.username,
        "email": user.email,
        "password": hashed_password
    })

    return {
        "message": "User registration successful",
        "username": user.username,
        "email": user.email
    }

@router.post("/auth/login")
def login_user(user: UserLogin):

    existing_user = users_collection.find_one({
        "email": user.email
    })

    if not existing_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    password_correct = verify_password(
        user.password,
        existing_user["password"]
    )

    if not password_correct:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    access_token = create_access_token({
        "user_id": str(existing_user["_id"]),
        "email": existing_user["email"]
    })

    return {
        "message": "Login successful",
        "access_token": access_token,
        "token_type": "bearer"
    }