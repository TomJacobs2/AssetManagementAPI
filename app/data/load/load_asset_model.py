#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from app.data.database_app import database_app
from app.schema.asset_schema import AssetCreate
from app.data.commands.asset_command import asset_cmd
from app.data.commands.type_command import get_type_by_code
from app.data.models.asset_manufacturer_type_model import AssetManufacturerTypeModel
from app.data.models.asset_category_type_model import AssetCategoryTypeModel


sport_car_id = get_type_by_code(db=database_app.get_session(), model=AssetCategoryTypeModel, code="sport").id
esport_car_id = get_type_by_code(db=database_app.get_session(), model=AssetCategoryTypeModel, code="esport").id
truck_id = get_type_by_code(db=database_app.get_session(), model=AssetCategoryTypeModel, code="truck").id

ferrari_id = get_type_by_code(db=database_app.get_session(), model=AssetManufacturerTypeModel, code="ferrari").id
lamborghini_id = get_type_by_code(db=database_app.get_session(), model=AssetManufacturerTypeModel, code="lamborghini").id
ford_id = get_type_by_code(db=database_app.get_session(), model=AssetManufacturerTypeModel, code="ford").id
telsa_id = get_type_by_code(db=database_app.get_session(), model=AssetManufacturerTypeModel, code="telsa").id


raw_data = {"asset_tag": "FE8122021001", "description": "Ferrari 812 Superfast", "mileage": 4445,
            "model_year": "2021", "created_by": 1, "updated_by": 1, "color": "Rosso Fiorando",
            "asset_category_id": sport_car_id, "asset_manufacturer_id": ferrari_id}
schema = AssetCreate(**raw_data)
asset_cmd.create(db=database_app.get_session(), schema_in=schema)

raw_data = {"asset_tag": "FE8122022001", "description": "Ferrari 812 Superfast", "mileage": 1345,
            "model_year": "2022", "created_by": 1, "updated_by": 1, "color": "Rosso 70 Anni",
            "asset_category_id": sport_car_id, "asset_manufacturer_id": ferrari_id}
schema = AssetCreate(**raw_data)
asset_cmd.create(db=database_app.get_session(), schema_in=schema)

raw_data = {"asset_tag": "FE8122022002", "description": "Ferrari 812 GTS", "mileage": 2962,
            "model_year": "2022", "created_by": 1, "updated_by": 1, "color": "Blu Swaters",
            "asset_category_id": sport_car_id, "asset_manufacturer_id": ferrari_id}
schema = AssetCreate(**raw_data)
asset_cmd.create(db=database_app.get_session(), schema_in=schema)

raw_data = {"asset_tag": "FEF82022002", "description": "Ferrari F8 Spider", "mileage": 1678,
            "model_year": "2022", "created_by": 1, "updated_by": 1, "color": "Giallo Modena",
            "asset_category_id": sport_car_id, "asset_manufacturer_id": ferrari_id}
schema = AssetCreate(**raw_data)
asset_cmd.create(db=database_app.get_session(), schema_in=schema)

raw_data = {"asset_tag": "LAEVOS2022001", "description": "Huracan Evo Spyder", "mileage": 7325,
            "model_year": "2022", "created_by": 1, "updated_by": 1, "color": "Verde Turbine",
            "asset_category_id": sport_car_id, "asset_manufacturer_id": lamborghini_id}
schema = AssetCreate(**raw_data)
asset_cmd.create(db=database_app.get_session(), schema_in=schema)

raw_data = {"asset_tag": "LAEVOS2022002", "description": "Huracan Evo Spyder", "mileage": 7325,
            "model_year": "2022", "created_by": 1, "updated_by": 1, "color": "Arancio Anthaeus",
            "asset_category_id": sport_car_id, "asset_manufacturer_id": lamborghini_id}
schema = AssetCreate(**raw_data)
asset_cmd.create(db=database_app.get_session(), schema_in=schema)

raw_data = {"asset_tag": "LAAVENT2022001", "description": "Aventador LP 780-4 Ultimae", "mileage": 655,
            "model_year": "2022", "created_by": 1, "updated_by": 1, "color": "Blu Nethuns",
            "asset_category_id": sport_car_id, "asset_manufacturer_id": lamborghini_id}
schema = AssetCreate(**raw_data)
asset_cmd.create(db=database_app.get_session(), schema_in=schema)

raw_data = {"asset_tag": "FDF1502022001", "description": "F150", "mileage": 24355,
            "model_year": "2022", "created_by": 1, "updated_by": 1, "color": "White",
            "asset_category_id": truck_id, "asset_manufacturer_id": ford_id}
schema = AssetCreate(**raw_data)
asset_cmd.create(db=database_app.get_session(), schema_in=schema)

raw_data = {"asset_tag": "FDF1502022002", "description": "F150", "mileage": 17644,
            "model_year": "2022", "created_by": 1, "updated_by": 1, "color": "White",
            "asset_category_id": truck_id, "asset_manufacturer_id": ford_id}
schema = AssetCreate(**raw_data)
asset_cmd.create(db=database_app.get_session(), schema_in=schema)

raw_data = {"asset_tag": "FDF1502021001", "description": "F150", "mileage": 41465,
            "model_year": "2021", "created_by": 1, "updated_by": 1, "color": "Red",
            "asset_category_id": truck_id, "asset_manufacturer_id": ford_id}
schema = AssetCreate(**raw_data)
asset_cmd.create(db=database_app.get_session(), schema_in=schema)

raw_data = {"asset_tag": "TEMSP2022001", "description": "Model S Plaid", "mileage": 1359,
            "model_year": "2022", "created_by": 1, "updated_by": 1, "color": "Midnight Silver Metallic",
            "asset_category_id": esport_car_id, "asset_manufacturer_id": telsa_id}
schema = AssetCreate(**raw_data)
asset_cmd.create(db=database_app.get_session(), schema_in=schema)

raw_data = {"asset_tag": "TEMSP2022002", "description": "Model S Plaid", "mileage": 835,
            "model_year": "2022", "created_by": 1, "updated_by": 1, "color": "Deep Blue Metallic",
            "asset_category_id": esport_car_id, "asset_manufacturer_id": telsa_id}
schema = AssetCreate(**raw_data)
asset_cmd.create(db=database_app.get_session(), schema_in=schema)
