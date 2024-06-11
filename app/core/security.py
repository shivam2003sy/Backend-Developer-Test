from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Union

# Secret key for encoding and decoding JWT tokens
SECRET_KEY = "your-secret-key"

# Algorithm used for encoding JWT tokens
ALGORITHM = "HS256"

# Expiration time for access tokens in minutes
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Create a CryptContext instance for password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2 scheme for dependency injection
def oauth2_scheme(token: str):
    return token

# Verify a password against its hashed version
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Hash a plain text password
def get_password_hash(password):
    return pwd_context.hash(password)

# Create an access token with the given data and expiration time
def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Decode an access token and return its payload
def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
