from typing import Optional
from decimal import Decimal
from pydantic import BaseModel, ConfigDict
from .menu_items import MenuItem


class OrderDetailBase(BaseModel):
    menu_item_id: int
    quantity: int


class OrderDetailCreate(OrderDetailBase):
    order_id: int
    unit_price: Decimal


class OrderDetailUpdate(BaseModel):
    quantity: Optional[int] = None


class OrderDetail(OrderDetailBase):
    id: int
    order_id: int
    unit_price: Decimal
    menu_item: Optional[MenuItem] = None

    model_config = ConfigDict(from_attributes=True)