#  Copyright (c) Thomas Jacobs. All Rights Reserved.

import unittest

from app.data.database_app import database_app
from app.data.models.event_type_model import EventTypeModel
from app.data.commands.event_command import event_cmd
from app.data.commands.asset_command import asset_cmd
from app.data.commands.type_command import get_type_by_code

asset_id = asset_cmd.get_asset_by_tag(db=database_app.get_session(), asset_tag="TEMSP2022002").id
event_poweron_id = get_type_by_code(db=database_app.get_session(), model=EventTypeModel, code="power_on").id

class TestLoadAssetCommand(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Start Test Event Command")

    @classmethod
    def tearDownClass(cls):
        print('Finished Test Event Command')

    def setUp(self):
        self.session = database_app.get_session()

    def tearDown(self):
        pass

    def test_get_one(self):
        results = event_cmd.get_one(db=database_app.get_session(), model_id=1)
        self.assertEqual(results.event_type_id, event_poweron_id)

    def test_get_all(self):
        results = event_cmd.get_all(db=database_app.get_session())
        self.assertEqual(len(results), 5)

    def test_get(self):
        results = event_cmd.get_events_for_asset(db=database_app.get_session(), asset_id=asset_id)
        self.assertEqual(len(results), 3)
