from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base
from pydantic import BaseModel


class Department(Base):
    __tablename__ = "departments"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    org_id = Column(Integer, ForeignKey("organizations.id"))

    organization = relationship("Organization", back_populates="departments")


class DeptCreate(BaseModel):
    name: str
    org_id: int
