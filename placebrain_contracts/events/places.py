from typing import Literal
from uuid import UUID

from placebrain_contracts.events.base import BaseEvent


class MemberAdded(BaseEvent):
    event_type: Literal["member.added"] = "member.added"
    place_id: UUID
    user_id: UUID
    role: str


class MemberRemoved(BaseEvent):
    event_type: Literal["member.removed"] = "member.removed"
    place_id: UUID
    user_id: UUID


class MemberRoleChanged(BaseEvent):
    event_type: Literal["member.role_changed"] = "member.role_changed"
    place_id: UUID
    user_id: UUID
    role: str


class PlaceDeleted(BaseEvent):
    event_type: Literal["place.deleted"] = "place.deleted"
    place_id: UUID
    member_ids: list[UUID]
