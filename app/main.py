# Import necessary modules
from fastapi import FastAPI
from app.routers import auth, posts
from app.db.database import Base, engine

# Create database tables
Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI()

# Include authentication and posts routers
app.include_router(auth.router)
app.include_router(posts.router)
