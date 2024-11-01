from fastapi import FastAPI
from . import users

app = FastAPI()

# --------------- ROUTERS ---------------

app.include_router(users.router)

# --------------- READ ---------------

@app.get("/")
async def root():
    return "Welcome!"
