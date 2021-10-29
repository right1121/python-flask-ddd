from Domain.Models.User.user import User
from Domain.Models.User.IUserRepository import IUserRepository


class UserService:
    def __init__(self, userRepository: IUserRepository):
        self.userRepository = userRepository

    def exists(self, user: User) -> bool:
        found = self.userRepository.findByName(user.name)
        return found is not None
