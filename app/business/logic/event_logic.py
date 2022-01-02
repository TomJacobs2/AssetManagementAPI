#  Copyright (c) Thomas Jacobs. All Rights Reserved.

import json
from datetime import datetime
from app.business.pubsub.event_factory import event_factory
from app.business.pubsub.event_pubsub import event_pubsub
from app.schema.event_schema import EventRequest, EventCreate
from app.data.commands.event_command import event_cmd
from app.data.commands.asset_command import asset_cmd
from app.data.models.event_type_model import EventTypeModel
from app.data.commands.type_command import get_type_by_code
from app.data.database_app import database_app



class EventLogic:
    def __init__(self):
       self.session = database_app.get_session()

    def convert_request_to_create_schema(self, request_schema: EventRequest) -> EventCreate:
        asset_row = asset_cmd.get_asset_by_tag(db=self.session, asset_tag=request_schema.asset_tag)
        event_type_id = get_type_by_code(db=self.session, model=EventTypeModel, code=request_schema.event_type_code).id
        raw_data = {"event_type_id": event_type_id, "geo_lat": request_schema.geo_lat,
                    "geo_long": request_schema.geo_long, "event_data": request_schema.event_data,
                    "asset_id": asset_row.id}
        return EventCreate(**raw_data)

    def process_get_asset(self, asset_id: int):
        print(f"Event Logic: get events for asset with id of {asset_id}")
        return event_cmd.get_events_for_asset(db=self.session, asset_id=asset_id)

    def process_post(self, request: EventRequest):
        create_schema = self.convert_request_to_create_schema(request_schema=request)
        results = event_cmd.create(db=self.session, schema_in=create_schema)
        request.event_data = results
        event = event_factory.get_event_class(request)
        event_pubsub.publish_event(event_type=event.event_type_code, event=event)
        return results
