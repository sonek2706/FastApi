from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import registry, sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///data.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
connection = engine.connect()

metadata = MetaData()
mapper_registry = registry(metadata=metadata)

SessionLocal = sessionmaker(autocomit=False, autoflush=False, bind=engine)
