#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from .subscriber_base import SubscriberBase
from app.business.events.event_base import EventBase


class AlertEventSubscriber(SubscriberBase):
    subscribed_events = {"battery_disconnected", "rollover", "sudden_stop", "airbags_deployed", "over_heating",
                         "tire_pressure", "check_engine", "maintenance"}

    def __init__(self):
        pass

    def process_event(self, event: EventBase):
        print("Send Message Subscriber: " + event.asset_tag)
        print(type(event))
