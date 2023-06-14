from datetime import datetime

from sqlalchemy import MetaData, Table, Column, ForeignKey, String, Integer
from sqlalchemy.orm import Mapped, mapped_column, registry, relationship

metadata = MetaData()
mapper_registry = registry(metadata=metadata)


@mapper_registry.mapped_as_dataclass
class User:
    __tablename__ = "User"

    username: Mapped[str]
    email: Mapped[str]
    registration_timestamp: Mapped[datetime]

    orders: Mapped[list["Order"]] = relationship(back_populates="user")
    id: Mapped[int | None] = mapped_column(
        default_factory=lambda: None, primary_key=True, autoincrement=True
    )


@mapper_registry.mapped_as_dataclass
class Category:
    __tablename__ = "Category"

    name: Mapped[str] = mapped_column("category_name")
    products: Mapped[list["Product"]] = relationship(back_populates="category")

    id: Mapped[int | None] = mapped_column(
        default_factory=lambda: None, primary_key=True, autoincrement=True
    )


@mapper_registry.mapped_as_dataclass
class Product:
    __tablename__ = "Product"

    name: Mapped[str] = mapped_column("product_name")
    price: Mapped[float]
    description: Mapped[str]
    cateogory_id: Mapped[int] = mapped_column(ForeignKey("Category.id"))
    category: Mapped[Category] = relationship(back_populates="products")

    id: Mapped[int | None] = mapped_column(
        default_factory=lambda: None, primary_key=True, autoincrement=True
    )


@mapper_registry.mapped_as_dataclass
class Order:
    __tablename__ = "Order"

    total: Mapped[float]
    registration_timestamp: Mapped[datetime]

    user_id: Mapped[int] = mapped_column(ForeignKey("User.id"))
    user: Mapped[User] = relationship(back_populates="orders")
    id: Mapped[int | None] = mapped_column(
        default_factory=lambda: None, primary_key=True, autoincrement=True
    )


Product_Customer_association = Table(
    "Order_Item",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("order_id", ForeignKey("Order.id")),
    Column("product_id", ForeignKey("Product.id")),
    Column("quantity", String(50)),
)
