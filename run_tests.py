#  Copyright (c) Thomas Jacobs. All Rights Reserved.
import os
import unittest

from app.data.database_config import database_config
database_config.set_database_uri(db_uri="sqlite:///./asset_test.db")


#if os.path.isfile("./asset_test.db"):
#    os.remove("./asset_test.db")

from app.data.database_app import database_app

data_app = database_app
if not data_app.does_database_exists():
    data_app.create_database()


#run the data layer unit tests
data_layer_loader = unittest.TestLoader()
data_layer_test_dir = './app/data/tests'
data_layer_test_files = data_layer_loader.discover(data_layer_test_dir)
data_layer_runner = unittest.TextTestRunner()
data_layer_runner.run(data_layer_test_files)
