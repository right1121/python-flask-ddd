from typing import Optional
from Domain.Models.User.user import User
from Domain.Services.user import UserService
from Domain.Models.User.IUserRepository import IUserRepository
from Domain.Models.User.user_name import UserName
from app.Application.User.UserData import UserData
from app.Domain.Models.User.user_id import UserId
from app.EF.Users.EFUserRepository import UserRepository


class UserApplicationService:
    def __init__(self, userRepository: IUserRepository, userService: UserService):
        self.userRepository = userRepository
        self.userService = userService

    def createUser(self, user_name: str) -> None:
        user = User(UserName(user_name))

        if self.userService.exists(user):
            raise Exception(f'{user_name}はすでに存在しています。')

        self.userRepository.save(user)

    def Get(self, userId: str) -> Optional[UserData]:
        targetId = UserId(userId)
        user = self.userRepository.findByid(targetId)

        if user is None:
            return None

        userData = UserData(user)
        return userData

    def Update(self, userId: str, name: str) -> None:
        targetId = UserId(userId)
        user = self.userRepository.findByid(targetId)

        if user is None:
            raise NotFoundUser
        
        user.changeName(name)

    def delete(self, command: UserDeleteCommand) -> None:
        targetId = UserId(command._id)
        user = self.userRepository.findByid(targetId)

        if user is None:
            raise NotFoundUser

        self.userRepository.delete(user)


class NotFoundUser(Exception):
    pass
