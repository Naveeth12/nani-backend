from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from database import Base


# =====================================
# USER TABLE
# =====================================
class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    email = Column(String(150), unique=True, index=True, nullable=False)

    branch = Column(String(100), nullable=False)

    domain = Column(String(100), nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationship
    interviews = relationship("Interview", back_populates="user")


# =====================================
# INTERVIEW TABLE
# =====================================
class Interview(Base):

    __tablename__ = "interviews"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    question = Column(Text, nullable=False)

    answer = Column(Text, nullable=False)

    score = Column(Integer)

    weak_areas = Column(Text)

    suggestions = Column(Text)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationship
    user = relationship("User", back_populates="interviews")