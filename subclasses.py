from class_product import Product


class Smartphone(Product):

    def __init__(self, name, description, price, quantity, color, performance, model, memory):
        super().__init__(name, description, price, quantity, color)
        self.performance = performance
        self.model = model
        self.memory = memory

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __repr__(self):
        return f"{self.__class__.__name__},({self.__dict__.items()})"


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, color, country, germination):
        super().__init__(name, description, price, quantity, color)
        self.country = country
        self.germination = germination

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __repr__(self):
        return f"{self.__class__.__name__},({self.__dict__.items()})"
