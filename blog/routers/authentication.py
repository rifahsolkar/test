from fastapi import FastAPI, Depends
from schemas import Login
import schemas, database, models
from sqlalchemy.orm import Session

router = FastAPI()

@router.post('/login')
def login(request : schemas.Login, db:Session = Depends(database.get_db())):
    user = db.query(models.User).filter(models.User.email == request.username)
    return 'login'