from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.appointment import AppointmentCreate, AppointmentRead
from app.controllers.appointment import create_appointment, get_appointment, get_appointments, update_appointment, delete_appointment
from app.database import SessionLocal
from typing import List

router = APIRouter(prefix="/appointments", tags=["appointments"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[AppointmentRead])
def list_appointments(db: Session = Depends(get_db)):
    return get_appointments(db)

@router.post("/", response_model=AppointmentRead)
def create_new_appointment(appointment: AppointmentCreate, db: Session = Depends(get_db)):
    return create_appointment(db, appointment)

@router.get("/{appointment_id}", response_model=AppointmentRead)
def read_appointment(appointment_id: int, db: Session = Depends(get_db)):
    return get_appointment(db, appointment_id)

@router.put("/{appointment_id}", response_model=AppointmentRead)
def update_existing_appointment(appointment_id: int, appointment: AppointmentCreate, db: Session = Depends(get_db)):
    return update_appointment(db, appointment_id, appointment)

@router.delete("/{appointment_id}", response_model=AppointmentRead)
def delete_existing_appointment(appointment_id: int, db: Session = Depends(get_db)):
    return delete_appointment(db, appointment_id) 