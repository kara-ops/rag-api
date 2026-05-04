from app.services.embeddings import embed_text
from app.database import get_db
from sqlalchemy  import text



def retrieve_chunks(doc_id:int,ques:str,db,k:int=5)->list[str]:
    embed_ques = embed_text([ques])[0]

    query = text("SELECT id,content FROM chunks WHERE document_id = :doc_id ORDER BY embedding <=> CAST(:vector AS vector) LIMIT :k")
    res = db.execute(query,{"vector":embed_ques,"k":k,"doc_id":doc_id})
    rows = res.fetchall()
    return [row.content for row in rows]


