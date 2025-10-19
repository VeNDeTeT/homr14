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
