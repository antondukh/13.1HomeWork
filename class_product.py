from abc import ABC, abstractmethod


class ProductABC(ABC):
    @abstractmethod
    def __str__(self):
        pass


class MixinProduct:
    def __repr__(self):
        pass


class Product(ProductABC):
    """Класс Продукты."""
    name = str
    description = str
    price = float
    quantity = int

    def __init__(self, name, description, price, quantity, color=None):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.color = color

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    @classmethod
    def new_prod(cls, **kwargs):
        """Метод создания объекта."""
        return cls(**kwargs)

    @property
    def price(self):
        """Вывод цены."""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Изменение цены."""
        if new_price <= 0:
            print("цена введена некорректная")
        else:
            self.__price = new_price

    def __add__(self, other):
        if type(self) != type(other):
            raise ValueError('Складывать можно только объекты одного класса')
        return (self.__price * self.quantity) + (other.__price * other.quantity)
