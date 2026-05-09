from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from app.services.retrieval import retrieve_chunks
from app.services.llm_ans import generate_ans
from app.schemas.schemas import QueryRequest
from app.core.database import get_db

router = APIRouter(prefix="/rag")

@router.post("/query")
def query(req:QueryRequest,db:Session=Depends(get_db)):
    retrieve_context = retrieve_chunks(req.document_id,req.question,db)

    if not retrieve_context:
        raise HTTPException(status_code=404,detail="No information found in the document")
    
    result = generate_ans(req.question,retrieve_context)
    return result