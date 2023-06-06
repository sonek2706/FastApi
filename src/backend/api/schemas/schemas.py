from datetime import datetime

from pydantic import BaseModel

# User
class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    registration_timestamp: datetime

    class Config:
        orm_mode = True


# Product
class ProductBase(BaseModel):
    name: str
    price: float
    description: str


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True
