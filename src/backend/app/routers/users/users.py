from fastapi import Depends
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session


import crud, schemas, models
from dependencies import get_db

router = APIRouter()

@router.post("/{id}/")
def get_user(id: int, db: Session = Depends(get_db)) -> models.User:
    user = crud.get_user(id, db)
    return user


@router.get("/", response_model=list[schemas.User])
def get_users(db: Session = Depends(get_db)) -> list[models.User]:
    return crud.get_users(db)


@router.post("/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)) -> models.User:
    return crud.create_user(db, user)
