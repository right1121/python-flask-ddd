from abc import ABCMeta, abstractmethod
from Domain.Models.User.user import User
from app.Domain.Models.User.user_id import UserId
from app.Domain.Models.User.user_name import UserName


class IUserRepository(metaclass=ABCMeta):
    @abstractmethod
    def findByid(self, user_id: UserId) -> User:
        pass

    @abstractmethod
    def findByName(self, user_name: UserName) -> User:
        pass

    @abstractmethod
    def save(self, user: User) -> None:
        pass

    @abstractmethod
    def delete(self, user: User) -> None:
        pass
