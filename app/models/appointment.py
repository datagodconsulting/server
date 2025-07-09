from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from app.database import Base

class Appointment(Base):
    __tablename__ = 'appointments'
    appointment_id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey('clients.client_id'))
    advocate_id = Column(Integer, ForeignKey('advocates.advocate_id'))
    appointment_datetime = Column(DateTime)
    meeting_link = Column(String(255), nullable=True)
    status = Column(String(20), default='Scheduled')
    notes = Column(Text, nullable=True)
    client = relationship('Client')
    advocate = relationship('Advocate') 