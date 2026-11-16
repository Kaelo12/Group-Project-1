from typing import Optional
from decimal import Decimal
from pydantic import BaseModel, ConfigDict


class ResourceBase(BaseModel):
    name: str
    amount: Decimal
    unit: str


class ResourceCreate(ResourceBase):
    pass


class ResourceUpdate(BaseModel):
    name: Optional[str] = None
    amount: Optional[Decimal] = None
    unit: Optional[str] = None


class Resource(ResourceBase):
    id: int

    model_config = ConfigDict(from_attributes=True)