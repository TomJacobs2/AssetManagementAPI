#  Copyright (c) Thomas Jacobs. All Rights Reserved.

import datetime as _datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

from app.data.database_app import Base
from .user_model import UserModel


class AccountModel(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    account_number = Column(String(64), nullable=False)
    account_name = Column(String(256), nullable=False)
    mailing_line_one = Column(String(128), nullable=False)
    mailing_line_two = Column(String(128), nullable=True)
    mailing_city = Column(String(128), nullable=False)
    mailing_postal_code = Column(String(128), nullable=False)
    mailing_state = Column(String(128), nullable=False)
    billing_line_one = Column(String(128), nullable=False)
    billing_line_two = Column(String(128), nullable=True)
    billing_city = Column(String(128), nullable=False)
    billing_postal_code = Column(String(128), nullable=False)
    billing_state = Column(String(128), nullable=False)
    business_phone = Column(String(16), nullable=True)
    business_email = Column(String(256), nullable=True)

    primary_contact_id = Column(Integer, ForeignKey(UserModel.id), nullable=True)
    account_manager_id = Column(Integer, ForeignKey(UserModel.id), nullable=True)

    create_date = Column(DateTime, default=_datetime.datetime.utcnow())
    update_date = Column(DateTime, default=_datetime.datetime.utcnow())
    created_by = Column(Integer, ForeignKey(UserModel.id))
    updated_by = Column(Integer, ForeignKey(UserModel.id))
