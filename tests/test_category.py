import pytest
from src.product import Product, Smartphone, LawnGrass
from src.category import Category


@pytest.fixture(autouse=True)
def reset_counters():
    """Сброс счётчиков перед каждым тестом"""
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def sample_products():
    """Образцы продуктов для тестов"""
    return [
        Product("Apple", "Fresh red apple", 1.5, 10),
        Product("Banana", "Yellow banana", 1.0, 5),
        Product("Orange", "Juicy orange", 2.0, 8),
    ]


def test_category_init_with_products(sample_products):
    """Инициализация категории с товарами"""
    cat = Category("Fruits", "Fresh fruits", sample_products)
    assert cat.name == "Fruits"
    assert cat.description == "Fresh fruits"
    assert len(cat.products) == 3
    assert Category.category_count == 1
    assert Category.product_count == 3


def test_category_init_empty():
    """Инициализация пустой категории"""
    cat = Category("Empty", "No items", [])
    assert cat.name == "Empty"
    assert cat.products == []
    assert Category.category_count == 1
    assert Category.product_count == 0


def test_category_multiple_categories():
    """Подсчёт нескольких категорий"""
    p1 = Product("Book", "Fiction", 15.0, 5)
    p2 = Product("Pen", "Blue pen", 2.0, 20)

    Category("Books", "Literature", [p1])
    Category("Stationery", "Office supplies", [p2])

    assert Category.category_count == 2
    assert Category.product_count == 2


def test_add_product_and_counters():
    """Добавление товара в категорию"""
    cat = Category("Tech", "Technology")
    p1 = Product("Laptop", "Gaming", 1500.0, 2)
    p2 = Product("Mouse", "Wireless", 50.0, 10)

    cat.add_product(p1)
    cat.add_product(p2)

    assert len(cat.products) == 2
    assert Category.product_count == 2
    assert cat.products[0].name == "Laptop"
    assert cat.products[1].name == "Mouse"


def test_add_product_type_error():
    """Проверка ошибки при добавлении не-Product"""
    cat = Category("Test", "Test")
    with pytest.raises(TypeError):
        cat.add_product("not a product")


def test_products_str_with_items():
    """Проверка строкового вывода продуктов"""
    p1 = Product("A", "d", 10.0, 1)
    p2 = Product("B", "d", 20.0, 2)
    cat = Category("Test", "Desc", [p1, p2])

    expected = "A, 10.0 руб. Остаток: 1 шт.\nB, 20.0 руб. Остаток: 2 шт."
    assert cat.products_str == expected


def test_products_str_empty():
    """Проверка пустого списка товаров"""
    cat = Category("Empty", "No items")
    assert cat.products_str == ""


def test_category_str():
    """Проверка строкового представления категории"""
    p1 = Product("A", "D", 10, 5)
    p2 = Product("B", "E", 20, 7)
    cat = Category("Техника", "Описание", [p1, p2])

    # Общее количество: 5 + 7 = 12
    assert str(cat) == "Техника, количество продуктов: 12 шт."


def test_category_attributes_types(sample_products):
    """Проверка типов атрибутов"""
    cat = Category("Test", "Test category", sample_products)

    assert isinstance(cat.name, str)
    assert isinstance(cat.description, str)
    assert isinstance(cat.products, list)
    assert isinstance(Category.category_count, int)
    assert isinstance(Category.product_count, int)


# tests/test_category.py — добавить в конец


def test_category_products_list_access():
    """Проверка доступа к list продуктов через products"""
    p1 = Product("A", "D", 10, 1)
    p2 = Product("B", "D", 20, 2)
    cat = Category("Cat", "Desc", [p1, p2])

    assert len(cat.products) == 2
    assert cat.products[0] is p1
    assert cat.products[1] is p2


def test_category_products_str_single_item():
    """products_str для категории с одним товаром"""
    p = Product("Single", "Item", 50.0, 1)
    cat = Category("Cat", "Desc", [p])

    assert cat.products_str == "Single, 50.0 руб. Остаток: 1 шт."


