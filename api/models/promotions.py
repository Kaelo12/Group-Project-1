from sqlalchemy import Column, Integer, String, DateTime, DECIMAL, CheckConstraint
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class Promotion(Base):
    __tablename__ = "promotions"
    __table_args__ = (
        CheckConstraint("discount_percent >= 0 AND discount_percent <= 100",
                        name="ck_promotion_discount_range"),
    )

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    code = Column(String(30), unique=True, nullable=False)
    expiration_date = Column(DateTime, nullable=False)
    discount_percent = Column(DECIMAL(5, 2), nullable=False, default=0)

    orders = relationship("Order", back_populates="promotion")