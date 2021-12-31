#  Copyright (c) Thomas Jacobs. All Rights Reserved.

"""
All of the type models are built the same way. So I should only need to model for the type_command test
"""

import unittest

from app.data.database_app import database_app
from app.data.commands.type_command import get_all, get_type_by_code, get_type_by_id
from app.data.models.cost_type_model import CostTypeModel


class TestTypeCommand(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Start Test Type Command")

    @classmethod
    def tearDownClass(cls):
        print('Finished Test Type Command')

    def setUp(self):
        self.session = database_app.get_session()

    def tearDown(self):
        pass

    def test_get_all(self):
        results = get_all(db=self.session, model=CostTypeModel)
        self.assertTrue(isinstance(results.pop(), CostTypeModel))

    def test_get_type_by_code(self):
        results = get_type_by_code(db=self.session, model=CostTypeModel, code="pickup")
        self.assertTrue(isinstance(results, CostTypeModel))
        self.assertEqual(results.code, "pickup")

    def test_get_type_by_id(self):
        results = get_type_by_id(db=self.session, model=CostTypeModel, id=1)
        self.assertTrue(isinstance(results, CostTypeModel))
        self.assertEqual(results.code, "pickup")


if __name__ == '__main__':
    print("run tests from the run_tests file in the main directory")
