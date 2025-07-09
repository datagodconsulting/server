from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class Case(Base):
    __tablename__ = 'cases'
    case_id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey('clients.client_id'))
    advocate_id = Column(Integer, ForeignKey('advocates.advocate_id'), nullable=True)
    case_type = Column(String(100))
    case_status = Column(String(20), default='Open')
    case_description = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    client = relationship('Client')
    advocate = relationship('Advocate') 