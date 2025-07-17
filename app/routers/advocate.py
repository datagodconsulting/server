from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.advocate import AdvocateCreate, AdvocateRead
from app.controllers.advocate import create_advocate, get_advocate, get_advocates, update_advocate, delete_advocate
from app.database import SessionLocal
from typing import List
from fastapi.security import OAuth2PasswordRequestForm
from app.controllers.user import authenticate_user, create_access_token
from app.schemas.user import UserRead

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

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    access_token = create_access_token(data={"sub": user.email})
    user_data = UserRead.from_orm(user).dict()
    return {"access_token": access_token, "token_type": "bearer", "user": user_data} 