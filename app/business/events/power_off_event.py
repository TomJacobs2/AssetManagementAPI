#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from app.schema.event_schema import EventRequest
from .event_base import EventBase


class PowerOffEvent(EventBase):
    event_type_code = "power_off"

    def __init__(self, event_schema: EventRequest):
        super().__init__(event_schema)
        