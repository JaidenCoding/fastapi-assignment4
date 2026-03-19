from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Part 2: Item class
class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

# Part 1: Root endpoint
@app.get("/")
def read_root():
    return {"Hello": "World"}

# Part 1: GET with path + query parameter
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# Part 2: PUT request
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {
        "item_name": item.name,
        "item_price": item.price,
        "is_offer": item.is_offer,
        "item_id": item_id
    }