from funcs import open_js


class Product():
    """Класс Продукты."""
    name = str
    description = str
    price = float
    quantity = int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

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
        return (self.__price * self.quantity) + (other.__price * other.quantity)


smart = open_js()[0]["products"]
tv_ = open_js()[1]["products"]


new_prod_smart1 = Product(smart[0]['name'], smart[0]['description'], smart[0]['price'], smart[0]['quantity'])
new_prod_smart2 = Product(smart[1]['name'], smart[1]['description'], smart[1]['price'], smart[1]['quantity'])
new_prod_smart3 = Product(smart[2]['name'], smart[2]['description'], smart[2]['price'], smart[2]['quantity'])

new_p = Product.new_prod(**smart[1])

print(new_prod_smart1)
print(new_prod_smart1 + new_prod_smart2)
