#  Copyright (c) Thomas Jacobs. All Rights Reserved.

import datetime as _datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean

from app.data.database_app import Base
from .user_model import UserModel
from .attribute_type_model import AttributeTypeModel
from .asset_model import AssetModel


class AssetAttributeModel(Base):
    __tablename__ = "asset_attributes"

    id = Column(Integer, primary_key=True, index=True)
    asset_id = Column(Integer, ForeignKey(AssetModel.id))
    attribute_type_id = Column(Integer, ForeignKey(AttributeTypeModel.id))
    attribute_value = Column(String(64), nullable=True)
    last_updated_on = Column(DateTime, default=_datetime.datetime.utcnow())
    retired = Column(Boolean, default=False)

    create_date = Column(DateTime, default=_datetime.datetime.utcnow())
    update_date = Column(DateTime, default=_datetime.datetime.utcnow())
    created_by = Column(Integer, ForeignKey(UserModel.id))
    updated_by = Column(Integer, ForeignKey(UserModel.id))
