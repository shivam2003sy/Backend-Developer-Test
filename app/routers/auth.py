from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas import user as user_schema
from app.models import user as user_model
from app.core.security import get_password_hash, create_access_token, verify_password
from app.dependencies import get_db

# Create a router for authentication endpoints
router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

# User signup endpoint
@router.post("/signup", response_model=user_schema.User)
def signup(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    # Check if the email is already registered
    db_user = db.query(user_model.User).filter(user_model.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Hash the password and create a new user
    hashed_password = get_password_hash(user.password)
    new_user = user_model.User(email=user.email, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# User login endpoint
@router.post("/login")
def login(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    # Find the user by email
    db_user = db.query(user_model.User).filter(user_model.User.email == user.email).first()
    
    # Check if the user exists and the password is correct
    if db_user is None or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    
    # Create an access token for the user
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
