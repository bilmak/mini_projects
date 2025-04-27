from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class Item(BaseModel):
    text: str | None = None
    is_done: bool = False


app = FastAPI()


@app.get("/")
def root():
    return "Hello"


items = []


@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return items


@app.get("/items", response_model=list[Item])
def get_list_items(limit: int = 10):
    return items[0:limit]


@app.get("/items/{item_id}", response_model=list[Item])
def get_item(item_id: int) -> Item:
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail="Item not found")
