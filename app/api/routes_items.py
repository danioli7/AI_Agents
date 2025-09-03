from fastapi import APIRouter, HTTPException
from uuid import uuid4, UUID
from datetime import datetime
from typing import Dict
from app.models.item import Item, ItemCreate, ItemUpdate

router = APIRouter(prefix="/items", tags=["items"])

# "Base de datos" en memoria
DB: Dict[UUID, Item] = {}

@router.get("", response_model=list[Item])
def list_items() -> list[Item]:
    return list(DB.values())

@router.get("/{item_id}", response_model=Item)
def get_item(item_id: UUID) -> Item:
    item = DB.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    return item

@router.post("", response_model=Item, status_code=201)
def create_item(payload: ItemCreate) -> Item:
    new_item = Item(
        id=uuid4(),
        created_at=datetime.utcnow(),
        **payload.model_dump()
    )
    DB[new_item.id] = new_item
    return new_item

@router.put("/{item_id}", response_model=Item)
def update_item(item_id: UUID, payload: ItemUpdate) -> Item:
    item = DB.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    data = item.model_dump()
    data.update(payload.model_dump(exclude_unset=True))
    updated = Item(**data)
    DB[item_id] = updated
    return updated

@router.delete("/{item_id}", status_code=204)
def delete_item(item_id: UUID) -> None:
    if item_id not in DB:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    del DB[item_id]
