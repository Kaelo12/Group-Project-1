from typing import Optional
from decimal import Decimal
from pydantic import BaseModel, ConfigDict
from .resources import Resource


class RecipeBase(BaseModel):
    menu_item_id: int
    resource_id: int
    amount: Decimal


class RecipeCreate(RecipeBase):
    pass


class RecipeUpdate(BaseModel):
    amount: Optional[Decimal] = None


class Recipe(RecipeBase):
    id: int
    resource: Optional[Resource] = None

    model_config = ConfigDict(from_attributes=True)