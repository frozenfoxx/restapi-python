#!/usr/bin/env python3

if __package__:
    from .guestbook import Guestbook
else:
    from guestbook import Guestbook
from fastapi import FastAPI, HTTPException
from typing import Optional
import datetime

app = FastAPI()
guestbook = Guestbook()

@app.get("/")
async def read_root():
    return {"msg": "Welcome to the guestbook"}

@app.get("/signatures")
async def read_signatures():
    try:
        return guestbook.signatures
    except RuntimeError:
         raise HTTPException(status_code=500, detail="Issue retrieving the signatures")

@app.post("/signatures/{id}")
async def create_signature(id):
    try:
        return guestbook.add(id)
    except RuntimeError:
        raise HTTPException(status_code=409, detail="Signature already exists")

@app.get("/signatures/{id}")
async def read_signature(id: str):
    try:
        return guestbook.signatures[id]
    except RuntimeError as e:
        raise HTTPException(status_code=404, detail="Unable to locate signature")

@app.put("/signatures/{id}")
async def update_signature(id: str):
    try:
        return guestbook.update(id)
    except RuntimeError:
        raise HTTPException(status_code=401, detail="Unable to update signature")

@app.delete("/signatures/{id}")
async def delete_signature(id: str):
    try:
        return guestbook.delete(id)
    except RuntimeError:
        raise HTTPException(status_code=401, detail="Unable to delete signature")

if __name__ == "__main__":
    app.run()
