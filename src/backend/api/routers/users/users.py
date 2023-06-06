from fastapi import Depends
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session

import crud, schemas
from dependencies import get_db

router = APIRouter()


@router.get("/")
def get_users(db: Session = Depends(get_db)) -> list[schemas.User]:
    return crud.get_users(db)


@router.post("/")
def create_user(
    user: schemas.UserCreate, db: Session = Depends(get_db)
) -> schemas.User:
    return crud.create_user(db, user)
