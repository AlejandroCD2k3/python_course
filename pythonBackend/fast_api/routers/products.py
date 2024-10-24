from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/products", tags=["products"], responses={404: {"message":"Not Found"}})

products_list = ["Product 1", "Product 2", "Product 3", "Product 4", "Product 5"]

# -------------------------- READ --------------------------

@router.get("/")
async def products():
    return products_list

@router.get("/{id}")
async def products(id: int):
    return products_list[id]