import pymupdf as pdf
from app.services.chunker import chunk_text
from app.services.embeddings import embed_text
from app.services.storage import save_documents
from app.database import get_db
import os
from sqlalchemy.orm import Session



def ingest_pdf(file_path:str,db:Session):
    #vars
    file_name = os.path.basename(file_path)
    doc = pdf.open(file_path)
    text = ""
    
    #fetching text from pdf
    for page in doc:
        text += page.get_text()
        
    if not text.strip():
        raise ValueError("No text found in pdf")
        
    chunks = chunk_text(text)#chunking 

    embedding = embed_text(chunks)#getting vectors

    
    save_document = save_documents(file_name,text,chunks,embedding,db)#saving all in db
    

    return save_document
        



    
    
    