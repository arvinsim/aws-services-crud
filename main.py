from typing import Any
from fastapi import FastAPI
from prisma import Prisma
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/users")
async def users():
    db = Prisma()
    await db.connect()
    users_response = await db.userdetails.find_many()
    return users_response
@app.get("/users/{id}")
async def user(id: int):
    db = Prisma()
    await db.connect()
    user_response = await db.userdetails.find_unique(where={"id": id})
    return user_response

@app.post("/users")
async def create_user(user):
    # TODO
    return {"message": "To be implemented"}

@app.put("/users/{id}")
async def edit_user(id: int, user) -> Any:
    # TODO
    return {"message": "To be implemented"}

@app.delete("/users/{id}")
async def delete_user(id: int):
    db = Prisma()
    await db.connect()
    user_response = await db.userdetails.delete(where={"id": id})
    return user_response
