from __future__ import annotations
from typing import Optional, Any

from .user_id import UserId
from .user_name import UserName


class User:
    def __init__(self, id: UserId, name: UserName) -> None:
        self.id = id
        self.name = name

    def __eq__(self, value: Optional[User, Any]):
        if value is None:
            return False
        if type(value) != User:
            return False
        if self is value:
            return True
        return self.id == value.id

        return super().__eq__(value)
