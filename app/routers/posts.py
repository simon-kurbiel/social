##get all the posts
from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session
from .. import models, schemas, oauth2
from ..database import get_db

router = APIRouter(
    prefix="/posts",
    tags=['Posts', 'Get all Posts']
)
@router.get("/", status_code=status.HTTP_200_OK, response_model=list[schemas.PostResponse] )
async def get_posts(db:Session=Depends(get_db), current_user:int=Depends(oauth2.get_current_user), limit:int=1, search:str=""):
    posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit)
    
    return posts

##create a post
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.PostResponse)
async def create_posts(post:schemas.Post, db:Session=Depends(get_db), current_user:int=Depends(oauth2.get_current_user)):
    print(current_user.email)
    new_post = models.Post(**post.dict())
    new_post.user_id = current_user.id
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    
    return new_post
    

##get one post
@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.PostResponse)
async def get_one_post(id:int,db:Session=Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id==id).first()
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post does not exist")
    
    return post
    
##delete a post
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id:int, db:Session=Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
   
    post=db.query(models.Post).filter(models.Post.id==id)
    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Post does not exist")
    print(f'user_id = {post.first().user_id}, current_user = {current_user.id}')
    if post.first().user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You do not own this post")
    post.delete(synchronize_session=False)
    db.commit()
    return {
        "success":True,
        "message":"Post deleted"
    }
    
    
##update post
@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=schemas.PostResponse)
async def update_post(id:int, post:schemas.Post, db:Session=Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    post_query=db.query(models.Post).filter(models.Post.id==id)
  
    post_first = post_query.first()
   
    
    if post_first==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'post not found')
    if post_first.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You do not own this post")    
    post_query.update(post.dict(), synchronize_session=False)
    db.commit()
    return post_query.first()
