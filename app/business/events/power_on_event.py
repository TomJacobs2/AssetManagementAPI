#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from app.schema.event_schema import EventRequest
from .event_base import EventBase


class PowerOnEvent(EventBase):
    event_type_code = "power_on"

    def __init__(self, event_schema: EventRequest):
        super().__init__(event_schema)
    