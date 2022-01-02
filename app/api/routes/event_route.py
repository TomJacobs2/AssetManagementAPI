#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from fastapi import APIRouter
from app.schema.event_schema import EventRequest

from app.business.logic.event_logic import EventLogic
logic = EventLogic();

router = APIRouter(prefix="/event",
                   tags=["events"],
                   responses={404: {"description": "Not Found"}})


@router.get("/{asset_id}", tags=["assets"])
async def get_action(asset_id: int):
    return logic.process_get_asset(asset_id)


@router.post("/", tags=["assets"])
async def post_action(request: EventRequest):
    return logic.process_post(request=request)