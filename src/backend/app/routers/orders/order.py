from fastapi import Depends
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session

import crud, schemas, models
from dependencies import get_db

router = APIRouter()


@router.get("/", response_model=list[schemas.Order])
def get_orders(db: Session = Depends(get_db)) -> list[models.Order]:
    return crud.get_orders(db)


@router.post("/", response_model=schemas.Order)
def create_orders(
    order: schemas.OrderCreate, db: Session = Depends(get_db)
) -> models.Order:
    return crud.create_order(db, order)
