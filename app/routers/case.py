from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.schemas.case import CaseCreate, CaseRead
from app.controllers.case import create_case, get_case, get_cases, update_case, delete_case
from app.models.case import Case
from app.models.client import Client
from app.database import SessionLocal
from typing import List, Optional
from app.constants.case_types import TypeList

router = APIRouter(prefix="/cases", tags=["cases"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[CaseRead])
def list_cases(
    advocate_id: Optional[int] = Query(None),
    user_id: Optional[int] = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(Case)
    if advocate_id:
        query = query.filter(Case.advocate_id == advocate_id)
    if user_id:
        client = db.query(Client).filter(Client.user_id == user_id).first()
        if client:
            query = query.filter(Case.client_id == client.client_id)
        else:
            return []
    return query.all()

@router.get("/client/{client_id}", response_model=List[CaseRead])
def get_cases_for_client(client_id: int, db: Session = Depends(get_db)):
    return db.query(Case).filter(Case.client_id == client_id).all()

@router.get("/types")
def get_case_types():
    return TypeList

@router.post("/", response_model=CaseRead)
def create_new_case(case: CaseCreate, db: Session = Depends(get_db)):
    return create_case(db, case)

@router.get("/{case_id}", response_model=CaseRead)
def read_case(case_id: int, db: Session = Depends(get_db)):
    return get_case(db, case_id)

@router.put("/{case_id}", response_model=CaseRead)
def update_existing_case(case_id: int, case: CaseCreate, db: Session = Depends(get_db)):
    return update_case(db, case_id, case)

@router.delete("/{case_id}", response_model=CaseRead)
def delete_existing_case(case_id: int, db: Session = Depends(get_db)):
    return delete_case(db, case_id) 