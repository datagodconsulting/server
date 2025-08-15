from app.models.client import Client
from app.schemas.client import ClientCreate
from sqlalchemy.orm import Session
from fastapi import HTTPException

def create_client(db: Session, client: ClientCreate):
    db_client = Client(**client.dict())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

def get_client(db: Session, client_id: int):
    client = db.query(Client).filter(Client.client_id == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

def get_clients(db: Session):
    return db.query(Client).all()

def update_client(db: Session, client_id: int, client: ClientCreate):
    db_client = get_client(db, client_id)
    for key, value in client.dict().items():
        setattr(db_client, key, value)
    db.commit()
    db.refresh(db_client)
    return db_client

def delete_client(db: Session, client_id: int):
    db_client = get_client(db, client_id)
    db.delete(db_client)
    db.commit()
    return db_client 