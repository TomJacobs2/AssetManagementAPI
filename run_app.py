#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from app.data.database_app import database_app


data_app = database_app
if not data_app.does_database_exists():
    data_app.create_database()
