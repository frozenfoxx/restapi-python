#!/usr/bin/env python3

if __package__:
    from .guestbook import Guestbook
else:
    from guestbook import Guestbook
from fastapi import FastAPI
from typing import Optional
import datetime

app = FastAPI()
guestbook = Guestbook()

@app.get("/")
async def read_root():
    return {"msg": "Welcome to the guestbook"}

@app.get("/signatures")
async def read_signatures():
    return guestbook.signatures

@app.post("/signatures/{id}")
async def create_signature(id):
    return guestbook.add(id)

@app.get("/signatures/{id}")
async def read_signature(id: str):
    return guestbook.signatures[id]

@app.put("/signatures/{id}")
async def update_signature(id: str):
    return guestbook.update(id)

@app.delete("/signatures/{id}")
async def delete_signature(id: str):
    return guestbook.delete(id)

if __name__ == "__main__":
    app.run()
