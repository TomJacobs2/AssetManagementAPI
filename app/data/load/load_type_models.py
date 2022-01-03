#  Copyright (c) Thomas Jacobs. All Rights Reserved.

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

from app.data.models.asset_category_type_model import AssetCategoryTypeModel
create_type(model=AssetCategoryTypeModel, code="sport", description="Sport Car")
create_type(model=AssetCategoryTypeModel, code="esport", description="Electric Sport Car")
create_type(model=AssetCategoryTypeModel, code="ecar", description="Electric Car")
create_type(model=AssetCategoryTypeModel, code="truck", description="Pickup Truck")
create_type(model=AssetCategoryTypeModel, code="etruck", description="Electric Pickup Truck")
create_type(model=AssetCategoryTypeModel, code="suv", description="SUV")
create_type(model=AssetCategoryTypeModel, code="esuv", description="Electric SUV")

from app.data.models.asset_manufacturer_type_model import AssetManufacturerTypeModel
create_type(model=AssetManufacturerTypeModel, code="chevy", description="Chevy")
create_type(model=AssetManufacturerTypeModel, code="ford", description="Ford")
create_type(model=AssetManufacturerTypeModel, code="dodge", description="Dodge")
create_type(model=AssetManufacturerTypeModel, code="ferrari", description="Ferrari")
create_type(model=AssetManufacturerTypeModel, code="lamborghini", description="Lamborghini")
create_type(model=AssetManufacturerTypeModel, code="telsa", description="Telsa")
create_type(model=AssetManufacturerTypeModel, code="mercedes", description="Mercedes")

from app.data.models.event_type_model import EventTypeModel
create_type(model=EventTypeModel, code="power_on", description="Power On")
create_type(model=EventTypeModel, code="power_off", description="Power Off")
create_type(model=EventTypeModel, code="over_heating", description="Over Heating")
create_type(model=EventTypeModel, code="tire_pressure", description="Tire Pressure")
create_type(model=EventTypeModel, code="check_engine", description="Check Engine")
create_type(model=EventTypeModel, code="airbags_deployed", description="Airbags Deployed")
create_type(model=EventTypeModel, code="maintenance", description="Maintenance Required")
create_type(model=EventTypeModel, code="speed", description="Asset Speed")
create_type(model=EventTypeModel, code="sudden_stop", description="Sudden Stop")
create_type(model=EventTypeModel, code="rollover", description="Asset Rolled Over")
create_type(model=EventTypeModel, code="process_error", description="Process Error")
create_type(model=EventTypeModel, code="send_email", description="Send Email")
create_type(model=EventTypeModel, code="send_text", description="Send Text")
create_type(model=EventTypeModel, code="send_chat", description="Send Chat")
create_type(model=EventTypeModel, code="asset_pickup", description="Customer Picked Up")
create_type(model=EventTypeModel, code="asset_returned", description="Customer Returned")
create_type(model=EventTypeModel, code="delivery_charge", description="Delivery Charge")
create_type(model=EventTypeModel, code="pickup_charge", description="Pickup Charge")
create_type(model=EventTypeModel, code="location", description="Location")
create_type(model=EventTypeModel, code="battery_disconnected", description="Battery Disconnected")

from app.data.models.event_subtype_model import EventSubTypeModel
create_type(model=EventSubTypeModel, code="asset", description="Asset")
create_type(model=EventSubTypeModel, code="user", description="User")
create_type(model=EventSubTypeModel, code="account", description="Account")

from app.data.models.attribute_type_model import AttributeTypeModel
create_type(model=AttributeTypeModel, code="power", description="Power")
create_type(model=AttributeTypeModel, code="speed", description="Speed")
create_type(model=AttributeTypeModel, code="location", description="Location")
create_type(model=AttributeTypeModel, code="lights", description="Lights")
create_type(model=AttributeTypeModel, code="doors", description="Doors")
create_type(model=AttributeTypeModel, code="hood", description="Hood")
create_type(model=AttributeTypeModel, code="trunk", description="Trunk")

