from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool

class DBUser(User):
    password: str

users_db = {
    "Simon": {
        "username": "simon123",
        "full_name": "Simon Lamberdt",
        "email": "simon123@gmail.com",
        "disabled": False,
        "password": "123456"
    },

    "Arthur": {
        "username": "arthur321",
        "full_name": "Arthur Bonnet",
        "email": "arthur321@gmail.com",
        "disabled": True,
        "password": "654321"
    }
}

def search_user(username: str):
    if username in users_db:
        return DBUser(users_db[username])
    return 