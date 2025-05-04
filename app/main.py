from fastapi import FastAPI
from app.routers.user_router import router as user_router
from app.routers.owner_router import router as owner_router

app = FastAPI(title="FastAPI MongoDB CRUD")

app.include_router(user_router)
app.include_router(owner_router)
