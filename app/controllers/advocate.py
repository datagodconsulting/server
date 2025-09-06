from app.models.advocate import Advocate
from app.models.locations import Location
from app.schemas.advocate import AdvocateCreate
from sqlalchemy.orm import Session, joinedload
from fastapi import HTTPException

def create_advocate(db: Session, advocate: AdvocateCreate):
    # 1. create location
    new_location = Location(
        city=advocate.location.city,
        state=advocate.location.state,
        pincode=advocate.location.pincode,
        country="India"  # default if needed
    )
    db.add(new_location)
    db.commit()
    db.refresh(new_location)

    # 2. create advocate with linked location_id
    new_advocate = Advocate(
        user_id=advocate.user_id,
        bar_council_id=advocate.bar_council_id,
        specialization=advocate.specialization,
        years_of_experience=advocate.years_of_experience,
        location_id=new_location.location_id
    )
    db.add(new_advocate)
    db.commit()
    db.refresh(new_advocate)
    
    # Load the location relationship for the response
    db.refresh(new_advocate)
    return db.query(Advocate).options(joinedload(Advocate.location)).filter(Advocate.advocate_id == new_advocate.advocate_id).first()

def get_advocate(db: Session, advocate_id: int):
    advocate = db.query(Advocate).options(joinedload(Advocate.location)).filter(Advocate.advocate_id == advocate_id).first()
    if not advocate:
        raise HTTPException(status_code=404, detail="Advocate not found")
    return advocate

def get_advocates(db: Session):
    return db.query(Advocate).options(joinedload(Advocate.location)).all()

def update_advocate(db: Session, advocate_id: int, advocate: AdvocateCreate):
    db_advocate = get_advocate(db, advocate_id)
    for key, value in advocate.dict().items():
        if key != 'location':  # Skip location as it's handled separately
            setattr(db_advocate, key, value)
    db.commit()
    db.refresh(db_advocate)
    return db.query(Advocate).options(joinedload(Advocate.location)).filter(Advocate.advocate_id == advocate_id).first()

def delete_advocate(db: Session, advocate_id: int):
    db_advocate = get_advocate(db, advocate_id)
    db.delete(db_advocate)
    db.commit()
    return db_advocate 