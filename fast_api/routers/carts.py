from models.Cart import Cart
from fastapi import APIRouter
from typing import List
import database.orm.cart_dao as cd

router = APIRouter(
    prefix="/carts",
    tags=["carts"]
)

@router.get("/get_carts")
async def get_carts():
    return cd.get_carts()

@router.post("/add_cart")
async def add_cart(id: int, list_of_items: List[int]):
    cart = Cart(id, list_of_items)
    return cd.add_cart(cart)

@router.post("/delete_cart")
async def delete_cart(id: int):
    cd.delete_cart(id)

@router.post("/update_cart")
async def update_cart(id: int, list_of_items: List[int]):
    cart = Cart(id, list_of_items)
    cd.update_cart(id, cart)