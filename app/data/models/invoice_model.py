#  Copyright (c) Thomas Jacobs. All Rights Reserved.

import datetime as _datetime
from sqlalchemy import Column, Integer, DateTime, ForeignKey, String

from app.data.database_app import Base
from .user_model import UserModel
from .account_model import AccountModel
from .invoice_status_type_model import InvoiceStatusTypeModel


class InvoiceModel(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True)
    invoice_number = Column(Integer, nullable=False)
    invoice_status_type_id = Column(Integer, ForeignKey(InvoiceStatusTypeModel.id))
    account_id = Column(Integer, ForeignKey(AccountModel.id))
    start_date = Column(DateTime)
    end_date = Column(DateTime)

    create_date = Column(DateTime, default=_datetime.datetime.utcnow())
    update_date = Column(DateTime, default=_datetime.datetime.utcnow())
    created_by = Column(Integer, ForeignKey(UserModel.id))
    updated_by = Column(Integer, ForeignKey(UserModel.id))
