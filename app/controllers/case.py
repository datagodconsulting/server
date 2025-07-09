from app.models.case import Case
from app.schemas.case import CaseCreate
from sqlalchemy.orm import Session
from fastapi import HTTPException

def create_case(db: Session, case: CaseCreate):
    db_case = Case(**case.dict())
    db.add(db_case)
    db.commit()
    db.refresh(db_case)
    return db_case

def get_case(db: Session, case_id: int):
    case = db.query(Case).filter(Case.id == case_id).first()
    if not case:
        raise HTTPException(status_code=404, detail="Case not found")
    return case

def get_cases(db: Session):
    return db.query(Case).all()

def update_case(db: Session, case_id: int, case: CaseCreate):
    db_case = get_case(db, case_id)
    for key, value in case.dict().items():
        setattr(db_case, key, value)
    db.commit()
    db.refresh(db_case)
    return db_case

def delete_case(db: Session, case_id: int):
    db_case = get_case(db, case_id)
    db.delete(db_case)
    db.commit()
    return db_case 