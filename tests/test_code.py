import pytest
from class_category import Category
from class_product import Product
from subclasses import Smartphone, LawnGrass


def test_category():
    a = Category('фрукты', 'фрукт', ['банан'])
    assert a.total_categories == 1
    b = Category('овощи', 'овощ', ['капуста'])
    assert b.total_categories == 2


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


def test_product():
    a = Category('фрукты', 'фрукт', ['банан', 'киви', 'слива'])
    assert a.total_products == 3


@pytest.fixture
def class_smartphone():
    return Smartphone("Iphone", "Смартфон", 120000.0, 6, "black", "USA", 14, 256)


def test_init_smartphone(class_smartphone):
    assert class_smartphone.name == "Iphone"
    assert class_smartphone.description == "Смартфон"
    assert class_smartphone.price == 120000.0
    assert class_smartphone.quantity == 6
    assert class_smartphone.color == "black"
    assert class_smartphone.performance == "USA"
    assert class_smartphone.model == 14
    assert class_smartphone.memory == 256


@pytest.fixture
def class_lawngrass():
    return LawnGrass("Трава", "трава для газона", 5000.0, 5, "green", "Russia", 4)


def test_init_lawngrass(class_lawngrass):
    assert class_lawngrass.name == "Трава"
    assert class_lawngrass.description == "трава для газона"
    assert class_lawngrass.price == 5000.0
    assert class_lawngrass.quantity == 5
    assert class_lawngrass.color == "green"
    assert class_lawngrass.country == "Russia"
    assert class_lawngrass.germination == 4
