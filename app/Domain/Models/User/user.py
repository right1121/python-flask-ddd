from __future__ import annotations
import uuid

from .user_id import UserId
from .user_name import UserName


class User:
    def __init__(self, name: UserName, _id: UserId) -> None:
        if name is None:
            raise ValueError
        self.name: UserName = name
        self.id: UserId = _id

    @classmethod
    def newUser(cls, name: UserName) -> User:
        if name is None:
            raise ValueError
        _id: UserId = UserId(str(uuid.uuid4()))
        return cls(name, _id)

    def changeName(self, name: UserName) -> None:
        self.name = name
