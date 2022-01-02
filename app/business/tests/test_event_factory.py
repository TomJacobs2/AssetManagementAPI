#  Copyright (c) Thomas Jacobs. All Rights Reserved.

import unittest

from app.schema.event_schema import EventRequest
from app.business.pubsub.event_factory import event_factory
from app.business.events.airbags_deployed_event import AirbagsDeployedEvent
from app.business.events.asset_pickup_event import AssetPickupEvent
from app.business.events.asset_returned_event import AssetReturnedEvent
from app.business.events.check_engine_event import CheckEngineEvent
from app.business.events.delivery_charge_event import DeliveryChargeEvent
from app.business.events.maintenance_event import MaintenanceEvent
from app.business.events.over_heating_event import OverHeatingEvent
from app.business.events.pickup_charge_event import PickupChargeEvent
from app.business.events.power_off_event import PowerOffEvent
from app.business.events.power_on_event import PowerOnEvent
from app.business.events.process_error_event import ProcessErrorEvent
from app.business.events.rollover_event import RolloverEvent
from app.business.events.send_chat_event import SendChatEvent
from app.business.events.send_email_event import SendEmailEvent
from app.business.events.send_text_event import SendTextEvent
from app.business.events.speed_event import SpeedEvent
from app.business.events.sudden_stop_event import SuddenStopEvent
from app.business.events.tire_pressure_event import TirePressureEvent


class TestEventFactory(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Start Test Event Factory Command")

    @classmethod
    def tearDownClass(cls):
        print('Finished Test Event Factory Command')

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_event_type_count(self):
        self.assertEqual(len(event_factory.event_types), 18)

    def test_factory_return_airbag_deployed(self):
        raw_data = {"asset_tag": "FE8122022001", "event_type_code": "airbags_deployed"}
        schema = EventRequest(**raw_data)
        type_result = event_factory.get_event_class(event_schema=schema)
        self.assertTrue(isinstance(type_result, AirbagsDeployedEvent))

    def test_factory_return_asset_pickup(self):
        raw_data = {"asset_tag": "FE8122022001", "event_type_code": "asset_pickup"}
        schema = EventRequest(**raw_data)
        type_result = event_factory.get_event_class(event_schema=schema)
        self.assertTrue(isinstance(type_result, AssetPickupEvent))

    def test_factory_return_asset_retuned(self):
        raw_data = {"asset_tag": "FE8122022001", "event_type_code": "asset_returned"}
        schema = EventRequest(**raw_data)
        type_result = event_factory.get_event_class(event_schema=schema)
        self.assertTrue(isinstance(type_result, AssetReturnedEvent))

    def test_factory_return_check_engine(self):
        raw_data = {"asset_tag": "FE8122022001", "event_type_code": "check_engine"}
        schema = EventRequest(**raw_data)
        type_result = event_factory.get_event_class(event_schema=schema)
        self.assertTrue(isinstance(type_result, CheckEngineEvent))

    def test_factory_return_delivery_charge(self):
        raw_data = {"asset_tag": "FE8122022001", "event_type_code": "delivery_charge"}
        schema = EventRequest(**raw_data)
        type_result = event_factory.get_event_class(event_schema=schema)
        self.assertTrue(isinstance(type_result, DeliveryChargeEvent))

    def test_factory_return_maintenance(self):
        raw_data = {"asset_tag": "FE8122022001", "event_type_code": "maintenance"}
        schema = EventRequest(**raw_data)
        type_result = event_factory.get_event_class(event_schema=schema)
        self.assertTrue(isinstance(type_result, MaintenanceEvent))

    def test_factory_return_over_heating(self):
        raw_data = {"asset_tag": "FE8122022001", "event_type_code": "over_heating"}
        schema = EventRequest(**raw_data)
        type_result = event_factory.get_event_class(event_schema=schema)
        self.assertTrue(isinstance(type_result, OverHeatingEvent))

    def test_factory_return_pickup_charge(self):
        raw_data = {"asset_tag": "FE8122022001", "event_type_code": "pickup_charge"}
        schema = EventRequest(**raw_data)
        type_result = event_factory.get_event_class(event_schema=schema)
        self.assertTrue(isinstance(type_result, PickupChargeEvent))

    def test_factory_return_power_off(self):
        raw_data = {"asset_tag": "FE8122022001", "event_type_code": "power_off"}
        schema = EventRequest(**raw_data)
        type_result = event_factory.get_event_class(event_schema=schema)
        self.assertTrue(isinstance(type_result, PowerOffEvent))

    def test_factory_return_power_on(self):
        raw_data = {"asset_tag": "FE8122022001", "event_type_code": "power_on"}
        schema = EventRequest(**raw_data)
        type_result = event_factory.get_event_class(event_schema=schema)
        self.assertTrue(isinstance(type_result, PowerOnEvent))

    def test_factory_return_process_error(self):
        raw_data = {"asset_tag": "FE8122022001", "event_type_code": "process_error"}
        schema = EventRequest(**raw_data)
        type_result = event_factory.get_event_class(event_schema=schema)
        self.assertTrue(isinstance(type_result, ProcessErrorEvent))

    def test_factory_return_rollover(self):
        raw_data = {"asset_tag": "FE8122022001", "event_type_code": "rollover"}
        schema = EventRequest(**raw_data)
        type_result = event_factory.get_event_class(event_schema=schema)
        self.assertTrue(isinstance(type_result, RolloverEvent))

    def test_factory_return_send_chat(self):
        raw_data = {"asset_tag": "FE8122022001", "event_type_code": "send_chat"}
        schema = EventRequest(**raw_data)
        type_result = event_factory.get_event_class(event_schema=schema)
        self.assertTrue(isinstance(type_result, SendChatEvent))

    def test_factory_return_send_email(self):
        raw_data = {"asset_tag": "FE8122022001", "event_type_code": "send_email"}
        schema = EventRequest(**raw_data)
        type_result = event_factory.get_event_class(event_schema=schema)
        self.assertTrue(isinstance(type_result, SendEmailEvent))

    def test_factory_return_send_text(self):
        raw_data = {"asset_tag": "FE8122022001", "event_type_code": "send_text"}
        schema = EventRequest(**raw_data)
        type_result = event_factory.get_event_class(event_schema=schema)
        self.assertTrue(isinstance(type_result, SendTextEvent))

    def test_factory_return_speed(self):
        raw_data = {"asset_tag": "FE8122022001", "event_type_code": "speed"}
        schema = EventRequest(**raw_data)
        type_result = event_factory.get_event_class(event_schema=schema)
        self.assertTrue(isinstance(type_result, SpeedEvent))

    def test_factory_return_sudden_stop(self):
        raw_data = {"asset_tag": "FE8122022001", "event_type_code": "sudden_stop"}
        schema = EventRequest(**raw_data)
        type_result = event_factory.get_event_class(event_schema=schema)
        self.assertTrue(isinstance(type_result, SuddenStopEvent))

    def test_factory_return_tire_pressure(self):
        raw_data = {"asset_tag": "FE8122022001", "event_type_code": "tire_pressure"}
        schema = EventRequest(**raw_data)
        type_result = event_factory.get_event_class(event_schema=schema)
        self.assertTrue(isinstance(type_result, TirePressureEvent))
