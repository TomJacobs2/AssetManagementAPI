#  Copyright (c) Thomas Jacobs. All Rights Reserved.

import unittest

from app.data.database_app import database_app
from app.data.commands.account_command import account_cmd
from app.data.commands.user_command import user_cmd


class TestLoadAccountCommand(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Start Test Account Command")

    @classmethod
    def tearDownClass(cls):
        print('Finished Test Account Command')

    def setUp(self):
        self.session = database_app.get_session()

    def tearDown(self):
        pass

    def test_get_one(self):
        results = account_cmd.get_one(db=self.session, model_id=1)
        self.assertEqual(results.account_name, "New Spider Racing")

    def test_get_all(self):
        results = account_cmd.get_all(db=database_app.get_session())
        self.assertEqual(len(results), 2)

    def test_get_account_by_name_spider(self):
        results = account_cmd.get_account_by_account_name(db=self.session, account_name="New Spider Racing")
        self.assertEqual(results.account_number, "NAC123456")

    def test_get_account_by_name_gorilla(self):
        results = account_cmd.get_account_by_account_name(db=self.session, account_name="Gorilla Pro Racing")
        self.assertEqual(results.account_number, "NAC654987")

    def test_get_account_by_number_NAC123456(self):
        results = account_cmd.get_account_by_account_number(db=self.session, account_number="NAC123456")
        self.assertEqual(results.account_name, "New Spider Racing")

    def test_get_account_by_number_NAC654987(self):
        results = account_cmd.get_account_by_account_number(db=self.session, account_number="NAC654987")
        self.assertEqual(results.account_name, "Gorilla Pro Racing")

    def test_get_account_manager_accounts(self):
        account_manager_id = user_cmd.get_user_by_email(db=database_app.get_session(),
                                                        email="jonney.applegate@newassetcompany.com").id
        results = account_cmd.get_account_manager_accounts(db=database_app.get_session(),
                                                           account_manager_id=account_manager_id)
        self.assertEqual(len(results), 2)


if __name__ == '__main__':
    print("run tests from the run_tests file in the main directory")