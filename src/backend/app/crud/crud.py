from datetime import datetime
from typing import Iterable

from fastapi import Response
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.sql import Select

import models, schemas


# User
# def authorize(cred: schemas.Credentials, db: Session) -> Response:
#     # user = crud.get_student(user.number, db)

#     # if user is None:
#     #     return Response(status_code=404)

#     # if user.password != user.password:
#     #     return Response(status_code=401)

#     return Response(status_code=200)

def get_user(id: int, db: Session) -> models.User:
    return db.get(models.User, id)


def get_users(db: Session) -> list[models.User]:
    return list(db.scalars(get_users_query()))


def get_users_query() -> Select[Iterable[models.User]]:
    return select(models.User)


def login(credentials: schemas.UserCredentials, db: Session) -> Response:
    user = db.query(models.User).filter(models.User.username == credentials.username).first()
    
    if user is None:
        return Response(status_code=404)    
    
    if user.password != credentials.password:
        return Response(status_code=401)
    
    return Response(status_code=200)


def create_user(db: Session, user: schemas.UserCreate) -> Response:
    tmp = db.query(models.User).filter(models.User.username == user.username or models.User.email == user.email ).first()

    if tmp is None:
        user_model = models.User(
            username=user.username,
            email=user.email,
            password=user.password,
            registration_timestamp=datetime.now(),
        )

        db.add(user_model)
        db.commit()
        db.refresh(user_model)
        return Response(status_code=200)
    else:
        return Response(status_code=409)
    


# Category
def get_category(db: Session, id: int) -> models.Category:
    return db.get(models.Category, id)


def get_categories(db: Session) -> list[models.Category]:
    return list(db.scalars(get_categories_query()))


def get_categories_query() -> Select[Iterable[models.Category]]:
    return select(models.Category)


def create_category(db: Session, category: schemas.CategoryCreate) -> models.Category:
    category_model = models.Category(
        name=category.name,
    )

    db.add(category_model)
    db.commit()
    db.refresh(category_model)

    return category_model


# Product
def get_product(db: Session, id: int) -> list[models.Product]:
    return db.get(models.Product, id)


def get_products(db: Session) -> list[models.Product]:
    return list(db.scalars(get_products_query()))


def get_products_for_category(category_id: int, db: Session) -> list[models.Product]:
    return db.query(models.Product).filter(models.Product.category_id == category_id).all()

def get_cart(order_id: int, db: Session):
    order_product = db.query(models.OrderProduct).filter(models.OrderProduct.order_id == order_id).all()

    products = []
    for op in order_product:
        tmp = db.query(models.Product).filter(models.Product.id == op.product_id).first()
        products.append(tmp)
    
    return products

def get_products_query() -> Select[Iterable[models.Product]]:
    return select(models.Product)


def create_product(data: schemas.ProductCreate, db: Session) -> models.Product:
    product_model = models.Product(
        name=data.name,
        price=data.price,
        description=data.description,
        category_id=data.category_id,
    )

    db.add(product_model)
    db.commit()
    db.refresh(product_model)

    return product_model


# Order
def get_order(id: int, db: Session) -> models.Order:
    return db.query(models.Order).filter(models.Order.id == id).first()

def update_order(orderUpdate: schemas.OrderUpdate, db: Session) -> Response:
    order = db.get(models.Order, orderUpdate.id)

    # We should create an order
    if order is None:
        orderCreate = schemas.OrderCreate(
            total=0,
            registration_timestamp=datetime.now(),
            user_id=1
        )
        order = create_order(orderCreate, db)
    else:
        order.total += orderUpdate.total

    db.commit()

    return Response(status_code=200)


def get_orders(db: Session) -> list[models.Order]:
    return list(db.scalars(get_orders_query()))


def get_orders_query() -> Select[Iterable[models.Order]]:
    return select(models.Order)


def create_order(order: schemas.OrderCreate, db: Session) -> models.Order:
    
    order_model = models.Order(
        user_id=order.user_id,
        total=order.total,
        registration_timestamp=order.registration_timestamp,
    )

    db.add(order_model)
    db.commit()
    db.refresh(order_model)

    return order_model


# Order Product
def get_products_from_Order(order_id: int, db: Session):
    return db.query(models.OrderProduct).filter(models.OrderProduct.order_id == order_id).all()

def remove_product(product_id: int, order_id: int, db: Session):


    order = db.query(models.Order).filter(models.Order.id == order_id).first()
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    order_product = db.query(models.OrderProduct).filter(models.OrderProduct.product_id == product_id and models.OrderProduct.order_id == order_id).first()
    
    order.total -= product.price * order_product.quantity

    db.query(models.OrderProduct).filter(models.OrderProduct.product_id == product_id and models.OrderProduct.order_id == order_id).delete()

    db.commit()
    db.refresh(order)
    db.refresh(product)
    db.refresh(order_product)

    return

def create_order_product(db: Session, data: schemas.OrderProductCreate) -> Response:

    order_product = models.OrderProduct(
        order_id=data.order_id,
        product_id=data.product_id,
        quantity=data.quantity
    )

    db.add(order_product)
    db.commit()
    db.refresh(order_product)

    product = db.get(models.Product, data.product_id)

    orderUpdate = schemas.OrderUpdate(
        id=data.order_id,
        total=data.quantity*product.price
    )
    update_order(orderUpdate ,db)


    return Response(status_code=200)
