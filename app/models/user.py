from sqlalchemy import Column, Integer, String
from app.db.database import Base

# Define the User model class
class User(Base):
    # Table name
    __tablename__ = 'users'

    # Columns
    id = Column(Integer, primary_key=True, index=True)  # User ID
    email = Column(String, unique=True, index=True)  # User email
    hashed_password = Column(String)  # Hashed password
