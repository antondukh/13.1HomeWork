

class Category():
    name = str
    description = str
    goods = str
    total_categories = int
    total_products = int

    def __init__(self, name, description, goods):
        self.name = name
        self.description = description
        self.goods = goods
