import pytest
from src.product import Product, Smartphone, LawnGrass
from src.category import Category


@pytest.fixture(autouse=True)
def reset_counters():
    """Сброс счётчиков перед каждым тестом"""
    Category.category_count = 0
    Category.product_count = 0


# ===== ТЕСТЫ ЗАДАНИЕ 1: ValueError при quantity=0 =====


def test_product_zero_quantity_raises_value_error():
    """Создание Product с quantity=0 выбрасывает ValueError"""
    with pytest.raises(ValueError) as excinfo:
        Product("Test", "Desc", 100.0, 0)
    assert "Товар с нулевым количеством не может быть добавлен" in str(excinfo.value)


def test_smartphone_zero_quantity_raises_value_error():
    """Создание Smartphone с quantity=0 выбрасывает ValueError"""
    with pytest.raises(ValueError) as excinfo:
        Smartphone("iPhone", "A", 100000.0, 0, "A17", "15", "256GB", "Черный")
    assert "Товар с нулевым количеством не может быть добавлен" in str(excinfo.value)


def test_lawn_grass_zero_quantity_raises_value_error():
    """Создание LawnGrass с quantity=0 выбрасывает ValueError"""
    with pytest.raises(ValueError) as excinfo:
        LawnGrass("Газон", "Трава", 1000.0, 0, "РФ", "7 дней", "Зеленый")
    assert "Товар с нулевым количеством не может быть добавлен" in str(excinfo.value)


def test_product_positive_quantity_works():
    """Создание Product с quantity>0 работает нормально"""
    p = Product("Test", "Desc", 100.0, 1)
    assert p.name == "Test"
    assert p.quantity == 1


def test_product_large_quantity_works():
    """Создание Product с большим quantity работает"""
    p = Product("Test", "Desc", 100.0, 1000)
    assert p.quantity == 1000


# ===== ТЕСТЫ ЗАДАНИЕ 2: Средний ценник =====


def test_average_price_with_products():
    """Средний ценник с товарами"""
    cat = Category("Электроника", "Техника")
    p1 = Product("A", "D", 100.0, 1)
    p2 = Product("B", "E", 200.0, 1)
    p3 = Product("C", "F", 300.0, 1)

    cat.add_product(p1)
    cat.add_product(p2)
    cat.add_product(p3)

    assert cat.average_price() == 200.0


def test_average_price_empty_category():
    """Средний ценник пустой категории возвращает 0"""
    cat = Category("Пустая", "Без товаров")
    assert cat.average_price() == 0


def test_average_price_one_product():
    """Средний ценник с одним товаром"""
    cat = Category("Test", "Desc")
    p = Product("A", "D", 150.0, 1)
    cat.add_product(p)

    assert cat.average_price() == 150.0


def test_average_price_different_prices():
    """Средний ценник с разными ценами"""
    cat = Category("Test", "Desc")
    p1 = Product("A", "D", 50.0, 1)
    p2 = Product("B", "E", 100.0, 1)

    cat.add_product(p1)
    cat.add_product(p2)

    assert cat.average_price() == 75.0


def test_average_price_with_smartphones():
    """Средний ценник смартфонов"""
    cat = Category("Смартфоны", "Техника")
    phone1 = Smartphone("iPhone", "A", 100000.0, 1, "A17", "15", "256GB", "Черный")
    phone2 = Smartphone(
        "Samsung", "B", 80000.0, 1, "Snapdragon", "S24", "128GB", "Белый"
    )

    cat.add_product(phone1)
    cat.add_product(phone2)

    assert cat.average_price() == 90000.0


def test_average_price_mixed_products():
    """Средний ценник смешанных товаров"""
    cat = Category("Смешанные", "Разные")

    p = Product("Ноутбук", "A", 75000.0, 1)
    phone = Smartphone("iPhone", "B", 100000.0, 1, "A17", "15", "256GB", "Черный")
    grass = LawnGrass("Газон", "C", 1000.0, 1, "РФ", "7 дней", "Зеленый")

    cat.add_product(p)
    cat.add_product(phone)
    cat.add_product(grass)

    # (75000 + 100000 + 1000) / 3 = 58666.67
    assert round(cat.average_price(), 2) == 58666.67


def test_average_price_returns_float():
    """average_price возвращает float"""
    cat = Category("Test", "Desc")
    p = Product("A", "D", 100.0, 1)
    cat.add_product(p)

    result = cat.average_price()
    assert isinstance(result, float)


def test_average_price_zero_for_empty():
    """Проверка явного возврата 0 для пустой категории"""
    cat = Category("Empty", "No products")
    result = cat.average_price()
    assert result == 0
    assert isinstance(result, (int, float))


# ===== ПРОВЕРКА СОВМЕСТИМОСТИ СО СТАРЫМИ ТЕСТАМИ =====


def test_old_functionality_still_works():
    """Старая функциональность продолжает работать"""
    p1 = Product("A", "D", 100.0, 5)
    p2 = Product("B", "E", 200.0, 3)

    assert p1.name == "A"
    assert p1.price == 100.0
    assert p1 + p2 == 100.0 * 5 + 200.0 * 3


def test_category_add_product_still_works():
    """Добавление товаров в категорию работает"""
    cat = Category("Test", "Desc")
    p = Product("A", "D", 100.0, 1)
    cat.add_product(p)

    assert len(cat.products) == 1
