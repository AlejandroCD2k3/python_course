from fastapi import FastAPI
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


users_list = [User(id = 1, name="Michael",lastname="Washington",age=20, url="https://michael.dev/"),
              User(id = 2, name="Alex",lastname="Smith",age=25, url="https://alex.dev/"),
              User(id = 3, name="Ashley",lastname="Taylor",age=21, url="https://ashley.dev/")]

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


