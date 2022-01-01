#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from typing import Any
from fastapi import APIRouter

from app.business.logic.asset_logic import AssetLogic
logic = AssetLogic()

router = APIRouter(prefix="/asset",
                   tags=["assets"],
                   responses={404: {"description": "Not Found"}})


@router.get("/", tags=["assets"])
async def get_action():
    return logic.process_get_all()


@router.get("/{asset_id}", tags=["assets"])
async def get_action(asset_id: int):
    return logic.process_get_asset(asset_id)


@router.post("/", tags=["assets"])
async def post_action(request: Any):
    return logic.process_post(request=request)


@router.put("/", tags=["assets"])
async def put_action(request: Any):
    return logic.process_post(request=request)


@router.delete("/", tags=["assets"])
async def delete_action(asset_id: int):
    return {"msg": f"Delete asset {asset_id}"}
