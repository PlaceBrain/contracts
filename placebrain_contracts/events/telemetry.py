import json
from datetime import datetime
from typing import Any

from pydantic import BaseModel, field_validator


class TelemetryPayload(BaseModel):
    ts: datetime | None = None
    values: dict[str, float]


class TelemetryReading(BaseModel):
    """Domain event for a telemetry reading published to telemetry.readings."""

    place_id: str
    device_id: str
    payload: TelemetryPayload

    @field_validator("payload", mode="before")
    @classmethod
    def parse_payload(cls, v: Any) -> dict[str, Any]:
        if isinstance(v, str):
            return json.loads(v)
        return v


class DeviceStatusPayload(BaseModel):
    status: str
    device_id: str | None = None


class EmqxStatusMessage(BaseModel):
    """Message format from EMQX Kafka bridge for telemetry.status topic."""

    topic: str
    payload: DeviceStatusPayload

    @field_validator("payload", mode="before")
    @classmethod
    def parse_payload(cls, v: Any) -> dict[str, Any]:
        if isinstance(v, str):
            return json.loads(v)
        return v

    def extract_device_id(self) -> str:
        """Extract device_id from MQTT topic.

        Topic format: placebrain/{place_id}/devices/{device_id}/status
        """
        parts = self.topic.split("/")
        return parts[3]
