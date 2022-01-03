#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from pydantic import BaseModel
from typing import Sequence, Optional


class AssetGeoFencingBase(BaseModel):
    asset_id: int
    lower_left_geo_lat: float
    lower_left_geo_long: float
    upper_right_geo_lat: float
    upper_right_geo_lat: float
    max_failure_count: int
    reset_failure_count: int
    active: bool


class AssetGeoFencingCreate(AssetGeoFencingBase):
    pass


class AssetGeoFencingUpdate(AssetGeoFencingBase):
    id: int


class AssetGeoFencingInDBBase(AssetGeoFencingBase):
    id: int
    create_date: str

    class Config:
        orm_mode = True


class AssetGeoFencing(AssetGeoFencingInDBBase):
    pass


class AssetGeoFencingSearchResults(BaseModel):
    results: Sequence[AssetGeoFencing]
