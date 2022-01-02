#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from app.business.events.event_base import EventBase
from app.schema.event_schema import EventRequest
from app.business.events import *


class EventFactory:
    def __init__(self):
        self.event_types = dict()
        events = EventBase.__subclasses__()
        for rec in events:
            self.event_types[rec.event_type_code] = rec

    def get_event_class(self, event_schema: EventRequest):
        return self.event_types[event_schema.event_type_code](event_schema)


event_factory = EventFactory()