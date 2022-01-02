#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from app.schema.event_schema import EventRequest
from .event_base import EventBase


class AssetReturnedEvent(EventBase):
    event_type_code = "asset_returned"

    def __init__(self, event_schema: EventRequest):
        super().__init__(event_schema)
