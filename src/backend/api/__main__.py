from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from api.models import crud, models, schemas
from api.models.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal() 
    try:
        yield db
    finally:
        db.close()


@app.get("/products/", response_model=list[schemas.Product])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = crud.get_Products(db, skip=skip, limit=limit)
    return products

@app.get("/customers/", response_model=list[schemas.Customer])
def read_customers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    customers = crud.get_Customers(db, skip=skip, limit=limit)
    return customers
