from typing import List

from db import get_session
from fastapi import APIRouter, Depends, status
from models import Hero, HeroCreate, HeroRead
from sqlmodel import Session, select

router = APIRouter()


@router.post("/heroes/", response_model=HeroRead, status_code=status.HTTP_200_OK)
def create_hero(*, db: Session = Depends(get_session), hero: HeroCreate):
    """
    Then we create a new Hero (this is the actual table model
    that saves things to the database) using Hero.from_orm().

    The method .from_orm() reads data from another object with attributes
    and creates a new instance of this class, in this case Hero.
    """
    db_hero = Hero.from_orm(hero)
    db.add(db_hero)
    db.commit()
    db.refresh(db_hero)
    return db_hero


@router.get("/heroes/", response_model=List[HeroRead], status_code=status.HTTP_200_OK)
def read_heroes(*, db: Session = Depends(get_session)):
    heroes = db.exec(select(Hero)).all()
    return heroes
