#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from app.data.database_app import database_app
from app.schema.account_schema import AccountCreate
from app.data.commands.account_command import account_cmd
from app.data.commands.user_command import user_cmd

account_manager_id = user_cmd.get_user_by_email(db=database_app.get_session(),
                                                email="jonney.applegate@newassetcompany.com").id
spider_primary_contact_id = user_cmd.get_user_by_email(db=database_app.get_session(),
                                                       email="niki.telsa@@newspiderracing.com").id
gorilla_primary_contact_id = user_cmd.get_user_by_email(db=database_app.get_session(),
                                                        email="mike.telason@@gorillaproracing.com").id


raw_data = {"account_number": "NAC123456", "account_name": "New Spider Racing", "mailing_line_one": "120 Main Street",
            "mailing_city": "Ashland", "mailing_state": "Missouri", "mailing_postal_code": "65010",
            "billing_line_one": "120 Main Street", "billing_city": "Ashland", "billing_state": "Missouri",
            "billing_postal_code": "65010", "business_phone": "573.999.1234",
            "business_email": "support@newspiderracing.com", "created_by": 1, "updated_by": 1,
            "account_manager_id": account_manager_id, "primary_contact_id": spider_primary_contact_id}
schema = AccountCreate(**raw_data)
account_cmd.create(db=database_app.get_session(), schema_in=schema)

raw_data = {"account_number": "NAC654987", "account_name": "Gorilla Pro Racing",
            "mailing_line_one": "2440 Forbis Avenue", "mailing_city": "Deer Park", "mailing_state": "Missouri",
            "mailing_postal_code": "65203", "billing_line_one": "244 Fourth Avenue", "billing_city": "Ashland",
            "billing_state": "Missouri", "billing_postal_code": "65010", "business_phone": "573.999.4321",
            "business_email": "support@gorillaproracing.com", "created_by": 1, "updated_by": 1,
            "account_manager_id": account_manager_id, "primary_contact_id": gorilla_primary_contact_id}
schema = AccountCreate(**raw_data)
account_cmd.create(db=database_app.get_session(), schema_in=schema)
