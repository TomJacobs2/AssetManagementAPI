#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from datetime import datetime
from pydantic import BaseModel
from typing import Sequence, Optional


class EventBase(BaseModel):
    event_type_id: int
    event_subtype_id: int
    fk_subtype_link_id: int
    geo_lat: Optional[float] = 0
    geo_long: Optional[float] = 0
    event_data: Optional[str] = ""


class EventCreate(EventBase):
    pass


class EventUpdate(EventBase):
    id: int


class EventInDBBase(EventBase):
    id: int
    create_date: str

    class Config:
        orm_mode = True


class Event(EventInDBBase):
    pass


class EventSearchResults(BaseModel):
    results: Sequence[Event]


class EventRequest(BaseModel):
    event_type_code: str
    event_subtype_code: str
    asset_tag: str
    geo_lat: Optional[float] = 0
    geo_long: Optional[float] = 0
    event_data: Optional[str] = ""
