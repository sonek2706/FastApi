from datetime import datetime
from typing import Iterable

from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.sql import Select

import models, schemas

# User
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
def get_products(db: Session) -> list[models.Product]:
    return list(db.scalars(get_products_query()))


def get_products_query() -> Select[Iterable[models.Product]]:
    return select(models.Product)


def create_product(db: Session, product: schemas.ProductCreate) -> models.Product:
    product_model = models.Product(
        name=product.name,
        price=product.price,
        description=product.description
    )

    db.add(product_model)
    db.commit()
    db.refresh(product_model)

    return product_model
