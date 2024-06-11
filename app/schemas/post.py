from pydantic import BaseModel

class PostCreate(BaseModel):
    text: str

class Post(BaseModel):
    id: int
    text: str
    user_id: int

    class Config:
        orm_mode = True
