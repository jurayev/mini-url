from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .config import settings
from .endpoints.endpoints import router

app = FastAPI(title=settings.APP_NAME)
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")
app.include_router(router, tags=["shortener"])
