from fastapi import Depends
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session

import crud, schemas, models
from dependencies import get_db

router = APIRouter()


@router.get("/{id}", response_model=schemas.Product)
def get_products(id: int, db: Session = Depends(get_db)) -> models.Product:
    return crud.get_product(db, id)


@router.get("/", response_model=list[schemas.Product])
def get_products(db: Session = Depends(get_db)) -> list[models.Product]:
    return crud.get_products(db)


@router.post("/", response_model=schemas.Product)
def create_product(
    product: schemas.ProductCreate, db: Session = Depends(get_db)
) -> models.Product:
    return crud.create_product(db, product)
