#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from .subscriber_base import SubscriberBase
from app.business.events.event_base import EventBase
from app.business.events.process_error_event import ProcessErrorEvent

class ErrorSubscriber(SubscriberBase):
    subscribed_events = {"process_error"}

    def __init__(self):
        pass

    def process_event(self, event: EventBase):
        print("Error Subscriber: " + event.asset_tag)
        if isinstance(event, ProcessErrorEvent):
            print("event.additional_data.description")
        print(type(event))