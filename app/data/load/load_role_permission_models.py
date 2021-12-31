#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from typing import TypeVar

from app.data.database_app import database_app, Base
from app.schema.role_permission_schema import RolePermissionCreate
from app.data.commands.role_permission_command import create

db_session = database_app.get_session()
ModelType = TypeVar("ModelType", bound=Base)


def create_role_permission(model: ModelType, code: str, description: str, for_external_user: bool):
    raw_data = {"code": code, "description": description, "for_external_user": for_external_user, "retired": False}
    schema = RolePermissionCreate(**raw_data)
    create(db=db_session, model=model, schema_in=schema)


from app.data.models.role_model import RoleModel
create_role_permission(model=RoleModel, code="superuser", description="Super User", for_external_user=False)
create_role_permission(model=RoleModel, code="adminuser", description="Admin User", for_external_user=False)
create_role_permission(model=RoleModel, code="accountmanager", description="Account Manager", for_external_user=False)
create_role_permission(model=RoleModel, code="assetmanager", description="Asset Manager", for_external_user=False)
create_role_permission(model=RoleModel, code="custservice", description="Customer Service", for_external_user=False)
create_role_permission(model=RoleModel, code="acctadmin", description="Account Admin", for_external_user=True)
create_role_permission(model=RoleModel, code="acctbilling", description="Account Billing User", for_external_user=True)
create_role_permission(model=RoleModel, code="acctuser", description="Account User", for_external_user=True)
