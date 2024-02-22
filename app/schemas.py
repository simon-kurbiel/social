from pydantic import BaseModel, EmailStr
from typing import Annotated
from fastapi import Query
from datetime import datetime
class Post(BaseModel):
    title:str
    content:str
    published:bool = True
    

class UserOut(BaseModel):
    id:int
    email:EmailStr
    created_at:datetime 
    
class PostResponse(Post):
    id:int
    created_at: datetime
    user_id:int
    owner: UserOut
    
    
    
class UserCreate(BaseModel):
    email:EmailStr
    password: str
    

    
class UserLogin(BaseModel):
    email:EmailStr
    password:str
    
    
class Token(BaseModel):
    access_token:str
    token_type : str
    
class TokenData(BaseModel):
    id : int | None = None
    
    
class Vote(BaseModel):
    post_id:int
    user_id:int

class VoteResponse(BaseModel):
    message:str
    

    
   
    
    