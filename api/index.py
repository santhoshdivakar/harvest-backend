from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://harvest-festival-auction.vercel.app"],  # Replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# This will serve as our simple database
items = []

class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: str

@app.get("/api")
async def root():
    return {"message": "Welcome to the FastAPI server on Vercel!"}

@app.get("/api/items", response_model=List[Item])
async def get_items():
    return items

@app.get("/api/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    item = next((item for item in items if item.id == item_id), None)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.post("/api/items", response_model=Item)
async def create_item(item: Item):
    item.id = len(items) + 1
    items.append(item)
    return item

@app.put("/api/items/{item_id}", response_model=Item)
async def update_item(item_id: int, updated_item: Item):
    for i, item in enumerate(items):
        if item.id == item_id:
            updated_item.id = item_id
            items[i] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

# For demonstration purposes, let's add a few items
items.extend([
    Item(id=1, name="Laptop", description="A portable computer"),
    Item(id=2, name="Smartphone", description="A mobile device"),
    Item(id=3, name="Tablet", description="A touchscreen device")
])

