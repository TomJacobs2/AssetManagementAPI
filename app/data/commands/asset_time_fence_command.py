#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from .command_base import CommandBase
from app.data.models.asset_time_fence_model import AssetTimeFenceModel
from app.schema.asset_time_fence_schema import AssetTimeFenceCreate, AssetTimeFenceUpdate


class AssetTimeFenceCommand(CommandBase[AssetTimeFenceModel, AssetTimeFenceCreate, AssetTimeFenceUpdate]):
    ...


asset_time_fence_cmd = AssetTimeFenceCommand(AssetTimeFenceModel)