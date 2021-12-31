#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from pydantic import BaseModel
from typing import Sequence, Optional


class TypeBase(BaseModel):
    code: str
    description: str
    retired: Optional[bool] = False


class TypeCreate(TypeBase):
    pass


class TypeUpdate(TypeBase):
    id: int


class TypeInDBBase(TypeBase):
    id: int
    create_date: str
    update_date: str

    class Config:
        orm_mode = True


class Type(TypeInDBBase):
    pass


class TypeSearchResults(BaseModel):
    results: Sequence[Type]
