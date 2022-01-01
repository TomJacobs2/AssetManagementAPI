#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from typing import Any
from app.data.database_app import database_app
from app.data.commands.asset_command import asset_cmd


class AssetLogic:
    def __init__(self):
        self.session = database_app.get_session()

    def process_get_all(self):
        print("Asset Logic: get all called")
        return asset_cmd.get_all(db=self.session)

    def process_get_asset(self, asset_id: int):
        print(f"Asset Logic: get asset with id of {asset_id}")
        return asset_cmd.get_one(db=self.session, model_id=asset_id)

    def process_post(self, request: Any):
        return asset_cmd.create(db=self.session, schema_in=request)

    def process_put(self, request: Any):
        return asset_cmd.update(db=self.session, schema_in=request)

    def process_delete(self, asset_id: int):
        return asset_cmd.delete(db=self.session, model_id=asset_id)