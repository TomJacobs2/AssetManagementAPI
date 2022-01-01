#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from sqlalchemy.orm import Session

from .command_base import CommandBase
from app.data.models.asset_model import AssetModel
from app.schema.asset_schema import AssetCreate, AssetUpdate, AssetRequest
from app.data.commands.type_command import get_type_by_code
from app.data.models.asset_manufacturer_type_model import AssetManufacturerTypeModel
from app.data.models.asset_category_type_model import AssetCategoryTypeModel


class AssetCommand(CommandBase[AssetModel, AssetCreate, AssetUpdate]):
    ...

    def get_asset_by_tag(self, db: Session, asset_tag: str):
        return db.query(self.model).filter(self.model.asset_tag == asset_tag).first()

    def get_asset_by_category_id(self, db: Session, category_id: int):
        return db.query(self.model).filter(self.model.asset_category_id == category_id).all()

    def get_asset_by_manufacturer_id(self, db: Session, manufacturer_id: int):
        return db.query(self.model).filter(self.model.asset_manufacturer_id == manufacturer_id).all()

    def retired_asset(self, db: Session, asset_id: int):
        update_str = f"""UPDATE {self.model.__tablename__} SET retired = 1 WHERE id = {asset_id};"""
        db.execute(update_str)
        db.commit()

    def create_from_request(self, db: Session, schema_in: AssetRequest):
        category_id = get_type_by_code(db=db, model=AssetCategoryTypeModel,
                                       code=schema_in.asset_category_code).id
        manufacturer_id = get_type_by_code(db=db, model=AssetManufacturerTypeModel,
                                           code=schema_in.asset_manufacturer_code).id
        raw_data = {"asset_tag": schema_in.asset_tag, "description": schema_in.description,
                    "mileage": schema_in.mileage, "model_year": schema_in.model_year,
                    "created_by": 1, "updated_by": 1, "color": schema_in.color,
                    "asset_category_id": category_id, "asset_manufacturer_id": manufacturer_id}
        schema = AssetCreate(**raw_data)
        asset_cmd.create(db=db, schema_in=schema)


asset_cmd = AssetCommand(AssetModel)
