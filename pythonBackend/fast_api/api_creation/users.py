from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Start server with: python -m uvicorn users:app --reload

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

@app.post("/user/", response_model=User ,status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=204, detail="User already exists")
    else:
        users_list.append(user)
    
# ----------------------- READ -----------------------

@app.get("/users_json")
async def users_json():
    return {{"name":"Michael", "lastname":"Washington", "age": 20, "url":"https://michael.dev/"},
            {"name":"Alex", "lastname":"Smith", "age": 25, "url":"https://alex.dev/"},
            {"name":"Ashley", "lastname":"Taylor", "age": 21, "url":"https://ashley.dev/"}}

@app.get("/users")
async def user():
    return users_list

# Path

@app.get("/user/{id}")
async def user(id: int):
    return search_user(id)

# Query

@app.get("/user/")
async def userquery(id: int):
    return search_user(id)

# ----------------------- UPDATE -----------------------

@app.put("/user/")

async def user(user: User):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True

    if not found:
        return "Error: user not found"

# ----------------------- DELETE -----------------------

@app.delete("/user/{id}")

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

"""
@app.get("users")
async def users():
    return User(name = "Michael", lastname = "Washington", age = 20, url = "https://michael.dev/")
"""


