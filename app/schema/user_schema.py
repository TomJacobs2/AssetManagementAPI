#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from pydantic import BaseModel
from typing import Sequence, Optional


class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    cell_phone: int
    external_user: Optional[bool] = False
    login_name: str
    active: Optional[bool] = True
    locked: Optional[bool] = False
    role_id: int


class UserCreate(UserBase):
    login_password: str


class UserUpdate(UserBase):
    id: int


class UserInDBBase(UserBase):
    id: int
    create_date: str
    update_date: str

    class Config:
        orm_mode = True


class User(UserInDBBase):
    pass


class UserSearchResults(BaseModel):
    results: Sequence[User]
