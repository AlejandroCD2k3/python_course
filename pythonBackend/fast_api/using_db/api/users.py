from fastapi import APIRouter, HTTPException, status
from db.entity_models.user import User
from db.schemas.user import user_schema, users_schema
from db.client import db_client
from bson import ObjectId


router = APIRouter(prefix="/userdb", tags=["userdb"], responses={404: {"message":"Not found"}})

users_list = []

# ----------------------- CREATE -----------------------

@router.post("/", response_model=User ,status_code=201)
async def user(user: User):
    
    if type(search_user("email", user.email)) == User:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exists")

    user_dict = dict(user)
    del user_dict["id"]

    id = db_client.local.users.insert_one(user_dict).inserted_id

    new_user = user_schema(db_client.local.users.find_one({"_id":id}))

    return User(**new_user)

# ----------------------- READ -----------------------

@router.get("/users", response_model=list[User])
async def usersdb():
    return users_schema(db_client.local.users.find())

# Path

@router.get("/{id}")
async def user(id: str):
    return search_user("_id", ObjectId(id))

# Query

@router.get("/")
async def userquery(id: str):
    return search_user("_id", ObjectId(id))

# ----------------------- UPDATE -----------------------

@router.put("/")

async def user(user: User):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True

    if not found:
        return "Error: user not found"

# ----------------------- DELETE -----------------------

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)

async def user(id: str):

    found = db_client.local.users.find_one_and_delete({"_id": ObjectId(id)})

    if not found:
        return "Error: user not deleted"

# ----------------------- FUNCTIONS -----------------------

def search_user(field: str, key):
    
    try:
        user = user_schema(db_client.local.users.find_one({field:key}))
        return User(**user)
    except:
        return "{'Error: user not found'}"
