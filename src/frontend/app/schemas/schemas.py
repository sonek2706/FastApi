from datetime import datetime

from pydantic import BaseModel


# User
class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    email: str
    registration_timestamp: datetime

    class Config:
        orm_mode = True

class Credentials(UserBase):
    password: str

#  Product
class ProductBase(BaseModel):
    name: str
    price: float
    description: str | None = None


class ProductCreate(ProductBase):
    category_id: int


class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True


# Order
class OrderBase(BaseModel):
    total: float
    registration_timestamp: datetime


class OrderCreate(OrderBase):
    pass


class Order(OrderBase):
    id: int

    class Config:
        orm_mode = True


# Category
class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True
