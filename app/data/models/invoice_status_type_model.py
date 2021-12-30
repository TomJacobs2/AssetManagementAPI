#  Copyright (c) Thomas Jacobs. All Rights Reserved.

import datetime as _datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean

from app.data.database_app import Base
from .user_model import UserModel


class InvoiceStatusTypeModel(Base):
    __tablename__ = "invoice_status_types"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(16), nullable=False, index=True, unique=True)
    description = Column(String(256), nullable=False)
    retired = Column(Boolean, default=False)

    create_date = Column(DateTime, default=_datetime.datetime.utcnow())
    update_date = Column(DateTime, default=_datetime.datetime.utcnow())
    created_by = Column(Integer, ForeignKey(UserModel.id))
    updated_by = Column(Integer, ForeignKey(UserModel.id))
