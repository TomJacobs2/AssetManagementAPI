#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from pydantic import BaseModel
from typing import Sequence, Optional


class AssetBase(BaseModel):
    asset_tag: str
    description: str
    model_year: str
    mileage: Optional[int] = 0
    hours_ran: Optional[int] = 0
    color: Optional[str] = None
    asset_category_id: int
    asset_manufacturer_id: int


class AssetCreate(AssetBase):
    created_by: int
    updated_by: int


class AssetUpdate(AssetBase):
    id: int
    created_by: int
    updated_by: int


class AssetInDBBase(AssetBase):
    id: int
    create_date: str

    class Config:
        orm_mode = True


class Asset(AssetInDBBase):
    pass


class AssetSearchResults(BaseModel):
    results: Sequence[Asset]


class AssetRequest(BaseModel):
    asset_tag: str
    description: str
    model_year: str
    mileage: Optional[int] = 0
    hours_ran: Optional[int] = 0
    color: Optional[str] = None
    asset_category_code: str
    asset_manufacturer_code: str