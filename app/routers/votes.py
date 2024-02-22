from fastapi import APIRouter, Depends, HTTPException, status
from .. import models, schemas, oauth2, database
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/vote",
    tags =["Vote"]
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.VoteResponse)
async def vote(vote:schemas.Vote, db:Session=Depends(database.get_db), current_user:int = Depends(oauth2.get_current_user)):
    post_exist = db.query(models.Post).filter(models.Post.id== vote.post_id).first()
    if post_exist is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post does not exist")
    vote_exists = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id, models.Vote.user_id == current_user.id)
    vote_response= schemas.VoteResponse
    if vote_exists.first():
        vote_exists.delete(synchronize_session=False)
        vote_response.message="Unliked"
        db.commit()
    else:
        vote_response.message="Liked"
        new_vote = models.Vote(**vote.dict())
        db.add(new_vote)
        db.commit()
        
    return vote_response
        
        
        
        
   
       

