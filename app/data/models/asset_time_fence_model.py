#  Copyright (c) Thomas Jacobs. All Rights Reserved.

import datetime as _datetime
from sqlalchemy import Column, Integer, DateTime, ForeignKey, Boolean

from app.data.database_app import Base
from .user_model import UserModel
from .asset_model import AssetModel


class AssetTimeFenceModel(Base):
    __tablename__ = "asset_time_fences"

    id = Column(Integer, primary_key=True, index=True)
    asset_id = Column(Integer, ForeignKey(AssetModel.id))
    mon_allowed_start_time = Column(Integer, default=600)
    mon_allowed_end_time = Column(Integer, default=1800)
    tue_allowed_start_time = Column(Integer, default=600)
    tue_allowed_end_time = Column(Integer, default=1800)
    wed_allowed_start_time = Column(Integer, default=600)
    wed_allowed_end_time = Column(Integer, default=1800)
    thu_allowed_start_time = Column(Integer, default=600)
    thu_allowed_end_time = Column(Integer, default=1800)
    fri_allowed_start_time = Column(Integer, default=600)
    fri_allowed_end_time = Column(Integer, default=1800)
    sat_allowed_start_time = Column(Integer, default=600)
    sat_allowed_end_time = Column(Integer, default=1800)
    sun_allowed_start_time = Column(Integer, default=600)
    sun_allowed_end_time = Column(Integer, default=1800)
    active = Column(Boolean, default=False)

    create_date = Column(DateTime, default=_datetime.datetime.utcnow())
    update_date = Column(DateTime, default=_datetime.datetime.utcnow())
    created_by = Column(Integer, ForeignKey(UserModel.id))
    updated_by = Column(Integer, ForeignKey(UserModel.id))
