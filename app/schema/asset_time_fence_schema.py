#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from pydantic import BaseModel
from typing import Sequence, Optional


class AssetTimeFenceBase(BaseModel):
    asset_id: int
    mon_allowed_start_time: Optional[int] = 600
    mon_allowed_end_time: Optional[int] = 1800
    tue_allowed_start_time: Optional[int] = 600
    tue_allowed_end_time: Optional[int] = 1800
    wed_allowed_start_time: Optional[int] = 600
    wed_allowed_end_time: Optional[int] = 1800
    thu_allowed_start_time: Optional[int] = 600
    thu_allowed_end_time: Optional[int] = 1800
    fri_allowed_start_time: Optional[int] = 600
    fri_allowed_end_time: Optional[int] = 1800
    sat_allowed_start_time: Optional[int] = 600
    sat_allowed_end_time: Optional[int] = 1800
    sun_allowed_start_time: Optional[int] = 600
    sun_allowed_end_time: Optional[int] = 1800
    active: bool


class AssetTimeFenceCreate(AssetTimeFenceBase):
    pass


class AssetTimeFenceUpdate(AssetTimeFenceBase):
    id: int


class AssetTimeFenceInDBBase(AssetTimeFenceBase):
    id: int
    create_date: str

    class Config:
        orm_mode = True


class AssetTimeFence(AssetTimeFenceInDBBase):
    pass


class AssetTimeFenceSearchResults(BaseModel):
    results: Sequence[AssetTimeFence]
