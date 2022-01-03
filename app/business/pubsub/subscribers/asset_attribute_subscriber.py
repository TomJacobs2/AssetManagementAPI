#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from .subscriber_base import SubscriberBase
from app.business.events.event_base import EventBase


class AssetAttributeSubscriber(SubscriberBase):
    subscribed_events = {"power_on", "power_off", "speed", "location"}

    def __init__(self):
        pass

    def process_event(self, event: EventBase):
        print("Send Message Subscriber: " + event.asset_tag)
        print(type(event))
