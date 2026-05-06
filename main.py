from app.routers.documents import  router as upload_route
from app.routers.query import router as query_route
from fastapi import FastAPI

app = FastAPI()

app.include_router(upload_route)
app.include_router(query_route)