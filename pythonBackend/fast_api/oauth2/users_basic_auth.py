from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

# # --------------------------- DEFINITIONS ---------------------------

app = FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

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
    
def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])

async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED, detail="Invalid auth credentials", headers={"WWW-Authenticate":"Bearer"})
    
    if user.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Disabled user")
    
    return user

# ----------------------------- CREATE -----------------------------

@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    
    user_db = users_db.get(form.username)

    if not user_db:
        raise HTTPException(status_code=400, detail="User not found")
    
    user = search_user_db(form.username)
    if not form.password == user.password:
        raise HTTPException(status_code=400, detail="Incorrect password")

    return {"access_token": user.username, "token_type":"bearer"}

# ----------------------------- READ -----------------------------

@app.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user