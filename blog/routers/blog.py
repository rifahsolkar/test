from fastapi import APIRouter,Depends, HTTPException, status, Response
import schemas, models
# import database
import database, schemas
from typing import List
from sqlalchemy.orm import Session
from database import engine, SessionLocal, get_db
from repository import blog


router = APIRouter(
    prefix = '/blog',
    tags=['blogs']
)

@router.get('/',response_model=List[schemas.ShowBlog])
def all(db:Session = Depends(database.get_db)):
    return blog.get_all(db)


# @router.post('/',status_code=status.HTTP_201_CREATED)
# def create(request : schemas.Blog, db:Session = Depends(get_db)):
#     return blog.create(request,db)


@router.delete('/{id}',status_code = status.HTTP_204_NO_CONTENT)
def destroy(id,db:Session = Depends(get_db)):
    return blog.destroy(id,db)
    


@router.put('/{id}',status_code = status.HTTP_202_ACCEPTED)
def update(id, request : schemas.Blog, db:Session = Depends(get_db)):
    return blog.update(id,request,db)
    


@router.get('/{id}',status_code=200, response_model = schemas.ShowBlog)
def show(id,response:Response, db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        # response.status_code = status.HTTP_404_NOT_FOUND 
        # return {'details': f'Blog with id {id} is not available'}
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
        detail=f'Blog with id {id} is not available')
    return blog