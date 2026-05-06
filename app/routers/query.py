from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.services.retrieval import retrieve_chunks
from app.schemas import QueryRequest
from app.database import get_db

router = APIRouter(prefix="/rag")

@router.post("/query")
def query(req:QueryRequest,db:Session=Depends(get_db)):
    retrieve = retrieve_chunks(req.document_id,req.question,db)
    return retrieve