from datetime import datetime

from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    registration_timestamp: datetime

    class Config:
        orm_mode = True
