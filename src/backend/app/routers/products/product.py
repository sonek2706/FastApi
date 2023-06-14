from fastapi import Depends
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session

import crud, schemas
from dependencies import get_db

router = APIRouter()


@router.get("/")
def get_products(db: Session = Depends(get_db)) -> list[schemas.Product]:
    return crud.get_products(db)


@router.post("/")
def create_product(
    product: schemas.ProductCreate, db: Session = Depends(get_db)
) -> schemas.Product:
    return crud.create_product(db, product)
