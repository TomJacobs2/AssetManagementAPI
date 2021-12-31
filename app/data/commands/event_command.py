#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from sqlalchemy.orm import Session
from .command_base import CommandBase
from app.data.models.event_model import EventModel
from app.schema.event_schema import EventCreate, EventUpdate


class EventCommand(CommandBase[EventModel, EventCreate, EventUpdate]):
    ...

    def get_events_for_asset(self, db: Session, asset_id: int):
        return db.query(self.model).filter(self.model.asset_id == asset_id).all()


event_cmd = EventCommand(EventModel)