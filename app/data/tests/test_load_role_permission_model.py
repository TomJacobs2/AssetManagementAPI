#  Copyright (c) Thomas Jacobs. All Rights Reserved.

import unittest
from typing import Any

from app.data.database_app import database_app
from app.data.commands.role_permission_command import get_role_permission_by_code, get_role_permission_for_external
from app.data.commands.role_permission_command import get_all, get_role_permission_by_id
from app.data.models.role_model import RoleModel


class TestLoadTypeModels(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Start Test Role Permission Models")

    @classmethod
    def tearDownClass(cls):
        print('Finished Test Role Permission Models')

    def setUp(self):
        self.session = database_app.get_session()

    def tearDown(self):
        pass

    def select_model_by_code(self, model_list: Any, code: str):
        return [rec for rec in model_list if rec.code == code].pop()

    def test_get_all(self):
        models = get_all(db=self.session, model=RoleModel)
        self.assertEqual(len(models), 8)
        self.assertEqual(self.select_model_by_code(model_list=models, code="superuser").code, "superuser")
        self.assertEqual(self.select_model_by_code(model_list=models, code="adminuser").code, "adminuser")
        self.assertEqual(self.select_model_by_code(model_list=models, code="accountmanager").code, "accountmanager")
        self.assertEqual(self.select_model_by_code(model_list=models, code="assetmanager").code, "assetmanager")
        self.assertEqual(self.select_model_by_code(model_list=models, code="custservice").code, "custservice")
        self.assertEqual(self.select_model_by_code(model_list=models, code="acctadmin").code, "acctadmin")
        self.assertEqual(self.select_model_by_code(model_list=models, code="acctbilling").code, "acctbilling")
        self.assertEqual(self.select_model_by_code(model_list=models, code="acctuser").code, "acctuser")

    def test_get_role_permission_by_id(self):
        results = get_role_permission_by_id(db=self.session, model=RoleModel, id=1)
        self.assertEqual(results.code, "superuser")

    def test_get_role_permission_by_code(self):
        results = get_role_permission_by_code(db=self.session, model=RoleModel, code="adminuser")
        self.assertEqual(results.code, "adminuser")

    def test_get_role_permission_for_external_true(self):
        results = get_role_permission_for_external(db=self.session, model=RoleModel, for_external=True)
        self.assertEqual(len(results), 3)

    def test_get_role_permission_for_external_false(self):
        results = get_role_permission_for_external(db=self.session, model=RoleModel, for_external=False)
        self.assertEqual(len(results), 5)


if __name__ == '__main__':
    print("run tests from the run_tests file in the main directory")