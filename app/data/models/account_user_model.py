#  Copyright (c) Thomas Jacobs. All Rights Reserved.

import datetime as _datetime
from sqlalchemy import Column, Integer, ForeignKey, DateTime

from app.data.database_app import Base
from .account_model import AccountModel
from .user_model import UserModel


class AccountUserModel(Base):
    __tablename__ = "accounts_users"

    id = Column(Integer, primary_key=True, index=True)
    account_id = Column(Integer, ForeignKey(AccountModel.id))
    user_id = Column(Integer, ForeignKey(UserModel.id))
    create_date = Column(DateTime, default=_datetime.datetime.utcnow())
    create_by = Column(Integer, ForeignKey(UserModel.id))
