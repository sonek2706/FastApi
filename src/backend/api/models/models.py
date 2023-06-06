from sqlalchemy import inspect, ForeignKey, Column, Table, String
from sqlalchemy.orm import registry, mapped_column, Mapped, MappedAsDataclass
import pydantic

from api.models.database import Base

Product_Customer_association = Table(
    "Order",
    Base.metadata,
    Column("product_id", ForeignKey("Product.id"), primary_key=True),
    Column("customer_id", ForeignKey("Customer.id"), primary_key=True),
    Column("quantity", String(50)),
)


class Product(
    MappedAsDataclass, Base, dataclass_callable=pydantic.dataclasses.dataclass
):
    __tablename__ = "Product"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column("product_name")
    price: Mapped[float]
    description: Mapped[str]


class Customer(
    MappedAsDataclass, Base, dataclass_callable=pydantic.dataclasses.dataclass
):
    __tablename__ = "Customer"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    email: Mapped[str]

