from fastapi import Depends
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session

import crud, schemas, models
from dependencies import get_db

router = APIRouter()


@router.get("/{id}/", response_model=schemas.Category)
def get_category(db: Session = Depends(get_db), id: int = 1) -> models.Category:
    return crud.get_category(db, id)


@router.get("/", response_model=list[schemas.Category])
def get_categories(db: Session = Depends(get_db)) -> list[models.Category]:
    return crud.get_categories(db)


@router.post("/", response_model=schemas.Category)
def create_category(
    category: schemas.CategoryCreate, db: Session = Depends(get_db)
) -> models.Category:
    return crud.create_category(db, category)
