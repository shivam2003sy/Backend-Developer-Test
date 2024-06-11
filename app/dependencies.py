from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.core.security import decode_access_token
from app.models import user as user_model
from app.core.security import decode_access_token, oauth2_scheme

# Function to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Function to get the current user from the access token
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    # Define an HTTPException for unauthorized access
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        # Decode the access token
        payload = decode_access_token(token)
        
        # Raise an exception if the payload is None
        if payload is None:
            raise credentials_exception
        
        # Extract the email from the payload
        email: str = payload.get("sub")
        
        # Raise an exception if the email is None
        if email is None:
            raise credentials_exception
    except JWTError:
        # Raise an exception if there's a JWTError
        raise credentials_exception
    
    # Query the database to find the user by email
    user = db.query(user_model.User).filter(user_model.User.email == email).first()
    
    # Raise an exception if the user is not found
    if user is None:
        raise credentials_exception
    
    # Return the user if found
    return user
