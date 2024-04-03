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

    @property
    def average_price(self):
        """Gодсчитывает средний ценник всех товаров."""
        quantity_all = 0
        price_all = 0
        for i in self.__goods:
            quantity_all += i.quantity
        for i in self.__goods:
            price_all += i.price
        try:
            quantity_all = 0
            result = price_all / quantity_all
        except ZeroDivisionError:
            return 0

        return price_all / quantity_all


    def add_product(self, prod):
        """Добавление объекта товара в список."""
        if not isinstance(prod, Product):
            raise ValueError('Складывать можно только объекты одного класса')
        elif prod.quantity == 0:
            raise ValueError('товар с нулевым количеством не может быть добавлен')
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


a = Category('фрукты', 'фрукт', [])
b = Product('Фуджи', 'яблоки', 50, 1)
f = Product('Фуджи', 'яблоки', 100, 1)
a.add_product(b)
a.add_product(f)

print(a.average_price)

