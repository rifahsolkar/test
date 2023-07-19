from sqlalchemy.orm import Session
import models, schemas
from fastapi import APIRouter,Depends, HTTPException, status, Response
from database import engine, SessionLocal, get_db


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


# def create(request: schemas.Blog, db: Session):
#     new_blog = models.Blog(title=request.title,body=request.body)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog

def destroy(id:int,db:Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id==id).delete(synchronize_session = False)
    db.commit()
    return 'done'

def update(id:int, request : schemas.Blog, db:Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id == id).update(request)
    db.commit()
    return 'Updated successfully'