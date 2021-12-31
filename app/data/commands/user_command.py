#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from sqlalchemy.orm import Session

from .command_base import CommandBase
from app.data.models.user_model import UserModel
from app.schema.user_schema import UserCreate, UserUpdate


class UserCommand(CommandBase[UserModel, UserCreate, UserUpdate]):
    ...

    def get_user_by_credentials(self, db: Session, username: str, password: str):
        return db.query(self.model)\
            .filter(self.model.login_name == username, self.model.login_password == password)\
            .first()

    def get_user_by_email(self, db: Session, email: str):
        return db.query(self.model).filter(self.model.email == email).first()


user_cmd = UserCommand(UserModel)
