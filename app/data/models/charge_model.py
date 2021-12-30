#  Copyright (c) Thomas Jacobs. All Rights Reserved.

import datetime as _datetime
from sqlalchemy import Column, Integer, DateTime, ForeignKey, Float

from app.data.database_app import Base
from .user_model import UserModel
from .rental_model import RentalModel
from .cost_model import CostModel


class ChargeModel(Base):
    __tablename__ = "charges"

    id = Column(Integer, primary_key=True, index=True)
    rental_id = Column(Integer, ForeignKey(RentalModel.id))
    cost_id = Column(Integer, ForeignKey(CostModel.id))
    amount = Column(Float, default=0.00)

    create_date = Column(DateTime, default=_datetime.datetime.utcnow())
    update_date = Column(DateTime, default=_datetime.datetime.utcnow())
    created_by = Column(Integer, ForeignKey(UserModel.id))
    updated_by = Column(Integer, ForeignKey(UserModel.id))
