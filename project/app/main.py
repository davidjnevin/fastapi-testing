from anyio import start_blocking_portal
from fastapi import FastAPI, Header, HTTPException
from app.models import Item


fake_secret_token = "correcttoken"

fake_db = {
    "primary": {"id": "primary", "title": "Primary", "description": "The primary response"},
    "secondary": {"id": "secondary", "title": "Secondary", "description": "The secondary response"},
}

app = FastAPI()


@app.get("/ping")
async def read_ping():
    return {"msg": "pong"}

@app.get("/items/{item_id}", response_model=Item)
async def read_main(item_id: str, x_token: str = Header()):
    if x_token != fake_secret_token:
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return fake_db[item_id]

@app.post("/items/", response_model=Item)
async def create_items(item: Item, x_token: str = Header()):
    if x_token != fake_secret_token:
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
    if item.id in fake_db:
        raise HTTPException(status_code=400, detail="Item already exists")
    fake_db[item.id] = item
    return item
