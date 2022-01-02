#  Copyright (c) Thomas Jacobs. All Rights Reserved.

import datetime as _datetime
from sqlalchemy import Column, Integer, DateTime, ForeignKey, Float, String
from sqlalchemy.orm import relationship

from app.data.database_app import Base



class EventModel(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    event_type_id = Column(Integer, nullable=False)
    event_subtype_id = Column(Integer, nullable=False, index=True)
    fk_subtype_link_id = Column(Integer, nullable=False, index=True)       #id link to subtype entity
    geo_lat = Column(Float, nullable=True)          #store decimal degrees
    geo_long = Column(Float, nullable=True)         #store decimal degrees
    event_data = Column(String, nullable=True)
    create_date = Column(DateTime, default=_datetime.datetime.utcnow())

