#  Copyright (c) Thomas Jacobs. All Rights Reserved.

import uvicorn

from app.data.database_app import database_app
from app.api.fast_api_app import fast_api_app

data_app = database_app
if not data_app.does_database_exists():
    data_app.create_database()

api_app = fast_api_app.get_app()

uvicorn.run(api_app, host="127.0.0.1", port=5000)
