from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

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

# 

@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    
    user_db = users_db.get(form.username)

    if not user_db():
        raise HTTPException(status_code=400, detail="User not found")
    
    user = search_user(form.username)
    if not form.password == user.password:
        raise HTTPException(status_code=400, detail="Incorrect password")

    return {"access_token": user.username, "token_type":"bearer"}