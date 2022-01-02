#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from app.schema.event_schema import EventRequest
from .event_base import EventBase


class ProcessErrorEvent(EventBase):
    event_type_code = "process_error"

    def __init__(self, event_schema: EventRequest):
        super().__init__(event_schema)
