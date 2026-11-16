from uuid import uuid4
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, DECIMAL
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


def generate_tracking_number():
    return uuid4().hex[:12].upper()


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    promotion_id = Column(Integer, ForeignKey("promotions.id"), nullable=True)
    tracking_number = Column(String(20), unique=True, nullable=False,
                             default=generate_tracking_number)
    order_date = Column(DateTime, nullable=False, server_default=func.now())
    status = Column(String(30), nullable=False, default="pending")
    order_type = Column(String(20), nullable=False, default="takeout")  # dine-in / takeout / delivery
    total_price = Column(DECIMAL(8, 2), nullable=False, default=0)
    description = Column(String(300))

    customer = relationship("Customer", back_populates="orders")
    promotion = relationship("Promotion", back_populates="orders")
    order_details = relationship("OrderDetail", back_populates="order")
    payment = relationship("Payment", back_populates="order", uselist=False)