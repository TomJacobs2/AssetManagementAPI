#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from sqlalchemy import create_engine
from sqlalchemy.ext import declarative
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists

from .database_config import database_config

Base = declarative.declarative_base()

from app.data.models import *


class DatabaseApp:
    def __init__(self, db_uri: str):
        self.database_uri = db_uri
        self.engine = create_engine(self.database_uri, connect_args={"check_same_thread": False})
        session_local = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.session = session_local()
        self.base = Base

    def does_database_exists(self):
        results = database_exists(self.database_uri)
        return results

    def create_database(self):
        if not database_exists(self.database_uri):
            self.engine = create_engine(self.database_uri, connect_args={"check_same_thread": False})
            session_local = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
            self.session = session_local()
            self.base = Base
            create_database(self.database_uri)
            self.base.metadata.create_all(bind=self.engine)
            import app.data.load.load_user_model
            import app.data.load.load_type_models

    def get_session(self):
        return self.session


database_app = DatabaseApp(db_uri=database_config.get_database_uri())