def test_category_str_single_product():
    """__str__ категории с одним товаром"""
    p = Product("Item", "Desc", 100, 5)
    cat = Category("SingleCat", "Desc", [p])

    assert str(cat) == "SingleCat, количество продуктов: 5 шт."


def test_category_str_empty():
    """__str__ пустой категории"""
    cat = Category("Empty", "No items", [])

    assert str(cat) == "Empty, количество продуктов: 0 шт."


def test_category_add_multiple_then_check():
    """Добавление нескольких товаров и проверка lists"""
    cat = Category("Multi", "Desc")
    products = [
        Product("A", "D", 10, 1),
        Product("B", "D", 20, 2),
        Product("C", "D", 30, 3),
    ]

    for p in products:
        cat.add_product(p)

    assert len(cat.products) == 3
    assert sum(pr.quantity for pr in cat.products) == 6


def test_init_with_products_list():
    """Инициализация категории с передачей списка товаров"""
    products = [Product("X", "D", 5, 2), Product("Y", "D", 10, 3)]
    cat = Category("Init", "Desc", products)

    assert len(cat.products) == 2
    assert Category.product_count == 2


def test_category_counters_reset():
    """Проверка счётчиков после reset"""
    Category.category_count = 0
    Category.product_count = 0

    p = Product("Test", "D", 1, 1)
    Category("Cat1", "D", [p])

    assert Category.category_count == 1
    assert Category.product_count == 1


# === ДОПОЛНИТЕЛЬНЫЕ ТЕСТЫ ДЛЯ ПОКРЫТИЯ ===


def test_category_init_without_products_list():
    """Инициализация категории без списка товаров"""
    cat = Category("New", "Description")
    assert cat.name == "New"
    assert len(cat.products) == 0


def test_category_products_str_with_empty_list():
    """products_str для пустого списка товаров"""
    cat = Category("Empty", "No products")
    result = cat.products_str
    assert result == ""
    assert isinstance(result, str)


def test_category_products_getter_returns_list():
    """Геттер products возвращает список"""
    p = Product("Item", "D", 10, 1)
    cat = Category("Cat", "D", [p])
    result = cat.products
    assert isinstance(result, list)
    assert len(result) == 1


def test_category_str_format():
    """Проверка формата __str__"""
    p1 = Product("A", "D", 100, 5)
    p2 = Product("B", "D", 200, 3)
    cat = Category("Category", "Description", [p1, p2])
    result = str(cat)
    assert "Category" in result
    assert "8" in result  # 5+3
    assert "шт" in result


# ===== ПРАВИЛЬНОЕ ДОБАВЛЕНИЕ =====


def test_add_product_to_category():
    """Добавление обычного Product"""
    cat = Category("Техника", "D")
    p = Product("Ноутбук", "Игровой", 75000.0, 1)
    cat.add_product(p)
    assert len(cat.products) == 1
    assert cat.products[0] is p


def test_add_smartphone_to_category():
    """Добавление Smartphone в категорию"""
    cat = Category("Электроника", "Техника")
    phone = Smartphone(
        "iPhone", "Смартфон", 100000.0, 2, "A17", "15", "256GB", "Черный"
    )
    cat.add_product(phone)
    assert len(cat.products) == 1
    assert isinstance(cat.products[0], Smartphone)


def test_add_lawn_grass_to_category():
    """Добавление LawnGrass в категорию"""
    cat = Category("Сад", "Растения")
    grass = LawnGrass("Газон", "Трава", 1000.0, 5, "РФ", "7 дней", "Зеленый")
    cat.add_product(grass)
    assert len(cat.products) == 1
    assert isinstance(cat.products[0], LawnGrass)


def test_add_mixed_products():
    """Добавление товаров разных типов в категорию"""
    cat = Category("Смешанные", "Разные")

    p = Product("Ноутбук", "A", 75000.0, 1)
    phone = Smartphone("iPhone", "B", 100000.0, 2, "A17", "15", "256GB", "Черный")
    grass = LawnGrass("Газон", "C", 1000.0, 5, "РФ", "7 дней", "Зеленый")

    cat.add_product(p)
    cat.add_product(phone)
    cat.add_product(grass)

    assert len(cat.products) == 3
    assert Category.product_count == 3


