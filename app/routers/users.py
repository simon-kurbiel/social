from .. import models, schemas, utils
from fastapi import FastAPI, Response, status,HTTPException,Body, Depends, APIRouter
from ..database import get_db
from sqlalchemy.orm import Session

router= APIRouter(
    prefix='/users',
    tags=['Users']
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
async def create_user(user:schemas.UserCreate,db:Session = Depends(get_db)):
    ##hash password
    user_exists = db.query(models.User).filter(models.User.email == user.email).first()
    if user_exists:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Already an Email with this account! Please Sign In')
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    
    
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    return new_user


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.UserOut)
async def get_user(id:int, db:Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User Does Not Exist')
    return user