import pytest
from src.category import Category
from src.product import Product


def test_product_initialization():
    """Тест инициализации продукта"""
    product = Product("Laptop", "Gaming laptop", 1500.0, 5)
    assert product.name == "Laptop"
    assert product.description == "Gaming laptop"
    assert product.price == 1500.0
    assert product.quantity == 5


def test_product_with_zero_quantity():
    """Тест продукта с нулевым количеством"""
    product = Product("Mouse", "Wireless mouse", 25.0, 0)
    assert product.quantity == 0


def test_product_with_high_price():
    """Тест продукта с высокой ценой"""
    product = Product("Server", "Enterprise server", 50000.0, 1)
    assert product.price == 50000.0


def test_product_attributes_types():
    """Тест типов атрибутов продукта"""
    product = Product("Keyboard", "Mechanical keyboard", 150.0, 10)
    assert isinstance(product.name, str)
    assert isinstance(product.description, str)
    assert isinstance(product.price, float)
    assert isinstance(product.quantity, int)


def test_multiple_products_independence():
    """Тест независимости нескольких продуктов"""
    p1 = Product("Phone", "Smartphone", 800.0, 5)
    p2 = Product("Tablet", "Tablet device", 600.0, 3)

    assert p1.name != p2.name
    assert p1.price != p2.price
    assert p1.quantity != p2.quantity


def setup_function():
    Category.category_count = 0
    Category.product_count = 0


def test_add_product_and_counters():
    cat = Category("TestCat", "Desc")
    p1 = Product("A", "d", 10.0, 1)
    p2 = Product("B", "d", 20.0, 2)

    cat.add_product(p1)
    cat.add_product(p2)

    assert Category.category_count == 1
    assert Category.product_count == 2


def test_products_getter_format():
    cat = Category("TestCat", "Desc")
    p1 = Product("A", "d", 10.0, 1)
    p2 = Product("B", "d", 20.0, 2)

    cat.add_product(p1)
    cat.add_product(p2)

    expected = "A, 10.0 руб. Остаток: 1 шт.\nB, 20.0 руб. Остаток: 2 шт."
    assert cat.products_str == expected


def test_add_product_type_error():
    cat = Category("TestCat", "Desc")
    with pytest.raises(TypeError):
        cat.add_product("not a product")

def test_new_product_creates_instance():
    params = {"name":"X","description":"d","price":9.9,"quantity":4}
    p = Product.new_product(params)
    assert isinstance(p, Product)
    assert (p.name,p.description,p.price,p.quantity) == ("X","d",9.9,4)

def test_price_setter_accepts_positive():
    p = Product("A","d",5.5,1)
    p.price = 7.7
    assert p.price == 7.7

def test_price_setter_rejects_non_positive(capfd):
    p = Product("A","d",5.5,1)
    p.price = 0
    out = capfd.readouterr().out
    assert "Цена не должна быть нулевая или отрицательная" in out
    assert p.price == 5.5

def test_price_remains_on_negative(capfd):
    p = Product("A","d",5.5,1)
    p.price = -10
    assert p.price == 5.5