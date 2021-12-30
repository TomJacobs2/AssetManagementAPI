#  Copyright (c) Thomas Jacobs. All Rights Reserved.

import datetime as _datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean

from app.data.database_app import Base


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(64), nullable=False)
    last_name = Column(String(64), nullable=False)
    email = Column(String(256), nullable=False, index=True)
    cell_phone = Column(Integer)
    external_user = Column(Boolean, default=False)
    login_name = Column(String(256), nullable=False)
    login_password = Column(String(64), nullable=False)
    active = Column(Boolean, default=True)
    locked = Column(Boolean, default=False)
    create_date = Column(DateTime, default=_datetime.datetime.utcnow())
    update_date = Column(DateTime, default=_datetime.datetime.utcnow())
