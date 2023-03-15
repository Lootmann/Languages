from fastapi import FastAPI
from routers import router as hero_router

app = FastAPI()

app.include_router(hero_router)
