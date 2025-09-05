from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DECIMAL, Text, Date, TIMESTAMP
from sqlalchemy.orm import relationship
from app.database import Base

class Advocate(Base):
    __tablename__ = 'advocates'
    advocate_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), unique=True)
    bar_council_id = Column(String(50))
    specialization = Column(String(100))
    years_of_experience = Column(Integer)
    available_emergency = Column(Boolean, nullable=True)
    consultation_fee = Column(DECIMAL(10, 2), nullable=True)
    profile_picture = Column(String(500), nullable=True)
    # education_details = Column(Text, nullable=True)
    in_house_lawyer = Column(Boolean, nullable=True)
    # FK to location
    location_id = Column(Integer, ForeignKey("locations.location_id"), nullable=True)
    location = relationship("Location", backref="advocates")
    user = relationship('User') 