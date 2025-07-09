from fastapi import APIRouter, File, UploadFile, HTTPException
from app.core.s3 import upload_file_to_s3

router = APIRouter(prefix="/upload", tags=["upload"])

@router.post("/document")
def upload_document(file: UploadFile = File(...)):
    try:
        url = upload_file_to_s3(file.file, file.filename, folder='documents')
        return {"url": url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/profile-picture")
def upload_profile_picture(file: UploadFile = File(...)):
    try:
        url = upload_file_to_s3(file.file, file.filename, folder='profile-pictures')
        return {"url": url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 