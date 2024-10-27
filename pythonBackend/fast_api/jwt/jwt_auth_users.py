from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from passlib.context import CryptContext
import jwt

# --------------------------- DEFINITIONS ---------------------------

app = FastAPI()
oauth2 = OAuth2PasswordBearer(tokenUrl="login")

encrypt_algorithm = "HS256"
crypt = CryptContext(schemes=["bycrypt"])

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

    if not form.password == user.password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect password")
    
    return {"access_token": user.username, "token_type":"bearer"}