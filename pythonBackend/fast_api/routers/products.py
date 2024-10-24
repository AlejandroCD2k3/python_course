from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

@app.get("/products/")
async def products():
    return ["Product 1", "Product 2", "Product 3", "Product 4", "Product 5"]