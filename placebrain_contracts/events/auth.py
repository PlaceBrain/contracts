from typing import Literal
from uuid import UUID

from placebrain_contracts.events.base import BaseEvent


class UserUpdated(BaseEvent):
    event_type: Literal["user.updated"] = "user.updated"
    user_id: UUID
    username: str
    email: str
