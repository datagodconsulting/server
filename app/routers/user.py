from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserRead, UserLogin
from app.controllers.user import create_user, authenticate_user, get_user_by_id, create_access_token
from app.models.user import User
from app.database import SessionLocal
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from app.core.config import SECRET_KEY
from typing import List, Optional

router = APIRouter(prefix="/users", tags=["users"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

# @router.get("/", response_model=List[UserRead])
# def list_users(
#     role: Optional[str] = Query(None),
#     is_active: Optional[bool] = Query(None),
#     db: Session = Depends(get_db)
# ):
#     query = db.query(User)
#     if role:
#         query = query.filter(User.role == role)
#     if is_active is not None:
#         query = query.filter(User.is_active == is_active)
#     return query.all()
@router.get("/")
def list_users(
    role: Optional[str] = Query(None),
    is_active: Optional[bool] = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(User)
    if role:
        query = query.filter(User.role == role)
    if is_active is not None:
        query = query.filter(User.is_active == is_active)
    users = query.all()
    result = []
    from app.models.advocate import Advocate
    from app.models.client import Client
    for user in users:
        user_data = UserRead.from_orm(user).dict()
        if user.role == "advocate":
            advocate = db.query(Advocate).filter(Advocate.user_id == user.user_id).first()
            if advocate:
                user_data["advocate"] = {
                    "advocate_id": advocate.advocate_id,
                    "bar_council_id": advocate.bar_council_id,
                    "specialization": advocate.specialization,
                    "years_of_experience": advocate.years_of_experience,
                    "location": advocate.location
                }
        elif user.role == "client":
            client = db.query(Client).filter(Client.user_id == user.user_id).first()
            if client:
                user_data["client"] = {
                    "client_id": client.client_id,
                    "address": client.address
                }
        result.append(user_data)
    return result

@router.put("/{user_id}/approve", response_model=UserRead)
def approve_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.is_active = True
    db.commit()
    db.refresh(user)
    return user

@router.post("/register", response_model=UserRead)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = create_user(db, user)
    return db_user

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    access_token = create_access_token(data={"sub": user.email})
    user_data = UserRead.from_orm(user)
    return {"access_token": access_token, "token_type": "bearer", "user": user_data}

@router.get("/me", response_model=UserRead)
def read_users_me(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = db.query(get_user_by_id(db, user_id=None)).filter_by(email=email).first()
    if user is None:
        raise credentials_exception
    return user
