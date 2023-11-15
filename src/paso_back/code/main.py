from fastapi import FastAPI

app = FastAPI()

items = []

@app.get("/")
def read_root():
    return {"message": "¡Hola, FastAPI!"}

@app.get("/items")
def read_items():
    return {"items": items}

@app.post("/items")
def create_item(item: str):
    items.append(item)
    return {"item": item}

@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item: str):
    if 0 <= item_id < len(items):
        items[item_id] = updated_item
        return {"item_id": item_id, "item": updated_item}
    return {"error": "Índice fuera de rango"}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if 0 <= item_id < len(items):
        deleted_item = items.pop(item_id)
        return {"item_id": item_id, "deleted_item": deleted_item}
    return {"error": "Índice fuera de rango"}