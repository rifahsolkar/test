from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# @app.get('/')
# def index():
#     return 'Hello'

@app.get('/')
def index():
    return 'Hey'

@app.get('/blog')
def index(limit=10,published:bool=True,sort:Optional[str]=None):
    if published:
        return {'data' : f'{limit} published blogs from db'}
    else:
        return {'data' : f'{limit} blogs from db'}
    

@app.get('/about')
def details():
    return {'data' : 'More details'}

@app.get('/blog/{id}')
def show(id:int ):
    return {'data ' : id}

@app.get('/blog/{id}/comments')
def comments(id,limit=10):
    return {'data':'comments'}


class Blog(BaseModel):
    title:str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(request: schemas.Blog , db:Session = Depends(get_db)):
    new_blog = Models.Blog(title = request.title,body=request.body)
    # return request
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


# changing port

if __name__ =='__main__':
    uvicorn.run(app,host='127.0.0.1',port='9000')
