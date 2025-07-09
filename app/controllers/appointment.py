from app.models.appointment import Appointment
from app.schemas.appointment import AppointmentCreate
from sqlalchemy.orm import Session
from fastapi import HTTPException

def create_appointment(db: Session, appointment: AppointmentCreate):
    db_appointment = Appointment(**appointment.dict())
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment

def get_appointment(db: Session, appointment_id: int):
    appointment = db.query(Appointment).filter(Appointment.id == appointment_id).first()
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return appointment

def get_appointments(db: Session):
    return db.query(Appointment).all()

def update_appointment(db: Session, appointment_id: int, appointment: AppointmentCreate):
    db_appointment = get_appointment(db, appointment_id)
    for key, value in appointment.dict().items():
        setattr(db_appointment, key, value)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment

def delete_appointment(db: Session, appointment_id: int):
    db_appointment = get_appointment(db, appointment_id)
    db.delete(db_appointment)
    db.commit()
    return db_appointment 