#  Copyright (c) Thomas Jacobs. All Rights Reserved.

import unittest
from typing import Any

from app.data.database_app import database_app
from app.data.commands.type_command import get_all
from app.data.models.cost_type_model import CostTypeModel
from app.data.models.frequency_type_model import FrequencyTypeModel
from app.data.models.invoice_status_type_model import InvoiceStatusTypeModel
from app.data.models.rental_status_type_model import RentalStatusTypeModel
from app.data.models.asset_category_type_model import AssetCategoryTypeModel
from app.data.models.asset_manufacturer_type_model import AssetManufacturerTypeModel


class TestLoadTypeModels(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Start Test Type Models")

    @classmethod
    def tearDownClass(cls):
        print('Finished Test Type Models')

    def setUp(self):
        self.session = database_app.get_session()

    def tearDown(self):
        pass

    def select_model_by_code(self, model_list: Any, code: str):
        return [rec for rec in model_list if rec.code == code].pop()

    def test_load_cost_type_model(self):
        models = get_all(db=self.session, model=CostTypeModel)
        self.assertEqual(len(models), 12)
        self.assertEqual(self.select_model_by_code(model_list=models, code="pickup").code, "pickup")
        self.assertEqual(self.select_model_by_code(model_list=models, code="delivery").code, "delivery")
        self.assertEqual(self.select_model_by_code(model_list=models, code="dailycost").code, "dailycost")
        self.assertEqual(self.select_model_by_code(model_list=models, code="weeklycost").code, "weeklycost")
        self.assertEqual(self.select_model_by_code(model_list=models, code="monthlycost").code, "monthlycost")
        self.assertEqual(self.select_model_by_code(model_list=models, code="frequency").code, "frequency")
        self.assertEqual(self.select_model_by_code(model_list=models, code="dailyfree").code, "dailyfree")
        self.assertEqual(self.select_model_by_code(model_list=models, code="weeklyfree").code, "weeklyfree")
        self.assertEqual(self.select_model_by_code(model_list=models, code="monthlyfree").code, "monthlyfree")
        self.assertEqual(self.select_model_by_code(model_list=models, code="damages").code, "damages")
        self.assertEqual(self.select_model_by_code(model_list=models, code="cleaning").code, "cleaning")
        self.assertEqual(self.select_model_by_code(model_list=models, code="germcleaning").code, "germcleaning")

    def test_load_frequency_type_model(self):
        models = get_all(db=self.session, model=FrequencyTypeModel)
        self.assertEqual(len(models), 4)
        self.assertEqual(self.select_model_by_code(model_list=models, code="hourly").code, "hourly")
        self.assertEqual(self.select_model_by_code(model_list=models, code="daily").code, "daily")
        self.assertEqual(self.select_model_by_code(model_list=models, code="weekly").code, "weekly")
        self.assertEqual(self.select_model_by_code(model_list=models, code="monthly").code, "monthly")

    def test_load_invoice_status_type_model(self):
        models = get_all(db=self.session, model=InvoiceStatusTypeModel)
        self.assertEqual(len(models), 5)
        self.assertEqual(self.select_model_by_code(model_list=models, code="draft").code, "draft")
        self.assertEqual(self.select_model_by_code(model_list=models, code="submitted").code, "submitted")
        self.assertEqual(self.select_model_by_code(model_list=models, code="billed").code, "billed")
        self.assertEqual(self.select_model_by_code(model_list=models, code="paid").code, "paid")
        self.assertEqual(self.select_model_by_code(model_list=models, code="pastdue").code, "pastdue")

    def test_load_rental_status_type_model(self):
        models = get_all(db=self.session, model=RentalStatusTypeModel)
        self.assertEqual(len(models), 5)
        self.assertEqual(self.select_model_by_code(model_list=models, code="ready").code, "ready")
        self.assertEqual(self.select_model_by_code(model_list=models, code="rented").code, "rented")
        self.assertEqual(self.select_model_by_code(model_list=models, code="repair").code, "repair")
        self.assertEqual(self.select_model_by_code(model_list=models, code="cleaning").code, "cleaning")
        self.assertEqual(self.select_model_by_code(model_list=models, code="maintenance").code, "maintenance")

    def test_load_asset_category_type_model(self):
        models = get_all(db=self.session, model=AssetCategoryTypeModel)
        self.assertEqual(len(models), 7)
        self.assertEqual(self.select_model_by_code(model_list=models, code="sport").code, "sport")
        self.assertEqual(self.select_model_by_code(model_list=models, code="esport").code, "esport")
        self.assertEqual(self.select_model_by_code(model_list=models, code="ecar").code, "ecar")
        self.assertEqual(self.select_model_by_code(model_list=models, code="truck").code, "truck")
        self.assertEqual(self.select_model_by_code(model_list=models, code="etruck").code, "etruck")
        self.assertEqual(self.select_model_by_code(model_list=models, code="suv").code, "suv")
        self.assertEqual(self.select_model_by_code(model_list=models, code="esuv").code, "esuv")

    def test_load_asset_manufacturer_type_model(self):
        models = get_all(db=self.session, model=AssetManufacturerTypeModel)
        self.assertEqual(len(models), 7)
        self.assertEqual(self.select_model_by_code(model_list=models, code="chevy").code, "chevy")
        self.assertEqual(self.select_model_by_code(model_list=models, code="ford").code, "ford")
        self.assertEqual(self.select_model_by_code(model_list=models, code="dodge").code, "dodge")
        self.assertEqual(self.select_model_by_code(model_list=models, code="ferrari").code, "ferrari")
        self.assertEqual(self.select_model_by_code(model_list=models, code="lamborghini").code, "lamborghini")
        self.assertEqual(self.select_model_by_code(model_list=models, code="telsa").code, "telsa")
        self.assertEqual(self.select_model_by_code(model_list=models, code="mercedes").code, "mercedes")


if __name__ == '__main__':
    print("run tests from the run_tests file in the main directory")