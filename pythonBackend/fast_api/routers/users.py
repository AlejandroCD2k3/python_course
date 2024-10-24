from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

# Start server with: python -m uvicorn users:router --reload

# User Entity

class User(BaseModel):
    id: int
    name: str
    lastname: str
    age: int
    url: str

# Database table for users

users_list = [User(id = 1, name="Michael",lastname="Washington",age=20, url="https://michael.dev/"),
              User(id = 2, name="Alex",lastname="Smith",age=25, url="https://alex.dev/"),
              User(id = 3, name="Ashley",lastname="Taylor",age=21, url="https://ashley.dev/")]


# ----------------------- CREATE -----------------------

@router.post("/user/", response_model=User ,status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=204, detail="User already exists")
    else:
        users_list.routerend(user)
    
# ----------------------- READ -----------------------

@router.get("/users")
async def user():
    return users_list

# Path

@router.get("/user/{id}")
async def user(id: int):
    return search_user(id)

# Query

@router.get("/user/")
async def userquery(id: int):
    return search_user(id)

# ----------------------- UPDATE -----------------------

@router.put("/user/")

async def user(user: User):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True

    if not found:
        return "Error: user not found"

# ----------------------- DELETE -----------------------

@router.delete("/user/{id}")

async def user(id: int):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True

    if not found:
        return "Error: user not deleted"

# ----------------------- FUNCTIONS -----------------------

def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return "{'Error: user not found'}"
