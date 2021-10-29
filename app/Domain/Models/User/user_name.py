class UserName:
    def __init__(self, value: str) -> None:
        if value is None:
            raise ValueError

        if len(value) < 3:
            raise ValueError

        self.value = value
