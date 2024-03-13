from funcs import open_js
from class_product import *


class Category():
    name = str
    description = str
    goods = list

    total_categories = 0
    total_products = 0

    def __init__(self, name, description, goods):
        self.name = name
        self.description = description
        self.__goods = goods
        self.prod_list = []
        Category.total_categories += 1
        Category.total_products = len(self.__goods)

    def add_product(self, x):
        self.prod_list.append(x)
        return self.prod_list

    @property
    def good_list(self):
        for item in self.__goods:
            print(f"{item['name']}, {item['price']} руб. Остаток: {item['quantity']}")



smartphone = Category(open_js()[0]['name'], open_js()[0]['description'], open_js()[0]['products'])
tv = Category(open_js()[1]['name'], open_js()[1]['description'], open_js()[1]['products'])

print(smartphone.good_list)


