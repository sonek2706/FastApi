from datetime import datetime

from pydantic import BaseModel


# User
class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    email: str
    password: str

class UserCredentials(UserBase):
    password: str

class User(UserBase):
    email: str
    registration_timestamp: datetime
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


class OrderCreate(OrderBase):
    registration_timestamp: datetime
    user_id: int

class OrderUpdate(OrderBase):
    id: int


class Order(OrderBase):
    user_id: int
    registration_timestamp: datetime
    id: int

    class Config:
        orm_mode = True

# Order Product
class OrderProductBase(BaseModel):
    order_id: int
    product_id: int


class OrderProductCreate(OrderProductBase):
    quantity: int

class OrderProductRemove(OrderProductBase):
    pass

class OrderProduct(OrderProductBase):
    id: int
    quantity: int

    class Config:
        orm_mode = True
