from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

# from . import crud, models, schemas
from models import models
from models.database import SessionLocal, engine

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal() 
    try:
        yield db
    finally:
        db.close()


# @app.post("/users/", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = crud.get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.create_user(db=db, user=user)


# @app.get("/users/", response_model=list[schemas.User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = crud.get_users(db, skip=skip, limit=limit)
#     return users


# @app.get("/users/{user_id}", response_model=schemas.User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = crud.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user


# @app.post("/users/{user_id}/items/", response_model=schemas.Item)
# def create_item_for_user(
#     user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
# ):
#     return crud.create_user_item(db=db, item=item, user_id=user_id)


# @app.get("/items/", response_model=list[schemas.Item])
# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     items = crud.get_items(db, skip=skip, limit=limit)
#     return items


#=================================================  

# from utils import operations

# # print(operations.add(2,3))
# # print(operations.subtract(5, 2))
# # print(operations.multiply(4, 6))
# # print(operations.divide(10, 5))

# from fastapi import FastAPI
# from typing import Optional

# app = FastAPI()

# # Path parameters
# @app.get("/add/{x}/{y}")
# def add(x : float, y : float) -> float:
#     return x+y

# # Query parameters
# @app.get("/increment/{x}")
# def add(x : int, y : int, z : str | None = None) -> int:
#     return x+y

    
# @app.get("/increment/{x}")
# def add(x : int, y : int, z : Optional[str] = None) -> int:
#     print(z or "Hello")
#     return x+y


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}