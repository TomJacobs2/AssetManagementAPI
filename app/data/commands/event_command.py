#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from sqlalchemy.orm import Session
from .command_base import CommandBase
from app.data.models.event_model import EventModel
from app.data.models.event_subtype_model import EventSubTypeModel
from app.schema.event_schema import EventCreate, EventUpdate


class EventCommand(CommandBase[EventModel, EventCreate, EventUpdate]):
    ...


    subtype_codes: dict = None

    def get_events_for_sub_type(self, db: Session, subtype_code:str,  fk_link_id: int):
        if self.subtype_codes is None:
            self.subtype_codes = db.query(EventSubTypeModel).all()
        subtype_code_id = next(typecode for typecode in self.subtype_codes if typecode.code == subtype_code).id
        return db.query(self.model).filter(self.model.fk_subtype_link_id == fk_link_id,
                                           self.model.event_subtype_id == subtype_code_id).all()


event_cmd = EventCommand(EventModel)
