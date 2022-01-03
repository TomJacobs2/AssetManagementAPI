#  Copyright (c) Thomas Jacobs. All Rights Reserved.

import datetime as _datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from app.data.database_app import Base
from .user_model import UserModel
from .asset_category_type_model import AssetCategoryTypeModel
from .asset_manufacturer_type_model import AssetManufacturerTypeModel


class AssetModel(Base):
    __tablename__ = "assets"

    id = Column(Integer, primary_key=True, index=True)
    asset_tag = Column(String(32), nullable=False, index=True, unique=True)
    description = Column(String(256), nullable=False)
    model_year = Column(String(4))
    mileage = Column(Integer, nullable=False)
    hours_ran = Column(Integer, nullable=False)
    color = Column(String(64), nullable=True)
    asset_category_id = Column(Integer, ForeignKey(AssetCategoryTypeModel.id))
    asset_manufacturer_id = Column(Integer, ForeignKey(AssetManufacturerTypeModel.id))
    retired = Column(Boolean, default=False)

    geo_fencing = relationship("AssetGeoFencingModel")
    time_fencing = relationship("AssetTimeFencingModel")

    create_date = Column(DateTime, default=_datetime.datetime.utcnow())
    update_date = Column(DateTime, default=_datetime.datetime.utcnow())
    created_by = Column(Integer, ForeignKey(UserModel.id))
    updated_by = Column(Integer, ForeignKey(UserModel.id))
