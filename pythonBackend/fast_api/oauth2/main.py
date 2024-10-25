from fastapi import FastAPI
import products
import users

app = FastAPI()

# --------------- ROUTERS ---------------

app.include_router(products.router)
app.include_router(users.router)

# --------------- READ ---------------

@app.get("/")
async def root():
    return "Welcome!"