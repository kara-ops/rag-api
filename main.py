from app.routers.documents import  router as upload_route
from fastapi import FastAPI

app = FastAPI()

app.include_router(upload_route)