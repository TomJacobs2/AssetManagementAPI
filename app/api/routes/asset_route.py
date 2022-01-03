#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from fastapi import APIRouter

from app.schema.asset_schema import AssetRequest
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
async def post_action(request: AssetRequest):
    return logic.process_post(request=request)


@router.put("/", tags=["assets"])
async def put_action(request: AssetRequest):
    return logic.process_post(request=request)


@router.delete("/", tags=["assets"])
async def delete_action(asset_id: str):
    return logic.process_delete(asset_id=asset_id)
