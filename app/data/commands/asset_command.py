#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from sqlalchemy.orm import Session

from .command_base import CommandBase
from app.data.models.asset_model import AssetModel
from app.schema.asset_schema import AssetCreate, AssetUpdate


class AssetCommand(CommandBase[AssetModel, AssetCreate, AssetUpdate]):
    ...

    def get_asset_by_tag(self, db: Session, asset_tag: str):
        return db.query(self.model).filter(self.model.asset_tag == asset_tag).first()


asset_cmd = AssetCommand(AssetModel)
