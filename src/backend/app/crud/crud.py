from datetime import datetime
from typing import Iterable

from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.sql import Select

import models, schemas


# User
def get_user(id: int, db: Session) -> models.User:
    return db.get(models.User, id)


def get_users(db: Session) -> list[models.User]:
    return list(db.scalars(get_users_query()))


def get_users_query() -> Select[Iterable[models.User]]:
    return select(models.User)


def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    user_model = models.User(
        username=user.username,
        email=user.email,
        registration_timestamp=datetime.now(),
    )

    db.add(user_model)
    db.commit()
    db.refresh(user_model)

    return user_model


# Product
def get_product(db: Session, id: int) -> list[models.Product]:
    return db.get(models.Product, id)


def get_products(db: Session) -> list[models.Product]:
    return list(db.scalars(get_products_query()))


def get_products_query() -> Select[Iterable[models.Product]]:
    return select(models.Product)


def create_product(db: Session, data: schemas.ProductCreate) -> models.Product:
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
def get_orders(db: Session) -> list[models.Order]:
    return list(db.scalars(get_orders_query()))


def get_orders_query() -> Select[Iterable[models.Order]]:
    return select(models.Order)


def create_order(db: Session, order: schemas.OrderCreate) -> models.Order:
    order_model = models.Order(
        total=order.total,
        registration_timestamp=order.registration_timestamp,
    )

    db.add(order_model)
    db.commit()
    db.refresh(order_model)

    return order_model


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
