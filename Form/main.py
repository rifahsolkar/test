from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
import requests
from fastapi.encoders import jsonable_encoder


app = FastAPI()
templates = Jinja2Templates(directory = 'templates')

# @app.get('/')
# def index():
#     return 'Hello'

@app.get('/')
def registration(request : Request):
    return templates.TemplateResponse('user_register.html',{'request':request})

@app.post('/display/')
def display(email: str= Form(...),password: str= Form(...)):
    print(email,password)
    data1 = {
        'display_email' : email,
        'display_pswd' : password
    }
    data = jsonable_encoder(data1)
    # response = requests.post(url='http://127.0.0.1:8000/display',json=data)
    # response = requests.
    return f'email is {email} and password is {password}'
    # return JSONResponse(data)
# if __name__=='main':
    # app.run(host='0.0.0.0',port=8000, debug=True)
