#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from sqlalchemy.orm import Session

from .command_base import CommandBase
from app.data.models.account_model import AccountModel
from app.schema.account_schema import AccountCreate, AccountUpdate


class AccountCommand(CommandBase[AccountModel, AccountCreate, AccountUpdate]):
    ...

    def get_account_by_name(self, db: Session, account_name: str):
        return db.query(self.model).filter(self.model.account_name == account_name).first()

    def get_account_manager_accounts(self, db: Session, account_manager_id: int):
        return db.query(self.model).filter(self.model.account_manager_id == account_manager_id).all()


account_cmd = AccountCommand(AccountModel)
