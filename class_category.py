from class_product import Product


class Category:
    """Класс Категория товаров"""
    name = str
    description = str
    goods = list

    total_categories = 0
    total_products = 0

    def __init__(self, name, description, goods):
        self.name = name
        self.description = description
        self.__goods = goods
        Category.total_categories += 1
        Category.total_products = len(self.__goods)

    def add_product(self, prod):
        """Добавление объекта товара в список."""
        if not isinstance(prod, Product):
            raise ValueError('Складывать можно только объекты одного класса')
        self.__goods.append(prod)


    @property
    def goods(self):
        """Вывод списка товаров."""
        for good in self.__goods:
            print(f"{good.name}, {good.price} руб. Остаток: {good.quantity}")

    def __len__(self):
        quantity_all = 0
        for i in self.__goods:
            quantity_all += i.quantity
        return quantity_all

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self)}"
