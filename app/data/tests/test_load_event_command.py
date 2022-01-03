#  Copyright (c) Thomas Jacobs. All Rights Reserved.

import unittest

from app.data.database_app import database_app
from app.data.models.event_type_model import EventTypeModel
from app.data.commands.event_command import event_cmd
from app.data.commands.asset_command import asset_cmd
from app.data.commands.type_command import get_type_by_code

telsa_asset_id = asset_cmd.get_asset_by_tag(db=database_app.get_session(), asset_tag="TEMSP2022002").id
ford_asset_id = asset_cmd.get_asset_by_tag(db=database_app.get_session(), asset_tag="FDF1502022002").id
event_poweron_id = get_type_by_code(db=database_app.get_session(), model=EventTypeModel, code="power_on").id
event_poweroff_id = get_type_by_code(db=database_app.get_session(), model=EventTypeModel, code="power_off").id
event_speed_id = get_type_by_code(db=database_app.get_session(), model=EventTypeModel, code="speed").id


class TestLoadEventCommand(unittest.TestCase):

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

    def test_get_asset_events(self):
        results = event_cmd.get_events_for_sub_type(db=database_app.get_session(), subtype_code="asset",
                                                    fk_link_id=telsa_asset_id)
        self.assertEqual(len(results), 3)

    def test_get_user_events(self):
        results = event_cmd.get_events_for_sub_type(db=database_app.get_session(), subtype_code="user",
                                                    fk_link_id=ford_asset_id)
        self.assertEqual(len(results), 1)

    def test_get_account_events(self):
        results = event_cmd.get_events_for_sub_type(db=database_app.get_session(), subtype_code="account",
                                                    fk_link_id=ford_asset_id)
        self.assertEqual(len(results), 1)


if __name__ == '__main__':
    print("run tests from the run_tests file in the main directory")