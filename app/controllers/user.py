from app.models.user import User
from sqlalchemy.exc import IntegrityError
from app.schemas.user import UserCreate, UserRead, UserLogin
from app.database import SessionLocal
from sqlalchemy.orm import Session
from fastapi import HTTPException
from passlib.context import CryptContext
import jwt
from datetime import datetime, timedelta
from app.core.config import SECRET_KEY

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def create_user(db: Session, user: UserCreate):
    db_user = User(
        aadhar_id=user.aadhar_id,
        full_name=user.full_name,
        email=user.email,
        phone=user.phone,
        password_hash=get_password_hash(user.password),
        role=user.role,
        is_active=True
    )
    db.add(db_user)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Aadhar ID or Email already exists.")
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.password_hash):
        return None
    return user

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.user_id == user_id).first() 