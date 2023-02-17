from api.routers.auths import router as auth_router
from api.routers.users import router as user_router
from fastapi import FastAPI

app = FastAPI()

app.include_router(user_router)
app.include_router(auth_router)
