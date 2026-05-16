from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from app.services.retrieval import retrieve_chunks
from app.services.llm_ans import generate_ans
from app.schemas.query_schema import QueryRequest
from app.core.database import get_db
from app.models.service import User
from app.security.dependency import get_current_user
from app.models.service import Document

router = APIRouter(prefix="/rag")

@router.post("/query")
def query(req:QueryRequest,db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    document = db.query(Document).filter(Document.id==req.id,Document.user_id==current_user.id).first()
    if not document:
        raise HTTPException(status_code=403,detail="Document not found")

    retrieve_context = retrieve_chunks(req.document_id,req.question,db)

    if not retrieve_context:
        raise HTTPException(status_code=404,detail="No information found in the document")
    
    result = generate_ans(req.question,retrieve_context)
    return result