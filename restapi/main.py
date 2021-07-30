#!/usr/bin/env python3

if __package__:
    from .guestbook import Guestbook
else:
    from guestbook import Guestbook
from typing import Optional

from fastapi import FastAPI

app = FastAPI()
guestbook = Guestbook

@app.get("/")
async def read_root():
    return {"msg": "Welcome to the guestbook"}

@app.get("/signatures")
async def read_signatures():
    return guestbook.signatures

@app.get("/signatures/{signature_id}")
async def read_signature(signature_id: str):
    return guestbook.signatures[signature_id]

if __name__ == "__main__":
    app.run()
