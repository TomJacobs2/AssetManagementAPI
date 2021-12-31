#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from typing import TypeVar

from app.data.database_app import database_app, Base
from app.schema.user_schema import UserCreate
from app.data.commands.user_command import user_cmd

db_session = database_app.get_session()
ModelType = TypeVar("ModelType", bound=Base)


raw_data = {"first_name": "Super", "last_name": "User", "email": "super.user@newassetcompany.com",
            "cell_phone": 5739991234, "external_user": 0,
            "login_name": "super.user", "login_password": "SpiderMonkeys"}
schema = UserCreate(**raw_data)
user_cmd.create(db=database_app.get_session(), schema_in=schema)

raw_data = {"first_name": "Thomas", "last_name": "Jacobs", "email": "thomas.jacobs@newassetcompany.com",
            "cell_phone": 5739991235, "external_user": 0,
            "login_name": "thomas.jacobs", "login_password": "Little13Monkeys"}
schema = UserCreate(**raw_data)
user_cmd.create(db=database_app.get_session(), schema_in=schema)

raw_data = {"first_name": "Jonney", "last_name": "Applegate", "email": "jonney.applegate@newassetcompany.com",
            "cell_phone": 5739991236, "external_user": 0,
            "login_name": "jonney.applegate", "login_password": "Test2Jonney"}
schema = UserCreate(**raw_data)
user_cmd.create(db=database_app.get_session(), schema_in=schema)

raw_data = {"first_name": "Speed", "last_name": "Racer", "email": "speed_racer31@newracingcompany.com",
            "cell_phone": 5739993331, "external_user": 1,
            "login_name": "speed.racer31", "login_password": "TooFast4You"}
schema = UserCreate(**raw_data)
user_cmd.create(db=database_app.get_session(), schema_in=schema)

raw_data = {"first_name": "Niki", "last_name": "Telsa", "email": "niki.telsa@newracingcompany.com",
            "cell_phone": 5739993332, "external_user": 1,
            "login_name": "niki.telsa", "login_password": "No1Faster"}
schema = UserCreate(**raw_data)
user_cmd.create(db=database_app.get_session(), schema_in=schema)
