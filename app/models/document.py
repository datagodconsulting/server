from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class Document(Base):
    __tablename__ = 'documents'
    document_id = Column(Integer, primary_key=True, index=True)
    case_id = Column(Integer, ForeignKey('cases.case_id'))
    uploaded_by_id = Column(Integer, ForeignKey('users.user_id'))
    file_url = Column(String(255))
    document_type = Column(String(100))
    uploaded_at = Column(DateTime(timezone=True), server_default=func.now())
    case = relationship('Case')
    uploaded_by = relationship('User') 