#  Copyright (c) Thomas Jacobs. All Rights Reserved.

import unittest

from app.data.database_app import database_app
from app.data.commands.user_command import user_cmd



class TestLoadUserCommand(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Start User Command")

    @classmethod
    def tearDownClass(cls):
        print('Finished User Command')

    def setUp(self):
        self.session = database_app.get_session()

    def tearDown(self):
        pass

    def test_get_one(self):
        results = user_cmd.get_one(db=self.session, model_id=1)
        self.assertEqual(results.first_name, "Super")
        self.assertEqual(results.last_name, "User")

    def test_get_all(self):
        results = user_cmd.get_all(db=self.session)
        self.assertGreater(len(results), 0)

    def test_get_user_by_credentials(self):
        results = user_cmd.get_user_by_credentials(db=self.session, username="super.user", password="SpiderMonkeys2")
        self.assertEqual(results.first_name, "Super")
        self.assertEqual(results.last_name, "User")

    def test_get_user_by_email(self):
        results = user_cmd.get_user_by_email(db=self.session, email="super.user@newassetcompany.com")
        self.assertEqual(results.first_name, "Super")
        self.assertEqual(results.last_name, "User")


if __name__ == '__main__':
    print("run tests from the run_tests file in the main directory")
