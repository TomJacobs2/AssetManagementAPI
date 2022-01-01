#  Copyright (c) Thomas Jacobs. All Rights Reserved.

import unittest

from app.data.database_app import database_app
from app.data.commands.asset_command import asset_cmd
from app.data.models.asset_category_type_model import AssetCategoryTypeModel
from app.data.commands.type_command import get_type_by_code
from app.data.models.asset_manufacturer_type_model import AssetManufacturerTypeModel


class TestLoadAssetCommand(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Start Test Asset Command")

    @classmethod
    def tearDownClass(cls):
        print('Finished Test Asset Command')

    def setUp(self):
        self.session = database_app.get_session()

    def tearDown(self):
        pass

    def test_get_one(self):
        results = asset_cmd.get_one(db=self.session, model_id=1)
        self.assertEqual(results.asset_tag, "FE8122021001")
        self.assertEqual(results.description, "Ferrari 812 Superfast")
        self.assertEqual(results.mileage, 4445)
        self.assertEqual(results.color, "Rosso Fiorando")
        self.assertEqual(results.model_year, "2021")

    def test_get_all(self):
        results = asset_cmd.get_all(db=self.session)
        self.assertEqual(len(results), 12)

    def test_get_asset_by_tag(self):
        results = asset_cmd.get_asset_by_tag(db=self.session, asset_tag="TEMSP2022001")
        self.assertEqual(results.description, "Model S Plaid")
        self.assertEqual(results.mileage, 1359)
        self.assertEqual(results.color, "Midnight Silver Metallic")
        self.assertEqual(results.model_year, "2022")

    def test_get_asset_by_category_id_esport(self):
        category_id = get_type_by_code(db=self.session, model=AssetCategoryTypeModel, code="esport").id
        results = asset_cmd.get_asset_by_category_id(db=self.session, category_id=category_id)
        self.assertEqual(len(results), 2)

    def test_get_asset_by_category_id_sport(self):
        category_id = get_type_by_code(db=self.session, model=AssetCategoryTypeModel, code="sport").id
        results = asset_cmd.get_asset_by_category_id(db=self.session, category_id=category_id)
        self.assertEqual(len(results), 7)

    def test_get_asset_by_category_id_truck(self):
        category_id = get_type_by_code(db=self.session, model=AssetCategoryTypeModel, code="truck").id
        results = asset_cmd.get_asset_by_category_id(db=self.session, category_id=category_id)
        self.assertEqual(len(results), 3)

    def test_get_asset_by_manufacturer_id_ford(self):
        manufacturer_id = get_type_by_code(db=self.session, model=AssetManufacturerTypeModel, code="ford").id
        results = asset_cmd.get_asset_by_manufacturer_id(db=self.session, manufacturer_id=manufacturer_id)
        self.assertEqual(len(results), 3)

    def test_get_asset_by_manufacturer_id_ferrari(self):
        manufacturer_id = get_type_by_code(db=self.session, model=AssetManufacturerTypeModel, code="ferrari").id
        results = asset_cmd.get_asset_by_manufacturer_id(db=self.session, manufacturer_id=manufacturer_id)
        self.assertEqual(len(results), 4)

    def test_get_asset_by_manufacturer_id_telsa(self):
        manufacturer_id = get_type_by_code(db=self.session, model=AssetManufacturerTypeModel, code="telsa").id
        results = asset_cmd.get_asset_by_manufacturer_id(db=self.session, manufacturer_id=manufacturer_id)
        self.assertEqual(len(results), 2)

    def test_get_asset_by_manufacturer_id_lamborghini(self):
        manufacturer_id = get_type_by_code(db=self.session, model=AssetManufacturerTypeModel, code="lamborghini").id
        results = asset_cmd.get_asset_by_manufacturer_id(db=self.session, manufacturer_id=manufacturer_id)
        self.assertEqual(len(results), 3)


if __name__ == '__main__':
    print("run tests from the run_tests file in the main directory")