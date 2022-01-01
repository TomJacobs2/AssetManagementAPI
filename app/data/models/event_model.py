#  Copyright (c) Thomas Jacobs. All Rights Reserved.

import datetime as _datetime
from sqlalchemy import Column, Integer, DateTime, ForeignKey, Float, String
from sqlalchemy.orm import relationship

from app.data.database_app import Base
from .event_type_model import EventTypeModel
from .asset_model import AssetModel


class EventModel(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    event_type_id = Column(Integer, nullable=False)
    geo_lat = Column(Float, nullable=True) #store decimal degrees
    geo_long = Column(Float, nullable=True) #store decimal degrees
    event_data = Column(String, nullable=True)
    create_date = Column(DateTime, default=_datetime.datetime.utcnow())
    asset_id = Column(Integer, ForeignKey(AssetModel.id))
