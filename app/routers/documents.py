from fastapi import APIRouter,Depends,UploadFile
from sqlalchemy.orm import Session
from app.core.database import get_db
import os
import shutil
from app.services.ingestion import ingest_pdf


router = APIRouter(prefix="/rag")

@router.post("/upload")
async def upload_docs(file: UploadFile, db:Session=Depends(get_db)):
    upload_dir = r"C:\Users\ankus\Documents\rag-api\temp"
    file_path = os.path.join(upload_dir,file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file,buffer)
    

    ingest_file = ingest_pdf(file_path,db)
    os.remove(file_path)
    return ingest_file
