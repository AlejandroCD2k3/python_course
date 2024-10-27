from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel

app = FastAPI()
oauth2 = OAuth2PasswordBearer(tokenUrl="login")

class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool

class DBUser(User):
    password: str

users_db = {
    "simon123": {
        "username": "simon123",
        "full_name": "Simon Lamberdt",
        "email": "simon123@gmail.com",
        "disabled": False,
        "password": "123456"
    },

    "arthur321": {
        "username": "arthur321",
        "full_name": "Arthur Bonnet",
        "email": "arthur321@gmail.com",
        "disabled": True,
        "password": "654321"
    }
}