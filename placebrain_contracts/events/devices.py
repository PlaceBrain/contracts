from typing import Literal
from uuid import UUID

from placebrain_contracts.events.base import BaseEvent


class DeviceDeleted(BaseEvent):
    event_type: Literal["device.deleted"] = "device.deleted"
    device_id: UUID
    place_id: UUID


class DevicesBulkDeleted(BaseEvent):
    event_type: Literal["devices.bulk_deleted"] = "devices.bulk_deleted"
    device_ids: list[UUID]


class ThresholdCreated(BaseEvent):
    event_type: Literal["threshold.created"] = "threshold.created"
    sensor_id: UUID
    threshold_id: UUID
    threshold_type: Literal["min", "max"]
    value: float
    severity: Literal["warning", "critical"]


class ThresholdUpdated(BaseEvent):
    event_type: Literal["threshold.updated"] = "threshold.updated"
    sensor_id: UUID
    threshold_id: UUID
    threshold_type: Literal["min", "max"]
    value: float
    severity: Literal["warning", "critical"]


class ThresholdDeleted(BaseEvent):
    event_type: Literal["threshold.deleted"] = "threshold.deleted"
    sensor_id: UUID
    threshold_id: UUID
