from typing import Literal
from uuid import UUID

from placebrain_contracts.events.base import BaseEvent


class MemberAdded(BaseEvent):
    place_id: UUID
    user_id: UUID
    role: Literal["owner", "admin", "viewer"]


class MemberRemoved(BaseEvent):
    place_id: UUID
    user_id: UUID


class MemberRoleChanged(BaseEvent):
    place_id: UUID
    user_id: UUID
    role: Literal["owner", "admin", "viewer"]


class PlaceDeleted(BaseEvent):
    place_id: UUID
    member_ids: list[UUID]
