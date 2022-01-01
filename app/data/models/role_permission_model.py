#  Copyright (c) Thomas Jacobs. All Rights Reserved.

import datetime as _datetime
from sqlalchemy import Column, Integer, ForeignKey, DateTime

from app.data.database_app import Base
from .role_model import RoleModel
from .permission_model import PermissionModel
from .user_model import UserModel


class RolePermissionModel(Base):
    __tablename__ = "roles_permissions"

    id = Column(Integer, primary_key=True, index=True)
    role_id = Column(Integer, ForeignKey(RoleModel.id))
    permission_id = Column(Integer, ForeignKey(PermissionModel.id))
    create_date = Column(DateTime, default=_datetime.datetime.utcnow())
    create_by = Column(Integer, ForeignKey(UserModel.id))
