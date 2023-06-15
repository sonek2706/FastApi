from datetime import datetime

from pydantic import BaseModel

from models import Order


# User
class UserBase(BaseModel):
    username: str
    email: str
    orders: list[Order]


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


# Order
class OrderBase(BaseModel):
    total: float


class OrderCreate(OrderBase):
    registration_timestamp: datetime


class Order(OrderBase):
    user_id: int

    class Config:
        orm_mode = True


# Category
class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    pass


class Category(BaseModel):
    category_idw: int

    class Config:
        orm_mode = True
