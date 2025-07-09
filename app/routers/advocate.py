from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.advocate import AdvocateCreate, AdvocateRead
from app.controllers.advocate import create_advocate, get_advocate, get_advocates, update_advocate, delete_advocate
from app.database import SessionLocal
from typing import List

router = APIRouter(prefix="/advocates", tags=["advocates"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[AdvocateRead])
def list_advocates(db: Session = Depends(get_db)):
    return get_advocates(db)

@router.post("/", response_model=AdvocateRead)
def create_new_advocate(advocate: AdvocateCreate, db: Session = Depends(get_db)):
    return create_advocate(db, advocate)

@router.get("/{advocate_id}", response_model=AdvocateRead)
def read_advocate(advocate_id: int, db: Session = Depends(get_db)):
    return get_advocate(db, advocate_id)

@router.put("/{advocate_id}", response_model=AdvocateRead)
def update_existing_advocate(advocate_id: int, advocate: AdvocateCreate, db: Session = Depends(get_db)):
    return update_advocate(db, advocate_id, advocate)

@router.delete("/{advocate_id}", response_model=AdvocateRead)
def delete_existing_advocate(advocate_id: int, db: Session = Depends(get_db)):
    return delete_advocate(db, advocate_id) 