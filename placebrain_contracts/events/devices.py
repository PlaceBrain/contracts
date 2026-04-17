from typing import Literal
from uuid import UUID

from placebrain_contracts.events.base import BaseEvent


class DeviceDeleted(BaseEvent):
    device_id: UUID
    place_id: UUID


class DevicesBulkDeleted(BaseEvent):
    device_ids: list[UUID]


class ThresholdCreated(BaseEvent):
    sensor_id: UUID
    device_id: UUID
    key: str
    threshold_id: UUID
    threshold_type: Literal["min", "max"]
    value: float
    severity: Literal["warning", "critical"]


class ThresholdUpdated(BaseEvent):
    sensor_id: UUID
    threshold_id: UUID
    threshold_type: Literal["min", "max"]
    value: float
    severity: Literal["warning", "critical"]


class ThresholdDeleted(BaseEvent):
    sensor_id: UUID
    device_id: UUID
    key: str
    threshold_id: UUID
