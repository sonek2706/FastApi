from datetime import datetime

from sqlalchemy import MetaData, Table, Column, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, registry

metadata = MetaData()
mapper_registry = registry(metadata=metadata)


@mapper_registry.mapped_as_dataclass
class User:
    __tablename__ = "User"

    username: Mapped[str]
    email: Mapped[str]
    registration_timestamp: Mapped[datetime]
    id: Mapped[int | None] = mapped_column(
        default_factory=lambda: None, primary_key=True, autoincrement=True
    )


Product_Customer_association = Table(
    "Order",
    metadata,
    Column("product_id", ForeignKey("Product.id"), primary_key=True),
    Column("user_id", ForeignKey("User.id"), primary_key=True),
    Column("quantity", String(50)),
)

@mapper_registry.mapped_as_dataclass
class Product:
    __tablename__ = "Product"

    name: Mapped[str] = mapped_column("product_name")
    price: Mapped[float]
    description: Mapped[str]
    id: Mapped[int | None] = mapped_column(
        default_factory=lambda: None, primary_key=True, autoincrement=True
    )
