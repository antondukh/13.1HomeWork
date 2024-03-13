#from class_category import Category
from funcs import open_js


class Product():
    name = str
    description = str
    price = float
    quantity = int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @classmethod
    def new_prod(cls, x):
        name, description, price, quantity = pass
        return cls(name, description, price, quantity)

    @property
    def prod_price(self):
        if self.price <= 0:
            print("цена введена некорректная")


new_prod_smart1 = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
new_prod_smart2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
new_prod_smart3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

new_prod_tv = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)



