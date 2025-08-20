from app.models.document import Document
from app.schemas.document import DocumentCreate
from sqlalchemy.orm import Session
from fastapi import HTTPException

def create_document(db: Session, document: DocumentCreate):
    db_document = Document(**document.dict())
    db.add(db_document)
    db.commit()
    db.refresh(db_document)
    return db_document

def get_document(db: Session, document_id: int):
    document = db.query(Document).filter(Document.document_id == document_id).first()
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    return document

def get_documents(db: Session):
    return db.query(Document).all()

def update_document(db: Session, document_id: int, document: DocumentCreate):
    db_document = get_document(db, document_id)
    for key, value in document.dict().items():
        setattr(db_document, key, value)
    db.commit()
    db.refresh(db_document)
    return db_document

def delete_document(db: Session, document_id: int):
    db_document = get_document(db, document_id)
    db.delete(db_document)
    db.commit()
    return db_document 