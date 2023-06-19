from fastapi import Depends
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session

import crud, schemas, models
from dependencies import get_db

router = APIRouter()


@router.post("/{id}", response_model=list[schemas.OrderProduct])
def get_orders(id: int, db: Session = Depends(get_db)) -> list[models.OrderProduct]:
    return crud.get_products_from_Order(id, db)


@router.post("/", response_model=schemas.OrderProduct)
def create_orders(
    order_product: schemas.OrderProductCreate, db: Session = Depends(get_db)
) -> models.OrderProduct:
    return crud.create_order_product(db, order_product)
