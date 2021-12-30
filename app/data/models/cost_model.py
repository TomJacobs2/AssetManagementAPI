#  Copyright (c) Thomas Jacobs. All Rights Reserved.

import datetime as _datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Float

from app.data.database_app import Base
from .user_model import UserModel
from .asset_model import AssetModel
from .cost_type_model import CostTypeModel
from .frequency_type_model import FrequencyTypeModel


class CostModel(Base):
    __tablename__ = "costs"

    id = Column(Integer, primary_key=True, index=True)
    asset_id = Column(Integer, ForeignKey(AssetModel.id))
    cost_type_id = Column(Integer, ForeignKey(CostTypeModel.id))
    retired = Column(Boolean, default=False)
    description = Column(String(256), nullable=False)
    amount = Column(Float, default=0.0)
    frequency_rate = Column(Integer, ForeignKey(FrequencyTypeModel.id))

    create_date = Column(DateTime, default=_datetime.datetime.utcnow())
    update_date = Column(DateTime, default=_datetime.datetime.utcnow())
    created_by = Column(Integer, ForeignKey(UserModel.id))
    updated_by = Column(Integer, ForeignKey(UserModel.id))
