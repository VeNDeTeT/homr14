import pytest
from src.product import Product
from src.category import Category


@pytest.fixture(autouse=True)
def reset_counters():
    """Сброс счётчиков перед каждым тестом"""
    Category.category_count = 0
    Category.product_count = 0


def test_product_initialization():
    """Инициализация продукта"""
    p = Product("Laptop", "Gaming laptop", 1500.0, 5)
    assert p.name == "Laptop"
    assert p.description == "Gaming laptop"
    assert p.price == 1500.0
    assert p.quantity == 5


def test_product_attributes_types():
    """Проверка типов атрибутов"""
    p = Product("Keyboard", "Mechanical keyboard", 150.0, 10)
    assert isinstance(p.name, str)
    assert isinstance(p.description, str)
    assert isinstance(p.price, float)
    assert isinstance(p.quantity, int)


def test_product_price_getter():
    """Геттер возвращает корректное значение цены"""
    p = Product("Item", "Description", 99.99, 5)
    assert p.price == 99.99


def test_product_price_setter_valid():
    """Сеттер устанавливает положительную цену"""
    p = Product("Test", "Desc", 10.0, 1)
    p.price = 20.5
    assert p.price == 20.5


def test_product_price_setter_zero(capfd):
    """Сеттер блокирует нулевую цену"""
    p = Product("Test", "Desc", 10.0, 1)
    p.price = 0
    captured = capfd.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert p.price == 10.0


def test_product_price_setter_negative(capfd):
    """Сеттер блокирует отрицательную цену"""
    p = Product("Test", "Desc", 10.0, 1)
    p.price = -5
    captured = capfd.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert p.price == 10.0


def test_product_str_output():
    """__str__ возвращает форматированную строку"""
    p = Product("Laptop", "Gaming", 1500.0, 3)
    expected = "Laptop, 1500.0 руб. Остаток: 3 шт."
    assert str(p) == expected


def test_product_str_special_chars():
    """__str__ с русскими символами"""
    p = Product("Клавиатура", "Механическая", 2500.50, 5)
    result = str(p)
    assert "Клавиатура" in result
    assert "2500.5" in result


def test_product_add_two_products():
    """__add__ вычисляет сумму стоимостей"""
    p1 = Product("A", "D", 100.0, 5)
    p2 = Product("B", "D", 50.0, 2)
    assert p1 + p2 == 600.0


def test_product_add_with_zero_quantity():
    """__add__ работает с нулевым количеством"""
    p1 = Product("A", "D", 100.0, 0)
    p2 = Product("B", "D", 50.0, 3)
    assert p1 + p2 == 150.0


def test_product_add_large_values():
    """__add__ с большими значениями"""
    p1 = Product("A", "D", 50000.0, 100)
    p2 = Product("B", "D", 10000.0, 50)
    # 50000*100 + 10000*50 = 5000000 + 500000 = 5500000
    assert p1 + p2 == 5500000.0


def test_product_add_type_error_int():
    """__add__ вызывает ошибку при сложении с int"""
    p = Product("Test", "D", 10, 1)
    with pytest.raises(TypeError):
        p + 5


def test_product_add_type_error_string():
    """__add__ вызывает ошибку при сложении со строкой"""
    p = Product("Test", "D", 10, 1)
    with pytest.raises(TypeError):
        p + "string"


def test_product_add_type_error_none():
    """__add__ вызывает ошибку при сложении с None"""
    p = Product("Test", "D", 10, 1)
    with pytest.raises(TypeError):
        p + None


def test_product_new_product_basic():
    """new_product создает объект из словаря"""
    params = {
        "name": "Item",
        "description": "Description",
        "price": 50.0,
        "quantity": 10,
    }
    p = Product.new_product(params)
    assert isinstance(p, Product)
    assert p.name == "Item"
    assert p.description == "Description"
    assert p.price == 50.0
    assert p.quantity == 10


def test_product_new_product_with_floats():
    """new_product с float значениями"""
    params = {
        "name": "Float Item",
        "description": "Desc",
        "price": 123.45,
        "quantity": 7,
    }
    p = Product.new_product(params)
    assert p.price == 123.45
    assert p.quantity == 7


def test_product_price_set_to_int():
    """Сеттер цены принимает int"""
    p = Product("Test", "D", 10.0, 1)
    p.price = 15
    assert p.price == 15


def test_product_price_set_multiple_times():
    """Сеттер может вызваться несколько раз"""
    p = Product("Test", "D", 10.0, 1)
    p.price = 20.0
    assert p.price == 20.0
    p.price = 30.0
    assert p.price == 30.0
    p.price = 25.5
    assert p.price == 25.5


def test_product_with_zero_quantity():
    """Продукт с нулевым количеством"""
    p = Product("Mouse", "Wireless mouse", 25.0, 0)
    assert p.quantity == 0
