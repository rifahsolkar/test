from sqlalchemy.orm import Session
import models, schemas, database
from fastapi import APIRouter,Depends, HTTPException, status, Response
from database import engine, SessionLocal, get_db
# import Hash
from passlib.context import CryptContext
from hashing import Hash

# pwd_context = CryptContext(schemes=[bcrypt],deprecated='auto')


def create(request : schemas.User, db: Session =Depends(get_db)):
    hashed_pswd = Hash.bcrypt(request.password)
    new_user = models.User(user= request.user, email= request.email,password=hashed_pswd )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get(id:int,db: Session =Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail=f'User with id {id} is not available')
    return user

def destroy(id,db:Session = Depends(get_db)):
    db.query(models.User).filter(models.User.id==id).delete(synchronize_session = False)
    db.commit()
    return 'done'

