from models.User import User
from fastapi import APIRouter
from typing import List
import database.orm.user_dao as ud

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("/get_users")
async def get_users():
    return ud.get_users()

@router.post("/add_user")
async def add_person(id: int, first_name: str, last_name: str, email: str, list_of_items: List[int]):
    user = User(id, first_name, last_name, email, list_of_items)
    return ud.add_user(user)

@router.post("/delete_user")
async def delete_person(first_name: str, last_name: str):
    ud.delete_user(first_name, last_name)

@router.post("/update_user")
async def update_person(id: int, first_name: str, last_name: str, email: str, list_of_items: List[int]):
    user = User(id, first_name, last_name, email, list_of_items)
    ud.update_user(id, user)