#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from sqlalchemy.orm import Session
from typing import TypeVar

from app.data.database_app import database_app, Base
from app.schema.type_schema import TypeCreate
from app.data.commands.type_command import create

db_session = database_app.get_session()
ModelType = TypeVar("ModelType", bound=Base)


def create_type(model: ModelType, code: str, description: str):
    raw_data = {"code": code, "description": description, "retired": False}
    schema = TypeCreate(**raw_data)
    create(db=db_session, model=model, schema_in=schema)


from app.data.models.cost_type_model import CostTypeModel
create_type(model=CostTypeModel, code="pickup", description="Pickup asset from customer")
create_type(model=CostTypeModel, code="delivery", description="Delivered asset to customer")
create_type(model=CostTypeModel, code="dailycost", description="Daily cost of the asset")
create_type(model=CostTypeModel, code="weeklycost", description="Weekly cost of the asset")
create_type(model=CostTypeModel, code="monthlycost", description="Monthly cost of the asset")
create_type(model=CostTypeModel, code="frequency", description="Cost per mile / hour of use")
create_type(model=CostTypeModel, code="dailyfree", description="Amount of free mile / hour cost")
create_type(model=CostTypeModel, code="weeklyfree", description="Amount of free mile / hour cost")
create_type(model=CostTypeModel, code="monthlyfree", description="Amount of free mile / hour cost")
create_type(model=CostTypeModel, code="damages", description="Amount of damages to asset during the rental")
create_type(model=CostTypeModel, code="cleaning", description="Amount for cleaning asset after rental")
create_type(model=CostTypeModel, code="germcleaning", description="Disinfectant cleaning")


from app.data.models.frequency_type_model import FrequencyTypeModel
create_type(model=FrequencyTypeModel, code="hourly", description="Hourly")
create_type(model=FrequencyTypeModel, code="daily", description="Daily")
create_type(model=FrequencyTypeModel, code="weekly", description="Weekly")
create_type(model=FrequencyTypeModel, code="monthly", description="Monthly")


from app.data.models.invoice_status_type_model import InvoiceStatusTypeModel
create_type(model=InvoiceStatusTypeModel, code="draft", description="Draft")
create_type(model=InvoiceStatusTypeModel, code="submitted", description="Submitted")
create_type(model=InvoiceStatusTypeModel, code="billed", description="Billed")
create_type(model=InvoiceStatusTypeModel, code="paid", description="Paid")
create_type(model=InvoiceStatusTypeModel, code="pastdue", description="Past Due")


from app.data.models.rental_status_type_model import RentalStatusTypeModel
create_type(model=RentalStatusTypeModel, code="ready", description="Ready to be rented")
create_type(model=RentalStatusTypeModel, code="rented", description="Currently rented")
create_type(model=RentalStatusTypeModel, code="repair", description="Out for repair of damages")
create_type(model=RentalStatusTypeModel, code="cleaning", description="Being clean")
create_type(model=RentalStatusTypeModel, code="maintenance", description="Out for normal maintenance")

