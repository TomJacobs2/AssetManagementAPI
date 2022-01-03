#  Copyright (c) Thomas Jacobs. All Rights Reserved.

import unittest

from app.data.database_app import database_app
from app.data.commands.type_command import get_type_by_code
from app.data.models.event_type_model import EventTypeModel
from app.business.pubsub.subscribers.error_subscriber import ErrorSubscriber
from app.business.pubsub.subscribers.send_message_subscriber import SendMessageSubscriber
from app.business.pubsub.subscribers.asset_attribute_subscriber import AssetAttributeSubscriber
from app.business.pubsub.subscribers.alert_event_subscriber import AlertEventSubscriber


class TestSubscriber(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Start Test Subscribed Event Names")

    @classmethod
    def tearDownClass(cls):
        print('Finished Test Subscribed Event Names')

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_verify_error_subscribed_event_names(self):
        for evt in ErrorSubscriber.subscribed_events:
            results = get_type_by_code(db=database_app.get_session(), model=EventTypeModel, code=evt)
            self.assertEqual(results.code, evt)

    def test_verify_send_message_subscribed_event_names(self):
        for evt in SendMessageSubscriber.subscribed_events:
            results = get_type_by_code(db=database_app.get_session(), model=EventTypeModel, code=evt)
            self.assertEqual(results.code, evt)

    def test_verify_asset_attribute_subscribed_event_names(self):
        for evt in AssetAttributeSubscriber.subscribed_events:
            results = get_type_by_code(db=database_app.get_session(), model=EventTypeModel, code=evt)
            self.assertEqual(results.code, evt)

    def test_verify_alert_event_subscribed_event_names(self):
        for evt in AlertEventSubscriber.subscribed_events:
            results = get_type_by_code(db=database_app.get_session(), model=EventTypeModel, code=evt)
            self.assertEqual(results.code, evt)


    if __name__ == '__main__':
        print("run tests from the run_tests file in the main directory")
