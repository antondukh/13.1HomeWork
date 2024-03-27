from class_product import Product


class Smartphone(Product):

    def __init__(self, name, description, price, quantity, color, performance, model, memory):
        super().__init__(name, description, price, quantity, color)
        self.performance = performance
        self.model = model
        self.memory = memory


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, color, country, germination):
        super().__init__(name, description, price, quantity, color)
        self.country = country
        self.germination = germination

