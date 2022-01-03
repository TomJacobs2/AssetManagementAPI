#  Copyright (c) Thomas Jacobs. All Rights Reserved.

import datetime as _datetime
from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey, Boolean

from app.data.database_app import Base
from .user_model import UserModel
from .asset_model import AssetModel


class AssetGeoFencingModel(Base):
    __tablename__ = "asset_geo_fencing"

    id = Column(Integer, primary_key=True, index=True)
    asset_id = Column(Integer, ForeignKey(AssetModel.id))
    lower_left_geo_lat = Column(Float, nullable=False)
    lower_left_geo_long = Column(Float, nullable=False)
    upper_right_geo_lat = Column(Float, nullable=False)
    upper_right_geo_long = Column(Float, nullable=False)
    geo_variance = Column(Float, nullable=False)
    max_failure_count = Column(Integer, nullable=False, default=5)
    reset_failure_count = Column(Integer, nullable=False, default=3)
    active = Column(Boolean, default=False)

    create_date = Column(DateTime, default=_datetime.datetime.utcnow())
    update_date = Column(DateTime, default=_datetime.datetime.utcnow())
    created_by = Column(Integer, ForeignKey(UserModel.id))
    updated_by = Column(Integer, ForeignKey(UserModel.id))