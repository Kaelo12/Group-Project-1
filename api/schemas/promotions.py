from typing import Optional
from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, ConfigDict, Field


class PromotionBase(BaseModel):
    code: str
    expiration_date: datetime
    discount_percent: Decimal = Field(default=0, ge=0, le=100)


class PromotionCreate(PromotionBase):
    pass


class PromotionUpdate(BaseModel):
    code: Optional[str] = None
    expiration_date: Optional[datetime] = None
    discount_percent: Optional[Decimal] = Field(default=None, ge=0, le=100)


class Promotion(PromotionBase):
    id: int

    model_config = ConfigDict(from_attributes=True)