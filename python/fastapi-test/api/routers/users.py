from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def status():
    return {"hello": "world"}
