# contracts

> The shared wire-format for PlaceBrain: gRPC proto files + Pydantic event schemas, published to PyPI as `placebrain-contracts`.

[![License: Apache 2.0](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](./LICENSE)
![PyPI](https://img.shields.io/pypi/v/placebrain-contracts.svg)
![Python 3.14](https://img.shields.io/badge/python-3.14-blue.svg)

Every PlaceBrain service depends on this package. It contains:

- The `.proto` files for the four gRPC services (`auth`, `places`, `devices`, `collector`).
- Generated Python stubs (`*_pb2.py`, `*_pb2_grpc.py`, `*.pyi`) produced by CI.
- Pydantic event models for Kafka and MQTT payloads.
- Centralised topic/constant names so no service hardcodes a string.

## Role in PlaceBrain

PlaceBrain is an open-source IoT platform for smart buildings. See the [organization profile](https://github.com/PlaceBrain) for the full architecture.

- Consumed by [auth](https://github.com/PlaceBrain/auth), [places](https://github.com/PlaceBrain/places), [devices](https://github.com/PlaceBrain/devices), [gateway](https://github.com/PlaceBrain/gateway), [collector](https://github.com/PlaceBrain/collector).
- Never hand-generate protobuf code — the [CI/CD workflow](./.github/workflows/publish.yaml) does the full build: generates stubs, fixes up imports, builds an sdist/wheel and publishes to PyPI on every push to `main`.

## What's inside

```
proto/
├── auth.proto           gRPC: Register, Login, RefreshTokens, OTP, ValidateToken, ...
├── places.proto         gRPC: PlacesService (CRUD + members + role constants)
├── devices.proto        gRPC: DevicesService (Device/Sensor/Actuator/Threshold/Command + MQTT auth)
└── collector.proto      gRPC: internal readings methods

placebrain_contracts/
├── auth_pb2.py / auth_pb2_grpc.py            (generated)
├── places_pb2.py / places_pb2_grpc.py        (generated)
├── devices_pb2.py / devices_pb2_grpc.py      (generated)
└── events/
    ├── base.py          BaseEvent
    ├── places.py        MemberAdded, MemberRemoved, MemberRoleChanged, PlaceDeleted
    ├── devices.py       DeviceDeleted, DevicesBulkDeleted, ThresholdCreated, ThresholdDeleted
    ├── telemetry.py     EmqxTelemetryMessage, EmqxStatusMessage, TelemetryPayload
    └── topics.py        TOPIC_* constants — single source of truth for Kafka topic names
```

## Usage

```python
# gRPC: import the whole module, not individual classes.
from placebrain_contracts import auth_pb2 as auth_pb
request = auth_pb.LoginRequest(email=..., password=...)

# Kafka events: pass Pydantic models straight to the broker.
from placebrain_contracts.events import MemberAdded, TOPIC_MEMBER_ADDED

await broker.publish(
    MemberAdded(place_id=place.id, user_id=user_id, role=role.value),
    topic=TOPIC_MEMBER_ADDED,
    key=f"{place.id}:{user_id}".encode(),
)
```

## How a contract change gets shipped

Automated end-to-end, no manual build/publish:

1. Edit `proto/*.proto` or Pydantic event models.
2. Bump `version` in `pyproject.toml`.
3. Commit and push to `main`.
4. CI runs `publish.yaml`: generates stubs, fixes imports, builds with `uv build`, publishes to PyPI with `uv publish`.
5. In consuming services, bump the version in `pyproject.toml` and `uv lock --upgrade-package placebrain-contracts`. Clear the uv cache first (`uv cache clean placebrain-contracts`) if you just published a new version moments ago.

## License

Apache License 2.0 — see [LICENSE](./LICENSE).
