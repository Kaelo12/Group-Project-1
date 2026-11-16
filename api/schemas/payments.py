from typing import Optional
from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, ConfigDict, Field


class PaymentBase(BaseModel):
    order_id: int
    amount: Decimal
    payment_type: str
    card_holder_name: Optional[str] = None
    card_last_four: Optional[str] = Field(default=None, min_length=4, max_length=4)


class PaymentCreate(PaymentBase):
    pass


class PaymentUpdate(BaseModel):
    transaction_status: Optional[str] = None


class Payment(PaymentBase):
    id: int
    transaction_status: str
    payment_date: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)