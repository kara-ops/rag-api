from app.routers.documents import  router as upload_route
from app.routers.query import router as query_route
from app.routers.auth_router import router as user_router
from fastapi import FastAPI

app = FastAPI()

app.include_router(upload_route)
app.include_router(query_route)
app.include_router(user_router)