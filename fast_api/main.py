from fastapi import FastAPI
from .routers import users, items, carts

app = FastAPI()

app.include_router(users.router)
app.include_router(items.router)
app.include_router(carts.router)

@app.get("/test")
def home_page():
    return "Hello Python developers"

