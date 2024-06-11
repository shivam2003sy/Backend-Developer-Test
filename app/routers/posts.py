from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from sqlalchemy.orm import Session
from app.schemas import post as post_schema
from app.models import post as post_model
from app.dependencies import get_current_user, get_db
from app.core.caching import cache
from app.models.user import User

# Create a router for post-related endpoints
router = APIRouter(
    prefix="/posts",
    tags=["posts"],
)

# Create a new post
@router.post("/", response_model=post_schema.Post)
def create_post(post: post_schema.PostCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    # Check if the text size exceeds 1 MB
    if len(post.text.encode('utf-8')) > 1024 * 1024:
        raise HTTPException(status_code=400, detail="Payload size exceeds 1 MB")
    
    # Create the post and associate it with the current user
    db_post = post_model.Post(text=post.text, user_id=current_user.id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

# Get all posts for the current user
@router.get("/", response_model=list[post_schema.Post])
def get_posts(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    # Check if the posts are cached for the current user
    if current_user.id in cache:
        return cache[current_user.id]
    
    # Retrieve the posts from the database and cache them
    posts = db.query(post_model.Post).filter(post_model.Post.user_id == current_user.id).all()
    cache[current_user.id] = posts
    return posts

# Delete a post by ID
@router.delete("/{post_id}", response_model=post_schema.Post)
def delete_post(post_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    # Find the post by ID and user ID
    post = db.query(post_model.Post).filter(post_model.Post.id == post_id, post_model.Post.user_id == current_user.id).first()
    
    # If the post doesn't exist, raise an HTTPException
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    
    # Delete the post and commit the transaction
    db.delete(post)
    db.commit()
    return post
