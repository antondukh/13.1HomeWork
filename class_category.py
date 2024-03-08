class Category():
    name = str
    description = str
    goods = list

    total_categories = 0
    total_products = 0

    def __init__(self, name, description, goods):
        self.name = name
        self.description = description
        self.goods = goods

        Category.total_categories += 1
        Category.total_products = len(self.goods)
