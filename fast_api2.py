from fastapi import FastAPI, Path, HTTPException
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None
    
class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float]=None
    brand: Optional[str] = None


inventory = {
    1: {
        "name": "Milk",
        "price": 3.99,
        "brand": "Mlekovita"
    }
}

@app.get("/getall")
def get_all():
    return inventory

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(description="The ID of the item")):
    if item_id in inventory:
        return inventory[item_id]
    raise HTTPException(status_code=404, detail="Item is not found")


@app.get("/get-by-name")
def get_by_name(name: Optional[str] = None):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    raise HTTPException(status_code=404)

@app.post("/create-item/{item_id}")
def create_item(item_id:int, item: Item):
    if item_id in inventory:
        raise HTTPException(status_code=400, detail="This ID is exists")
    inventory[item_id]= {"name": item.name, "price":item.price, "brand": item.brand}
    return inventory[item_id]

@app.put("/update-item/{item_id}")
def update_item(item_id: int, item:UpdateItem ):
    if item_id not in inventory:
        raise HTTPException(status_code=404)
    if item.name != None:
        inventory[item_id]["name"] = item.name
    if item.price != None:
        inventory[item_id]["price"] = item.price
    if item.brand != None:
        inventory[item_id]["brand"] = item.brand
        
    return inventory[item_id]

@app.delete("/delete/{item_id}")
def delete_item(item_id: int):
    if item_id not in inventory:
        raise HTTPException(status_code=404)
    del inventory[item_id]
    return {"message": f"Item {item_id} successfully deleted"}
        
        
