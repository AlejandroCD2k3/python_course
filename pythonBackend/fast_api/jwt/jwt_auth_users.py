from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from passlib.context import CryptContext
from datetime import datetime, timedelta
import jwt

# --------------------------- DEFINITIONS ---------------------------

app = FastAPI()
oauth2 = OAuth2PasswordBearer(tokenUrl="login")

encrypt_algorithm = "HS256"
crypt = CryptContext(schemes=["bcrypt"])
access_token_duration = 1

# --------------------- ENTITIES ---------------------

class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool

class DBUser(User):
    password: str

# --------------------- FAKE DATA BASE ---------------------

users_db = {
    "simon123": {
        "username": "simon123",
        "full_name": "Simon Lamberdt",
        "email": "simon123@gmail.com",
        "disabled": False,
        "password": "$2a$12$KK9KT8mwqUhIwZMN0eSqJ.LrKTS65Co/ipDYVvtU5PJetdwSIwt3W"
    },

    "arthur321": {
        "username": "arthur321",
        "full_name": "Arthur Bonnet",
        "email": "arthur321@gmail.com",
        "disabled": True,
        "password": "$2a$12$oJg7RZ7yh1sZkvNLVTi/5Ox/AWcBi1CMA5NQ5z2IOXGZj2GyKmKsG"
    }
}

# --------------------------- FUNCTIONS ---------------------------


def search_user_db(username: str):
    if username in users_db:
        return DBUser(**users_db[username])

# --------------------------- CREATE ---------------------------

@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):

    user_db = users_db.get(form.username)

    if not user_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User not found")
    
    user = search_user_db(form.username)

    if not crypt.verify(form.password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect password")
    
    access_token = {"sub":user.username, 
                    "exp":datetime.utcnow() + timedelta(minutes=access_token_duration)}

    return {"access_token": access_token, "token_type":"bearer"}