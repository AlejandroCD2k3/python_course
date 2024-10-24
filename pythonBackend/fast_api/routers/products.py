from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

@router.get("/products/")
async def products():
    return ["Product 1", "Product 2", "Product 3", "Product 4", "Product 5"]