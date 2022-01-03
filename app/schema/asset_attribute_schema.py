#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from pydantic import BaseModel
from typing import Sequence


class AssetAttributeBase(BaseModel):
    asset_id: int
    attribute_type_id: int
    attribute_value: str
    last_updated_on: str
    retired: bool


class AssetAttributeCreate(AssetAttributeBase):
    created_by: int
    updated_by: int


class AssetAttributeUpdate(AssetAttributeBase):
    id: int
    created_by: int
    updated_by: int


class AssetAttributeInDBBase(AssetAttributeBase):
    id: int
    create_date: str

    class Config:
        orm_mode = True


class AssetAttribute(AssetAttributeInDBBase):
    pass


class AssetAttributeSearchResults(BaseModel):
    results: Sequence[AssetAttribute]
