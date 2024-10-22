from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Start server with: python -m users:app --reload

# User Entity

class User(BaseModel):
    name: str
    lastname: str
    age: int
    url: str


users_list = [User(name="Michael",lastname="Washington",age=20, url="https://michael.dev/"),
              User(name="Alex",lastname="Smith",age=25, url="https://alex.dev/"),
              User(name="Ashley",lastname="Taylor",age=21, url="https://ashley.dev/")]

@app.get("/users_json")
async def users_json():
    return {{"name":"Michael", "lastname":"Washington", "age": 20, "url":"https://michael.dev/"},
            {"name":"Alex", "lastname":"Smith", "age": 25, "url":"https://alex.dev/"},
            {"name":"Ashley", "lastname":"Taylor", "age": 21, "url":"https://ashley.dev/"}}

@app.get("/users")
async def users():
    return users_list

"""
@app.get("users")
async def users():
    return User(name = "Michael", lastname = "Washington", age = 20, url = "https://michael.dev/")
"""


