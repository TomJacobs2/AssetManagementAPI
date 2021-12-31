#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from pydantic import BaseModel
from typing import Sequence, Optional


class SystemRolePermissionBase(BaseModel):
    code: str
    description: str
    retired: Optional[bool] = False
    for_external_user: Optional[bool] = False


class SystemRolePermissionCreate(SystemRolePermissionBase):
    pass


class SystemRolePermissionUpdate(SystemRolePermissionBase):
    id: int


class SystemRolePermissionInDBBase(SystemRolePermissionBase):
    id: int
    create_date: str
    update_date: str

    class Config:
        orm_mode = True


class SystemRolePermission(SystemRolePermissionInDBBase):
    pass


class SystemRolePermissionSearchResults(BaseModel):
    results: Sequence[SystemRolePermission]