# ===== ОШИБКИ (НЕПРАВИЛЬНОЕ ДОБАВЛЕНИЕ) =====


def test_add_string_to_category():
    """Ошибка: добавление строки"""
    cat = Category("Электроника", "Техника")
    with pytest.raises(TypeError):
        cat.add_product("Это не продукт")


def test_add_integer_to_category():
    """Ошибка: добавление числа"""
    cat = Category("Электроника", "Техника")
    with pytest.raises(TypeError):
        cat.add_product(123)


def test_add_dict_to_category():
    """Ошибка: добавление словаря"""
    cat = Category("Электроника", "Техника")
    with pytest.raises(TypeError):
        cat.add_product({"name": "Test"})


def test_add_list_to_category():
    """Ошибка: добавление списка"""
    cat = Category("Электроника", "Техника")
    with pytest.raises(TypeError):
        cat.add_product(["A", "B"])


def test_add_none_to_category():
    """Ошибка: добавление None"""
    cat = Category("Электроника", "Техника")
    with pytest.raises(TypeError):
        cat.add_product(None)


# ===== ПРОВЕРКА isinstance =====


def test_isinstance_checks():
    """Проверка работы isinstance()"""
    p = Product("A", "B", 100, 1)
    phone = Smartphone("A", "B", 100, 1, "A17", "15", "256GB", "Черный")
    grass = LawnGrass("A", "B", 100, 1, "РФ", "7 дней", "Зеленый")

    # Все являются Product или его наследниками
    assert isinstance(p, Product)  # True
    assert isinstance(phone, Product)  # True
    assert isinstance(grass, Product)  # True

    # Проверка типов наследников
    assert isinstance(phone, Smartphone)  # True
    assert isinstance(grass, LawnGrass)  # True

    # Они не являются друг другом
    assert not isinstance(phone, LawnGrass)  # False
    assert not isinstance(grass, Smartphone)  # False


def test_category_products_str_with_smartphone():
    """Проверка products_str с Smartphone"""
    cat = Category("Электроника", "Техника")
    phone = Smartphone(
        "iPhone", "Смартфон", 100000.0, 1, "A17", "15", "256GB", "Черный"
    )
    cat.add_product(phone)

    result = cat.products_str
    assert "iPhone" in result
    assert "100000.0" in result


def test_category_products_str_with_lawn_grass():
    """Проверка products_str с LawnGrass"""
    cat = Category("Сад", "Растения")
    grass = LawnGrass("Газон", "Трава", 1000.0, 1, "РФ", "7 дней", "Зеленый")
    cat.add_product(grass)

    result = cat.products_str
    assert "Газон" in result
    assert "1000.0" in result


def test_category_str_with_smartphone():
    """Проверка __str__ категории со Smartphone"""
    phone = Smartphone(
        "iPhone", "Смартфон", 100000.0, 5, "A17", "15", "256GB", "Черный"
    )
    cat = Category("Электроника", "Техника", [phone])

    result = str(cat)
    assert "Электроника" in result
    assert "5" in result


def test_category_str_with_lawn_grass():
    """Проверка __str__ категории с LawnGrass"""
    grass = LawnGrass("Газон", "Трава", 1000.0, 10, "РФ", "7 дней", "Зеленый")
    cat = Category("Сад", "Растения", [grass])

    result = str(cat)
    assert "Сад" in result
    assert "10" in result


def test_category_products_str_multiple_types():
    """Проверка products_str с разными типами товаров"""
    cat = Category("Смешанные", "Разные")

    p = Product("Ноутбук", "A", 75000.0, 1)
    phone = Smartphone("iPhone", "B", 100000.0, 1, "A17", "15", "256GB", "Черный")
    grass = LawnGrass("Газон", "C", 1000.0, 1, "РФ", "7 дней", "Зеленый")

    cat.add_product(p)
    cat.add_product(phone)
    cat.add_product(grass)

    result = cat.products_str
    assert "Ноутбук" in result
    assert "iPhone" in result
    assert "Газон" in result
    assert result.count("\n") >= 2  # минимум 2 перевода строк
