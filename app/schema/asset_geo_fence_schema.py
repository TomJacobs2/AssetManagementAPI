#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from pydantic import BaseModel
from typing import Sequence, Optional


class AssetGeoFenceBase(BaseModel):
    asset_id: int
    lower_left_geo_lat: float
    lower_left_geo_long: float
    upper_right_geo_lat: float
    upper_right_geo_long: float
    geo_variance: float
    max_failure_count: Optional[int] = 5
    reset_failure_count: Optional[int] = 5
    active: Optional[bool] = True


class AssetGeoFenceCreate(AssetGeoFenceBase):
    pass


class AssetGeoFenceUpdate(AssetGeoFenceBase):
    id: int


class AssetGeoFenceInDBBase(AssetGeoFenceBase):
    id: int
    create_date: str

    class Config:
        orm_mode = True


class AssetGeoFence(AssetGeoFenceInDBBase):
    pass


class AssetGeoFenceSearchResults(BaseModel):
    results: Sequence[AssetGeoFence]
