from __future__ import annotations


class Money:
    def __init__(self, amount: int, currency: str) -> None:
        if currency is None:
            raise ValueError('currencyがNoneです。')

        self.__amount: int = amount
        self.__currency: str = currency  # 通貨単位

    @property
    def amount(self) -> int:
        return self.__amount

    @property
    def currency(self) -> int:
        return self.__currency

    def add(self, arg: Money) -> Money:
        if arg is None:
            raise ValueError('Noneは使用できません。')

        if self.currency != arg.currency:
            raise ValueError('通貨の単位が違います。')

        return Money(self.amount + arg.amount, self.currency)
