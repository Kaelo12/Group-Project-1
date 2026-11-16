from datetime import datetime
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, ConfigDict
from .order_details import OrderDetail
from .payments import Payment


class OrderBase(BaseModel):
    customer_id: int
    promotion_id: Optional[int] = None
    order_type: str = "takeout"
    description: Optional[str] = None


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    status: Optional[str] = None
    order_type: Optional[str] = None
    promotion_id: Optional[int] = None
    description: Optional[str] = None


class Order(OrderBase):
    id: int
    tracking_number: str
    status: str
    total_price: Decimal
    order_date: Optional[datetime] = None
    order_details: list[OrderDetail] = []
    payment: Optional[Payment] = None

    model_config = ConfigDict(from_attributes=True)