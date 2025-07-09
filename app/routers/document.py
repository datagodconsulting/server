from fastapi import APIRouter, Depends, HTTPException, File, UploadFile
from sqlalchemy.orm import Session
from app.schemas.document import DocumentCreate, DocumentRead
from app.controllers.document import create_document, get_document, get_documents, update_document, delete_document
from app.core.s3 import upload_file_to_s3
from app.database import SessionLocal
from typing import List

router = APIRouter(prefix="/documents", tags=["documents"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[DocumentRead])
def list_documents(db: Session = Depends(get_db)):
    return get_documents(db)

@router.post("/", response_model=DocumentRead)
def create_new_document(document: DocumentCreate, db: Session = Depends(get_db)):
    return create_document(db, document)

@router.get("/{document_id}", response_model=DocumentRead)
def read_document(document_id: int, db: Session = Depends(get_db)):
    return get_document(db, document_id)

@router.put("/{document_id}", response_model=DocumentRead)
def update_existing_document(document_id: int, document: DocumentCreate, db: Session = Depends(get_db)):
    return update_document(db, document_id, document)

@router.delete("/{document_id}", response_model=DocumentRead)
def delete_existing_document(document_id: int, db: Session = Depends(get_db)):
    return delete_document(db, document_id) 