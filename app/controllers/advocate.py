from app.models.advocate import Advocate
from app.schemas.advocate import AdvocateCreate
from sqlalchemy.orm import Session
from fastapi import HTTPException

def create_advocate(db: Session, advocate: AdvocateCreate):
    db_advocate = Advocate(**advocate.dict())
    db.add(db_advocate)
    db.commit()
    db.refresh(db_advocate)
    return db_advocate

def get_advocate(db: Session, advocate_id: int):
    advocate = db.query(Advocate).filter(Advocate.id == advocate_id).first()
    if not advocate:
        raise HTTPException(status_code=404, detail="Advocate not found")
    return advocate

def get_advocates(db: Session):
    return db.query(Advocate).all()

def update_advocate(db: Session, advocate_id: int, advocate: AdvocateCreate):
    db_advocate = get_advocate(db, advocate_id)
    for key, value in advocate.dict().items():
        setattr(db_advocate, key, value)
    db.commit()
    db.refresh(db_advocate)
    return db_advocate

def delete_advocate(db: Session, advocate_id: int):
    db_advocate = get_advocate(db, advocate_id)
    db.delete(db_advocate)
    db.commit()
    return db_advocate 