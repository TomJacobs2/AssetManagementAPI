#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from .subscriber_base import SubscriberBase
from app.business.events.event_base import EventBase
from app.business.events.process_error_event import ProcessErrorEvent

class ErrorSubscriber(SubscriberBase):
    subscribed_events = {"send_chat", "send_email", "send_text"}

    def __init__(self):
        pass

    def process_event(self, event: EventBase):
        print("Send Message Subscriber: " + event.asset_tag)
        if isinstance(event, ProcessErrorEvent):
            print(event.event_data)
        print(type(event))
