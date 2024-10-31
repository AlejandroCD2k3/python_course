from fastapi import FastAPI
from . import products, users, jwt_auth_users

app = FastAPI()

# --------------- ROUTERS ---------------

app.include_router(products.router)
app.include_router(users.router)
app.include_router(jwt_auth_users.router)

# --------------- READ ---------------

@app.get("/")
async def root():
    return "Welcome!"
