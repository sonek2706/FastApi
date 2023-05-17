# from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
# from sqlalchemy.orm import relationship

# from .database import Base

from sqlalchemy import MetaData, inspect, create_engine, ForeignKey, Column, Table, String
from sqlalchemy.orm import registry, mapped_column, Mapped, sessionmaker

metadata = MetaData()
mapper_registry = registry(metadata=metadata)

Product_Customer_association = Table(
    "Order",
    metadata,
    Column("product_id", ForeignKey("Product.id"), primary_key=True),
    Column("customer_id", ForeignKey("Customer.id"), primary_key=True),
    Column("quantity", String(50)),
)

@mapper_registry.mapped_as_dataclass
class Product:
    __tablename__ = "Product"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column("product_name")
    price: Mapped[float]
    description:Mapped[str]

@mapper_registry.mapped_as_dataclass
class Customer:
    __tablename__ = "Customer"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    email: Mapped[str]

# print(list(inspect(Product).columns))
# print(list(inspect(Product_Customer_association).columns))
# print(list(inspect(Customer).columns))

# DB_URL = "sqlite:///./data.db"

# engine = create_engine(DB_URL, connect_args={"check_same_thread": False})
# connection = engine.connect()

# metadata.create_all(bind=engine)

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)