from pydantic import BaseModel, Field
from typing import Optional, List
from uuid import UUID
from datetime import datetime

class ItemBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    price: float = Field(..., gt=0)
    tags: List[str] = []

class ItemCreate(ItemBase):
    description: Optional[str] = None

class ItemUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=3, max_length=50)
    price: Optional[float] = Field(None, gt=0)
    tags: Optional[List[str]] = None
    description: Optional[str] = None

class Item(ItemBase):
    id: UUID
    created_at: datetime
