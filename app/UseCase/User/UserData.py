from app.Domain.Models.User.user import User


class UserData:
    def __init__(self, user: User) -> None:
        self.id = user.id.value
        self.name = user.name.value
