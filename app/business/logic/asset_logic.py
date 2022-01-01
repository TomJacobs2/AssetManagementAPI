#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from app.data.database_app import database_app
from app.schema.asset_schema import AssetRequest
from app.data.commands.asset_command import asset_cmd

class AssetLogic:
    def __init__(self):
        self.session = database_app.get_session()

    def process_get_all(self):
        return asset_cmd.get_all(db=self.session)

    def process_get_asset(self, asset_id: int):
        return asset_cmd.get_one(db=self.session, model_id=asset_id)

    def process_post(self, request: AssetRequest):
        return asset_cmd.create_from_request(db=self.session, schema_in=request)

    def process_put(self, request: AssetRequest):
        return asset_cmd.update(db=self.session, schema_in=request)

    def process_delete(self, asset_id: int):
        return asset_cmd.retired_asset(db=self.session, asset_id=asset_id)
