from sqlalchemy import Column, Integer, String, DECIMAL
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class Resource(Base):
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), unique=True, nullable=False)  # ingredient name
    amount = Column(DECIMAL(10, 2), nullable=False, default=0)  # amount in stock
    unit = Column(String(20), nullable=False)  # e.g. kg, g, liters, pieces

    recipes = relationship("Recipe", back_populates="resource")