import json


def open_js():
    with open('products.json', 'r', encoding="utf8") as file:
        products = file.read()
        json_file = json.loads(products)
        return json_file
