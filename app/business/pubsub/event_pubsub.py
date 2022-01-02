#  Copyright (c) Thomas Jacobs. All Rights Reserved.


from app.business.pubsub.subscribers.subscriber_base import SubscriberBase
from app.business.events.event_base import EventBase
from app.business.pubsub.subscribers.error_subscriber import ErrorSubscriber


class EventPubSub:
    def __init__(self):
        self.subscribers = dict()
        subscribers = SubscriberBase.__subclasses__()
        for sub_class in subscribers:
            for evt in sub_class.subscribed_events:
                self.subscribe(event_type=evt, event_class=sub_class)

    def subscribe(self, event_type: str, event_class):
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(event_class)

    def unsubscribe(self, event_type: str, event_class):
        if event_type in self.subscribers:
            self.subscribers[event_type].remove(event_class)

    def publish_event(self, event_type: str, event: EventBase):
        if event_type not in self.subscribers:
            return
        """ TODO: Parallelize for loop """
        for event_class in self.subscribers[event_type]:
            event_class().process_event(event)


event_pubsub = EventPubSub()