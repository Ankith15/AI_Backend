from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base
from pydantic import BaseModel

class OrgCreate(BaseModel):
    name: str


class Organization(Base):
    __tablename__ = "organizations"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    created_by = Column(String(100), nullable=False)

    departments = relationship("Department", back_populates="organization")
