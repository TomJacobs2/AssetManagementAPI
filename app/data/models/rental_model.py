#  Copyright (c) Thomas Jacobs. All Rights Reserved.

import datetime as _datetime
from sqlalchemy import Column, Integer, DateTime, ForeignKey, String

from app.data.database_app import Base
from .user_model import UserModel
from .asset_model import AssetModel
from .rental_status_type_model import RentalStatusTypeModel


class RentalModel(Base):
    __tablename__ = "rentals"

    id = Column(Integer, primary_key=True, index=True)
    contract_number = Column(String(64), nullable=False)
    asset_id = Column(Integer, ForeignKey(AssetModel.id))
    rental_status_type_id = Column(Integer, ForeignKey(RentalStatusTypeModel.id))
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    rental_user_id = Column(Integer, ForeignKey(UserModel.id))

    create_date = Column(DateTime, default=_datetime.datetime.utcnow())
    update_date = Column(DateTime, default=_datetime.datetime.utcnow())
    created_by = Column(Integer, ForeignKey(UserModel.id))
    updated_by = Column(Integer, ForeignKey(UserModel.id))
