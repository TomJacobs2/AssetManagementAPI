#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from sqlalchemy.orm import Session

from .command_base import CommandBase
from app.data.models.asset_model import AssetModel
from app.schema.asset_schema import AssetCreate, AssetUpdate


class AssetCommand(CommandBase[AssetModel, AssetCreate, AssetUpdate]):
    ...

    def get_asset_by_tag(self, db: Session, asset_tag: str):
        return db.query(self.model).filter(self.model.asset_tag == asset_tag).first()

    def get_asset_by_category_id(self, db: Session, category_id: int):
        return db.query(self.model).filter(self.model.asset_category_id == category_id).all()

    def get_asset_by_manufacturer_id(self, db: Session, manufacturer_id):
        return db.query(self.model).filter(self.model.asset_manufacturer_id == manufacturer_id).all()


asset_cmd = AssetCommand(AssetModel)
