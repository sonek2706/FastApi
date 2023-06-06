from datetime import datetime

from sqlalchemy import MetaData
from sqlalchemy.orm import Mapped, mapped_column, registry

metadata = MetaData()
mapper_registry = registry(metadata=metadata)


@mapper_registry.mapped_as_dataclass
class User:
    __tablename__ = "user"

    username: Mapped[str]
    email: Mapped[str]
    registration_timestamp: Mapped[datetime]
    id: Mapped[int | None] = mapped_column(
        default_factory=lambda: None, primary_key=True, autoincrement=True
    )
