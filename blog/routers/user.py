from fastapi import APIRouter,Depends, HTTPException, status, Response
import schemas, models
# import database
import database, schemas
from typing import List
from sqlalchemy.orm import Session
from database import engine, SessionLocal, get_db
from repository import user


router = APIRouter(
    prefix = '/user',
    tags=['users']
)

@router.post('/',response_model=schemas.ShowUser)
def create_user(request : schemas.User, db: Session =Depends(get_db)):
    return user.create(request,db)

@router.get('/{id}',response_model=schemas.ShowUser)
def get_user(id:int,db: Session =Depends(get_db)):
    return user.get(id,db)

@router.delete('/{id}',status_code = status.HTTP_204_NO_CONTENT)
def destroy(id,db:Session = Depends(get_db)):
    return user.destroy(id,db)