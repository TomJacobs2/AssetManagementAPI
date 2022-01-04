#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from .command_base import CommandBase
from app.data.models.asset_geo_fence_model import AssetGeoFenceModel
from app.schema.asset_geo_fence_schema import AssetGeoFenceCreate, AssetGeoFenceUpdate


class AssetGeoFenceCommand(CommandBase[AssetGeoFenceModel, AssetGeoFenceCreate, AssetGeoFenceUpdate]):
    ...


asset_geo_fence_cmd = AssetGeoFenceCommand(AssetGeoFenceModel)

