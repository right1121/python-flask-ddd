class FullName:
    __first_name: str
    __last_name: str

    def __init__(self, first_name: str, last_name: str) -> None:
        self.__first_name = first_name
        self.__last_name = last_name

    @property
    def fistrName(self) -> str:
        return self.__first_name

    @property
    def lastName(self) -> str:
        return self.__last_name

    def __eq__(self, value):
        return super().__eq__(value)
