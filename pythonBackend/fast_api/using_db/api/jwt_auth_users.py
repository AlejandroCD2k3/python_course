from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from passlib.context import CryptContext
from datetime import datetime, timedelta
import jwt
from jwt.exceptions import InvalidTokenError

# --------------------------- DEFINITIONS ---------------------------

router = APIRouter(prefix="/login", tags=["login"], responses={404:{"message":"Not found"}})
oauth2 = OAuth2PasswordBearer(tokenUrl="login")

encrypt_algorithm = "HS256"
secret = "e1f53135e559c25302a15e8a1fae7a1a45162dbe7420d9fa1b7f6ff2c8eaea4d"
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
    
def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])
    
async def auth_user(token: str = Depends(oauth2)):
    
    invalid_token_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials", headers={"WWW-Authenticate":"Bearer"})

    try:
        username = jwt.decode(token, secret, algorithms=[encrypt_algorithm]).get("sub")
    
        if username is None:
            raise invalid_token_exception
         
    except InvalidTokenError:
        raise invalid_token_exception
    
    return search_user(username)

async def current_user(user: User = Depends(auth_user)):
    if user.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Disabled user")
    return user

# --------------------------- CREATE ---------------------------

@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):

    user_db = users_db.get(form.username)

    if not user_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User not found")
    
    user = search_user_db(form.username)

    if not crypt.verify(form.password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect password")
    
    access_token = {"sub":user.username, 
                    "exp":datetime.utcnow() + timedelta(minutes=access_token_duration)}

    return {"access_token": jwt.encode(access_token, secret,  algorithm=encrypt_algorithm), "token_type":"bearer"}

# --------------------------- READ ---------------------------

@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user