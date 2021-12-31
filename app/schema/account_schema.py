#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from pydantic import BaseModel
from typing import Sequence, Optional


class AccountBase(BaseModel):
    account_name: str
    mailing_line_one: str
    mailing_line_two: Optional[str] = None
    mailing_city: str
    mailing_state: str
    mailing_postal_code: str
    billing_line_one: str
    billing_line_two: Optional[str] = None
    billing_city: str
    billing_state: str
    billing_postal_code: str
    business_phone: str
    business_email: str
    primary_contact_id: int
    account_manager_id: int


class AccountCreate(AccountBase):
    created_by: int
    updated_by: int


class AccountUpdate(AccountBase):
    id: int
    created_by: int
    updated_by: int


class AccountInDBBase(AccountBase):
    id: int
    create_date: str
    update_date: str

    class Config:
        orm_mode = True


class Account(AccountInDBBase):
    pass


class AccountSearchResults(BaseModel):
    results: Sequence[Account]
