from fastapi import FastAPI, HTTPException
from pydantic import BaseModel



app = FastAPI()

@app.get("/")
def root():
    return "Gello"

items = []
@app.post("/items")
def create_item(item:str):
    items.append(item)
    return items

@app.get("/items/{item_id}")
def get_item(item_id:int):
    if item_id<len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail="Item not found")
    
@app.get("/items")
def get_items_limit(limit:int=10):
    return items[0:limit]