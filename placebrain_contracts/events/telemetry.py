import json
from datetime import datetime
from typing import Any

from pydantic import BaseModel, field_validator


class TelemetryPayload(BaseModel):
    ts: datetime | None = None
    values: dict[str, float]


class EmqxTelemetryMessage(BaseModel):
    """Message format from EMQX Kafka bridge for telemetry.readings topic."""

    topic: str
    payload: TelemetryPayload

    @field_validator("payload", mode="before")
    @classmethod
    def parse_payload(cls, v: Any) -> dict[str, Any]:
        if isinstance(v, str):
            return json.loads(v)
        return v

    def extract_ids(self) -> tuple[str, str]:
        """Extract (place_id, device_id) from MQTT topic.

        Topic format: placebrain/{place_id}/devices/{device_id}/telemetry
        """
        parts = self.topic.split("/")
        return parts[1], parts[3]


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
