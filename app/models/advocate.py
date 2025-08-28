from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Advocate(Base):
    __tablename__ = 'advocates'
    advocate_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), unique=True)
    bar_council_id = Column(String(50))
    specialization = Column(String(100))
    years_of_experience = Column(Integer)
    # FK to location
    location_id = Column(Integer, ForeignKey("locations.location_id"), nullable=True)

    # relationship
    location = relationship("Location", backref="advocates")
    user = relationship('User') 