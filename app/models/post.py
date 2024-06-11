from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

# Define the Post model class
class Post(Base):
    # Table name
    __tablename__ = 'posts'

    # Columns
    id = Column(Integer, primary_key=True, index=True)  # Post ID
    text = Column(String, index=True)  # Post text
    user_id = Column(Integer, ForeignKey('users.id'))  # Foreign key to link posts with users

    # Relationship with the User model
    user = relationship("User")
