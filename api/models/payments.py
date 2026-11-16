from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"), unique=True, nullable=False)
    amount = Column(DECIMAL(8, 2), nullable=False)
    payment_type = Column(String(30), nullable=False)  # card / cash / online
    card_holder_name = Column(String(100))
    card_last_four = Column(String(4))
    transaction_status = Column(String(20), nullable=False, default="pending")
    payment_date = Column(DateTime, server_default=func.now())

    order = relationship("Order", back_populates="payment")