#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from app.data.database_app import database_app
from app.schema.asset_geo_fence_schema import AssetGeoFenceCreate
from app.data.commands.asset_geo_fence_command import asset_geo_fence_cmd


raw_data = {"asset_id": 7, "lower_left_geo_lat": 38.774480, "lower_left_geo_long": -92.257180,
            "upper_right_geo_lat": 38.775480, "upper_right_geo_long": -92.256180, "geo_variance": .000300,
            "max_failure_count": 6, "reset_failure_count": 4, "active": 1}
schema = AssetGeoFenceCreate(**raw_data)
asset_geo_fence_cmd.create(db=database_app.get_session(), schema_in=schema)

raw_data = {"asset_id": 2, "lower_left_geo_lat": 38.777480, "lower_left_geo_long": -92.256180,
            "upper_right_geo_lat": 38.775480, "upper_right_geo_long": -92.256180, "geo_variance": .000300,
            "max_failure_count": 3, "reset_failure_count": 3, "active": 1}
schema = AssetGeoFenceCreate(**raw_data)
asset_geo_fence_cmd.create(db=database_app.get_session(), schema_in=schema)
