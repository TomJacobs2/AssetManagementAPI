#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from app.data.database_app import database_app
from app.schema.event_schema import EventRequest
from app.data.models.event_type_model import EventTypeModel
from app.data.commands.type_command import get_type_by_code


class EventBase:
    event_type_code: str

    def __init__(self, event_schema: EventRequest):
        self.event_schema = event_schema
        self.asset_tag = event_schema.asset_tag
        self.geo_lat = event_schema.geo_lat
        self.geo_long = event_schema.geo_long
        self.event_data = event_schema.event_data
        self.additional_data: dict = []

    def get_event_type_id(self, code: str):
        return get_type_by_code(db=database_app.get_session(), model=EventTypeModel, code=code).id
