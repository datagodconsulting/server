from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.client import ClientCreate, ClientRead
from app.controllers.client import create_client, get_client, get_clients, update_client, delete_client
from app.database import SessionLocal
from typing import List

router = APIRouter(prefix="/clients", tags=["clients"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[ClientRead])
def list_clients(db: Session = Depends(get_db)):
    return get_clients(db)

@router.post("/", response_model=ClientRead)
def create_new_client(client: ClientCreate, db: Session = Depends(get_db)):
    return create_client(db, client)

@router.get("/{client_id}", response_model=ClientRead)
def read_client(client_id: int, db: Session = Depends(get_db)):
    return get_client(db, client_id)

@router.put("/{client_id}", response_model=ClientRead)
def update_existing_client(client_id: int, client: ClientCreate, db: Session = Depends(get_db)):
    return update_client(db, client_id, client)

@router.delete("/{client_id}", response_model=ClientRead)
def delete_existing_client(client_id: int, db: Session = Depends(get_db)):
    return delete_client(db, client_id) 