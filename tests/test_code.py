import pytest
from class_category import Category
from class_product import Product


@pytest.fixture
def class_category():
    return Category('фрукты', 'фрукт', 'банан')


def test_init_category(class_category):
    assert class_category.name == 'фрукты'
    assert class_category.description == 'фрукт'
    assert class_category.goods == 'банан'


@pytest.fixture
def class_product():
    return Product('Фуджи', 'яблоки', 105.56, 45)


def test_init_product(class_product):
    assert class_product.name == 'Фуджи'
    assert class_product.description == 'яблоки'
    assert class_product.price == 105.56
    assert class_product.quantity == 45


class TestCategory():
    total_categories = 5
    total_products = 5


cat_1 = TestCategory


def test_category():
    assert cat_1.total_categories == 5
    assert cat_1.total_products == 5
