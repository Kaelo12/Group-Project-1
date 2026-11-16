from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, CheckConstraint
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class Review(Base):
    __tablename__ = "reviews"
    __table_args__ = (
        CheckConstraint("score >= 1 AND score <= 5", name="ck_review_score_range"),
    )

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    menu_item_id = Column(Integer, ForeignKey("menu_items.id"), nullable=False)
    score = Column(Integer, nullable=False)  # 1 to 5
    review_text = Column(String(500))
    review_date = Column(DateTime, server_default=func.now())

    customer = relationship("Customer", back_populates="reviews")
    menu_item = relationship("MenuItem", back_populates="reviews")