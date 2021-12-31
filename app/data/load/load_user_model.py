#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from typing import TypeVar

from app.data.database_app import database_app, Base
from app.schema.user_schema import UserCreate
from app.data.commands.user_command import user_cmd
from app.data.models.role_model import RoleModel
from app.data.commands.role_permission_command import get_role_permission_by_code

db_session = database_app.get_session()
ModelType = TypeVar("ModelType", bound=Base)

superuser_role_id = get_role_permission_by_code(db=database_app.get_session(), model=RoleModel, code="superuser").id
adminuser_role_id = get_role_permission_by_code(db=database_app.get_session(), model=RoleModel, code="adminuser").id
account_manager_role_id = get_role_permission_by_code(db=database_app.get_session(), model=RoleModel, code="accountmanager").id
asset_manager_role_id = get_role_permission_by_code(db=database_app.get_session(), model=RoleModel, code="assetmanager").id
acctadmin_role_id = get_role_permission_by_code(db=database_app.get_session(), model=RoleModel, code="acctadmin").id
acctuser_role_id = get_role_permission_by_code(db=database_app.get_session(), model=RoleModel, code="acctuser").id


raw_data = {"first_name": "Super", "last_name": "User", "email": "super.user@newassetcompany.com",
            "cell_phone": 5739991234, "external_user": 0, "role_id": superuser_role_id,
            "login_name": "super.user", "login_password": "SpiderMonkeys2"}
schema = UserCreate(**raw_data)
user_cmd.create(db=database_app.get_session(), schema_in=schema)

raw_data = {"first_name": "Thomas", "last_name": "Jacobs", "email": "thomas.jacobs@newassetcompany.com",
            "cell_phone": 5739991235, "external_user": 0, "role_id": adminuser_role_id,
            "login_name": "thomas.jacobs", "login_password": "Little13Monkeys"}
schema = UserCreate(**raw_data)
user_cmd.create(db=database_app.get_session(), schema_in=schema)

raw_data = {"first_name": "Jonney", "last_name": "Applegate", "email": "jonney.applegate@newassetcompany.com",
            "cell_phone": 5739991236, "external_user": 0, "role_id": account_manager_role_id,
            "login_name": "jonney.applegate", "login_password": "Test2Jonney"}
schema = UserCreate(**raw_data)
user_cmd.create(db=database_app.get_session(), schema_in=schema)

raw_data = {"first_name": "Drake", "last_name": "Jones", "email": "drake.jones@newassetcompany.com",
            "cell_phone": 5739991237, "external_user": 0, "role_id": asset_manager_role_id,
            "login_name": "drake.jones", "login_password": "FlyingDrakes4"}
schema = UserCreate(**raw_data)
user_cmd.create(db=database_app.get_session(), schema_in=schema)

raw_data = {"first_name": "Speed", "last_name": "Racer", "email": "speed_racer31@@newspiderracing.com",
            "cell_phone": 5739993331, "external_user": 1, "role_id": acctadmin_role_id,
            "login_name": "speed.racer31", "login_password": "TooFast4You"}
schema = UserCreate(**raw_data)
user_cmd.create(db=database_app.get_session(), schema_in=schema)

raw_data = {"first_name": "Niki", "last_name": "Telsa", "email": "niki.telsa@@newspiderracing.com",
            "cell_phone": 5739993332, "external_user": 1, "role_id": acctuser_role_id,
            "login_name": "niki.telsa", "login_password": "No1Faster"}
schema = UserCreate(**raw_data)
user_cmd.create(db=database_app.get_session(), schema_in=schema)

raw_data = {"first_name": "Mike", "last_name": "Telason", "email": "mike.telason@@gorillaproracing.com",
            "cell_phone": 5739993332, "external_user": 1, "role_id": acctadmin_role_id,
            "login_name": "mike.telason", "login_password": "Gorilla4Pro"}
schema = UserCreate(**raw_data)
user_cmd.create(db=database_app.get_session(), schema_in=schema)