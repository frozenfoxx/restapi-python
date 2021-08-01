#!/usr/bin/env python3

if __package__:
    from .guestbook import Guestbook
else:
    from guestbook import Guestbook
from fastapi import FastAPI
from typing import Optional
import datetime

app = FastAPI()
guestbook = Guestbook

@app.get("/")
async def read_root():
    return {"msg": "Welcome to the guestbook"}

@app.get("/signatures")
async def read_signatures():
    return guestbook.signatures

@app.post("/signatures/{signature_id}")
async def create_signature(signature_id: str):
    return guestbook.add(signature_id)

@app.get("/signatures/{signature_id}")
async def read_signature(signature_id: str):
    return guestbook.signatures[signature_id]

@app.put("/signatures/{signature_id}")
async def update_signature(signature_id: str):
    return guestbook.update(signature_id)

@app.delete("/signatures/{signature_id}")
async def delete_signature(signature_id: str):
    return guestbook.delete(signature_id)

if __name__ == "__main__":
    app.run()
