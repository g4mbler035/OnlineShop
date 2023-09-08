from models.Item import Item
from fastapi import APIRouter
from typing import List
import database.orm.item_dao as item_dao

router = APIRouter(
    prefix="/items",
    tags=["items"]
)

@router.get("/get_items")
async def get_users():
    return item_dao.get_items()

@router.post("/add_item")
async def add_person(id: int, name: str, price: float, quantity: int, cart_id: int):
    item = Item(id, name, price, quantity, cart_id)
    return item_dao.add_item(item)

@router.post("/delete_item")
async def delete_person(id: int):
    item_dao.delete_item(id)

@router.post("/update_item")
async def update_person(id: int, name: str, price: float, quantity: int, cart_id: int):
    item = Item(id, name, price, quantity, cart_id)
    item_dao.update_item(id, item)