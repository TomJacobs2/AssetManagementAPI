#  Copyright (c) Thomas Jacobs. All Rights Reserved.


class DatabaseConfig:
    def __init__(self):
        self.database_uri = "sqlite:///./asset.db"

    def get_database_uri(self):
        return self.database_uri

    def set_database_uri(self, db_uri: str):
        self.database_uri = db_uri


database_config = DatabaseConfig()
