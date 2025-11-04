import pytest
from src.product import Product, Smartphone, LawnGrass
from src.category import Category


@pytest.fixture(autouse=True)
def reset_counters():
    """Сброс счётчиков перед каждым тестом"""
    Category.category_count = 0
    Category.product_count = 0


def test_category_creation():
    """Тест создания категории"""
    cat = Category("Техника", "Электроника")
    assert cat.name == "Техника"
    assert cat.description == "Электроника"
    assert Category.category_count == 1


def test_add_product():
    """Тест добавления товара"""
    cat = Category("Техника", "Описание")
    p = Product("Ноутбук", "Игровой", 75000.0, 1)
    cat.add_product(p)

    assert len(cat.products) == 1
    assert cat.products[0] is p
    assert Category.product_count == 1


def test_add_multiple_products():
    """Тест добавления нескольких товаров"""
    cat = Category("Техника", "Описание")
    p1 = Product("A", "D", 100.0, 1)
    p2 = Product("B", "E", 200.0, 2)
    p3 = Product("C", "F", 300.0, 3)

    cat.add_product(p1)
    cat.add_product(p2)
    cat.add_product(p3)

    assert len(cat.products) == 3
    assert Category.product_count == 3


def test_add_smartphone():
    """Тест добавления Smartphone"""
    cat = Category("Электроника", "Техника")
    phone = Smartphone("iPhone", "A", 100000.0, 1, "A17", "15", "256GB", "Черный")
    cat.add_product(phone)

    assert len(cat.products) == 1
    assert isinstance(cat.products[0], Smartphone)


def test_add_lawn_grass():
    """Тест добавления LawnGrass"""
    cat = Category("Сад", "Растения")
    grass = LawnGrass("Газон", "Трава", 1000.0, 5, "РФ", "7 дней", "Зеленый")
    cat.add_product(grass)

    assert len(cat.products) == 1
    assert isinstance(cat.products[0], LawnGrass)


def test_add_mixed_products():
    """Тест добавления товаров разных типов"""
    cat = Category("Смешанные", "Разные")

    p = Product("A", "D", 100.0, 1)
    phone = Smartphone("iPhone", "B", 100000.0, 1, "A17", "15", "256GB", "Черный")
    grass = LawnGrass("Газон", "C", 1000.0, 5, "РФ", "7 дней", "Зеленый")

    cat.add_product(p)
    cat.add_product(phone)
    cat.add_product(grass)

    assert len(cat.products) == 3
    assert Category.product_count == 3


def test_add_invalid_string():
    """Ошибка при добавлении строки"""
    cat = Category("Техника", "Описание")
    with pytest.raises(TypeError):
        cat.add_product("Not a product")


def test_add_invalid_number():
    """Ошибка при добавлении числа"""
    cat = Category("Техника", "Описание")
    with pytest.raises(TypeError):
        cat.add_product(123)


def test_add_invalid_dict():
    """Ошибка при добавлении словаря"""
    cat = Category("Техника", "Описание")
    with pytest.raises(TypeError):
        cat.add_product({"name": "Test"})


def test_products_str():
    """Тест метода products_str"""
    cat = Category("Техника", "Описание")
    p1 = Product("A", "D", 10.0, 1)
    p2 = Product("B", "E", 20.0, 2)

    cat.add_product(p1)
    cat.add_product(p2)

    expected = "A, 10.0 руб. Остаток: 1 шт.\nB, 20.0 руб. Остаток: 2 шт."
    assert cat.products_str == expected


def test_str_method():
    """Тест метода __str__"""
    p1 = Product("A", "D", 100.0, 5)
    p2 = Product("B", "E", 200.0, 3)
    cat = Category("Техника", "Описание", [p1, p2])

    result = str(cat)
    assert "Техника" in result
    assert "8" in result  # 5 + 3 = 8


def test_category_with_initial_products():
    """Тест создания категории с начальными продуктами"""
    p1 = Product("A", "D", 100.0, 1)
    p2 = Product("B", "E", 200.0, 2)

    cat = Category("Техника", "Описание", [p1, p2])

    assert len(cat.products) == 2
    assert Category.product_count == 2


def test_multiple_categories():
    """Тест создания нескольких категорий"""
    Category("Техника", "A")
    Category("Одежда", "B")
    Category("Еда", "C")

    assert Category.category_count == 3
