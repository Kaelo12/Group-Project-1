from typing import Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field


class ReviewBase(BaseModel):
    customer_id: int
    menu_item_id: int
    score: int = Field(ge=1, le=5)
    review_text: Optional[str] = None


class ReviewCreate(ReviewBase):
    pass


class ReviewUpdate(BaseModel):
    score: Optional[int] = Field(default=None, ge=1, le=5)
    review_text: Optional[str] = None


class Review(ReviewBase):
    id: int
    review_date: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)