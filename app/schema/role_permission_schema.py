#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from pydantic import BaseModel
from typing import Sequence, Optional


class RolePermissionBase(BaseModel):
    code: str
    description: str
    retired: Optional[bool] = False
    for_external_user: Optional[bool] = False


class RolePermissionCreate(RolePermissionBase):
    pass


class RolePermissionUpdate(RolePermissionBase):
    id: int


class RolePermissionInDBBase(RolePermissionBase):
    id: int
    create_date: str
    update_date: str

    class Config:
        orm_mode = True


class RolePermission(RolePermissionInDBBase):
    pass


class RolePermissionSearchResults(BaseModel):
    results: Sequence[RolePermission]
