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


d1 = LawnGrass("Трава", "трава для газона", 5000.0, 5, "green", "Russia", 4)
d1_1 = LawnGrass("Трава", "трава для газона", 5000.0, 5, "green", "Russia", 4)
d2 = Product("Samsung", "Смартфон", 86000.0, 3, "grey")
d2_2 = Product("Samsung", "Смартфон", 86000.0, 3, "grey")
d3 = Smartphone("Iphone", "Смартфон", 120000.0, 6, "black", "USA", 14, 256)
d3_3 = Smartphone("Iphone", "Смартфон", 120000.0, 6, "black", "USA", 14, 256)
