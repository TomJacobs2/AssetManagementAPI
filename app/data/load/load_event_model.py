#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from app.data.database_app import database_app
from app.schema.event_schema import EventCreate
from app.data.models.event_type_model import EventTypeModel
from app.data.commands.event_command import event_cmd
from app.data.commands.asset_command import asset_cmd
from app.data.commands.type_command import get_type_by_code

asset_telsa_id = asset_cmd.get_asset_by_tag(db=database_app.get_session(), asset_tag="TEMSP2022002").id
asset_ford_id = asset_cmd.get_asset_by_tag(db=database_app.get_session(), asset_tag="FDF1502022002").id
event_poweron_id = get_type_by_code(db=database_app.get_session(), model=EventTypeModel, code="power_on").id
event_poweroff_id = get_type_by_code(db=database_app.get_session(), model=EventTypeModel, code="power_off").id
event_speed_id = get_type_by_code(db=database_app.get_session(), model=EventTypeModel, code="speed").id

raw_data = {"event_type_id": event_poweron_id, "asset_id": asset_telsa_id, "geo_lat": 38.774480, "geo_long": -92.257130}
schema = EventCreate(**raw_data)
event_cmd.create(db=database_app.get_session(), schema_in=schema)

raw_data = {"event_type_id": event_speed_id, "asset_id": asset_telsa_id, "geo_lat": 38.775480, "geo_long": -92.257330,
            "event_data": '{"speed": 138}'}
schema = EventCreate(**raw_data)
event_cmd.create(db=database_app.get_session(), schema_in=schema)

raw_data = {"event_type_id": event_poweroff_id, "asset_id": asset_telsa_id, "geo_lat": 38.774480, "geo_long": -92.257130}
schema = EventCreate(**raw_data)
event_cmd.create(db=database_app.get_session(), schema_in=schema)

raw_data = {"event_type_id": event_poweron_id, "asset_id": asset_ford_id, "geo_lat": 38.774480, "geo_long": -92.257130}
schema = EventCreate(**raw_data)
event_cmd.create(db=database_app.get_session(), schema_in=schema)

raw_data = {"event_type_id": event_poweroff_id, "asset_id": asset_ford_id, "geo_lat": 38.774480, "geo_long": -92.257130}
schema = EventCreate(**raw_data)
event_cmd.create(db=database_app.get_session(), schema_in=schema)
