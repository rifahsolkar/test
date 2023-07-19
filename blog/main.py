from fastapi import FastAPI, Depends, status, Response, HTTPException, File, UploadFile, Form
import schemas, models
from database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session
from typing import List
import hashing
from hashing import Hash
from routers import blog, user, authentication

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# @app.post('/blog',status_code=status.HTTP_201_CREATED)
# def create(rhttp://127.0.0.1:8000equest:schemas.Blog,db:Session = Depends(get_db)):
#     new_blog = models.Blog(title=request.title,body=request.body)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog


# @app.delete('/blog/{id}',status_code = status.HTTP_204_NO_CONTENT,tags=['blogs'])
# def destroy(id,db:Session = Depends(get_db)):
#     db.query(models.Blog).filter(models.Blog.id==id).delete(synchronize_session = False)
#     db.commit()
#     return 'done'


# @app.put('/blog/{id}',status_code = status.HTTP_202_ACCEPTED,tags=['blogs'])
# def update(id, request : schemas.Blog, db:Session = Depends(get_db)):
#     db.query(models.Blog).filter(models.Blog.id == id).update(request)
#     db.commit()
#     return 'Updated successfully'



# @app.get('/blog',response_model=List[schemas.ShowBlog],tags=['blogs'])
# def all(db:Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs

# @app.get('/blog/{id}',status_code=200, response_model = schemas.ShowBlog,tags=['blogs'])
# def show(id,response:Response, db:Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blog:
#         # response.status_code = status.HTTP_404_NOT_FOUND 
#         # return {'details': f'Blog with id {id} is not available'}
#         raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
#         detail=f'Blog with id {id} is not available')

#     return blog


# @app.post('/files/')
# async def create_new_file(file:UploadFile = File(...)):
#     return {'Name of file ': file.filename}


# @app.post('/login')
# async def login(username:str = Form(...),password:str = Form(...)):
#     print("password ",password)
#     return {'username': username}

@app.post('/blog',tags=['blogs'])
def create(request : schemas.Blog, db: Session =Depends(get_db)):
    new_blog = models.Blog(title = request.title, body = request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


# @app.post('/user',response_model=schemas.ShowUser,tags=['users'])
# def create_user(request : schemas.User, db: Session =Depends(get_db)):
#     hashed_pswd = Hash.bcrypt(request.password)
#     new_user = models.User(user= request.user, email= request.email,password=hashed_pswd )
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# @app.get('/user/{id}',response_model=schemas.ShowUser,tags=['users'])
# def get_user(id:int,db: Session =Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()
#     if not user:
#         raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail=f'User with id {id} is not available')
#     return user

# @app.delete('/user/{id}',status_code = status.HTTP_204_NO_CONTENT,tags=['users'])
# def destroy(id,db:Session = Depends(get_db)):
#     db.query(models.User).filter(models.User.id==id).delete(synchronize_session = False)
#     db.commit()
#     return 'done'