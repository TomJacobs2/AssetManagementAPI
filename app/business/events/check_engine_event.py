#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from app.schema.event_schema import EventRequest
from .event_base import EventBase


class CheckEngineEvent(EventBase):
    event_type_code = "check_engine"

    def __init__(self, event_schema: EventRequest):
        super().__init__(event_schema)
