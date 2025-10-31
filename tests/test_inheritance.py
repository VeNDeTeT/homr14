import pytest
from src.product import Product, Smartphone, LawnGrass
from src.category import Category


@pytest.fixture(autouse=True)
def reset_counters():
    """Сброс счётчиков перед каждым тестом"""
    Category.category_count = 0
    Category.product_count = 0


# ===== ЗАДАНИЕ 1: ТЕСТЫ НАСЛЕДОВАНИЯ =====


def test_smartphone_initialization():
    """Тест инициализации Smartphone"""
    phone = Smartphone(
        "iPhone 15", "Смартфон Apple", 100000.0, 10, "A17", "15 Pro", "512GB", "Черный"
    )
    assert phone.name == "iPhone 15"
    assert phone.description == "Смартфон Apple"
    assert phone.efficiency == "A17"
    assert phone.model == "15 Pro"
    assert phone.memory == "512GB"
    assert phone.color == "Черный"


def test_lawn_grass_initialization():
    """Тест инициализации LawnGrass"""
    grass = LawnGrass(
        "Газон Элит",
        "Премиум трава",
        1500.0,
        50,
        "Нидерланды",
        "10 дней",
        "Темно-зеленый",
    )
    assert grass.name == "Газон Элит"
    assert grass.description == "Премиум трава"
    assert grass.country == "Нидерланды"
    assert grass.germination_period == "10 дней"
    assert grass.color == "Темно-зеленый"


def test_smartphone_inherits_from_product():
    """Проверка наследования Smartphone от Product"""
    phone = Smartphone(
        "Samsung", "Galaxy", 80000.0, 5, "Snapdragon", "S24", "256GB", "Белый"
    )
    assert isinstance(phone, Product)
    assert isinstance(phone, Smartphone)


def test_lawn_grass_inherits_from_product():
    """Проверка наследования LawnGrass от Product"""
    grass = LawnGrass(
        "Спорт", "Спортивная трава", 2000.0, 30, "Германия", "7 дней", "Ярко-зеленый"
    )
    assert isinstance(grass, Product)
    assert isinstance(grass, LawnGrass)


def test_smartphone_price_setter():
    """Проверка сеттера цены в Smartphone"""
    phone = Smartphone("iPhone", "A", 100000.0, 1, "A17", "15", "256GB", "Черный")
    phone.price = 110000.0
    assert phone.price == 110000.0


def test_smartphone_price_setter_invalid(capfd):
    """Проверка сеттера цены с невалидным значением"""
    phone = Smartphone("iPhone", "A", 100000.0, 1, "A17", "15", "256GB", "Черный")
    phone.price = 0
    captured = capfd.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert phone.price == 100000.0


def test_smartphone_str():
    """Проверка __str__ Smartphone"""
    phone = Smartphone(
        "iPhone", "Смартфон", 100000.0, 1, "A17", "15", "256GB", "Черный"
    )
    result = str(phone)
    assert "iPhone" in result
    assert "A17" in result
    assert "256GB" in result
    assert "Черный" in result


def test_lawn_grass_str():
    """Проверка __str__ LawnGrass"""
    grass = LawnGrass("Газон", "Трава", 1000.0, 5, "РФ", "7 дней", "Зеленый")
    result = str(grass)
    assert "Газон" in result
    assert "РФ" in result
    assert "7 дней" in result
    assert "Зеленый" in result


# ===== ЗАДАНИЕ 2: ТЕСТЫ СЛОЖЕНИЯ С type() =====


def test_add_two_products():
    """Сложение двух обычных Product"""
    p1 = Product("Ноутбук", "A", 75000.0, 2)
    p2 = Product("Планшет", "B", 50000.0, 1)
    assert p1 + p2 == 75000.0 * 2 + 50000.0 * 1


def test_add_two_smartphones():
    """Сложение двух Smartphone"""
    phone1 = Smartphone("iPhone", "A", 50000.0, 2, "A17", "15", "256GB", "Черный")
    phone2 = Smartphone(
        "Samsung", "B", 40000.0, 3, "Snapdragon", "S24", "128GB", "Белый"
    )
    assert phone1 + phone2 == 50000.0 * 2 + 40000.0 * 3


def test_add_two_lawn_grass():
    """Сложение двух LawnGrass"""
    grass1 = LawnGrass("Газон1", "A", 1000.0, 5, "РФ", "7 дней", "Зеленый")
    grass2 = LawnGrass("Газон2", "B", 1500.0, 3, "Франция", "10 дней", "Светло-зеленый")
    assert grass1 + grass2 == 1000.0 * 5 + 1500.0 * 3


def test_add_smartphone_and_lawn_grass_type_error():
    """Ошибка при сложении Smartphone и LawnGrass"""
    phone = Smartphone("iPhone", "A", 50000.0, 1, "A17", "15", "256GB", "Черный")
    grass = LawnGrass("Газон", "B", 1000.0, 1, "РФ", "7 дней", "Зеленый")
    with pytest.raises(TypeError):
        phone + grass


def test_add_smartphone_and_product_type_error():
    """Ошибка при сложении Smartphone и Product"""
    phone = Smartphone("iPhone", "A", 50000.0, 1, "A17", "15", "256GB", "Черный")
    product = Product("Ноутбук", "B", 75000.0, 1)
    with pytest.raises(TypeError):
        phone + product


def test_add_lawn_grass_and_product_type_error():
    """Ошибка при сложении LawnGrass и Product"""
    grass = LawnGrass("Газон", "A", 1000.0, 1, "РФ", "7 дней", "Зеленый")
    product = Product("Ноутбук", "B", 75000.0, 1)
    with pytest.raises(TypeError):
        grass + product


def test_add_product_and_smartphone_type_error():
    """Ошибка при сложении Product и Smartphone"""
    product = Product("Ноутбук", "A", 75000.0, 1)
    phone = Smartphone("iPhone", "B", 50000.0, 1, "A17", "15", "256GB", "Черный")
    with pytest.raises(TypeError):
        product + phone


# ===== ЗАДАНИЕ 3: ТЕСТЫ isinstance В add_product =====


def test_add_product_to_category():
    """Добавление Product в категорию"""
    cat = Category("Техника", "Описание")
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


def test_add_mixed_products_to_category():
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


def test_add_string_to_category():
    """Ошибка: добавление строки в категорию"""
    cat = Category("Электроника", "Техника")
    with pytest.raises(TypeError):
        cat.add_product("Это не продукт")


def test_add_integer_to_category():
    """Ошибка: добавление числа в категорию"""
    cat = Category("Электроника", "Техника")
    with pytest.raises(TypeError):
        cat.add_product(123)


def test_add_dict_to_category():
    """Ошибка: добавление словаря в категорию"""
    cat = Category("Электроника", "Техника")
    with pytest.raises(TypeError):
        cat.add_product({"name": "Test"})


def test_add_list_to_category():
    """Ошибка: добавление списка в категорию"""
    cat = Category("Электроника", "Техника")
    with pytest.raises(TypeError):
        cat.add_product(["A", "B"])


def test_add_none_to_category():
    """Ошибка: добавление None в категорию"""
    cat = Category("Электроника", "Техника")
    with pytest.raises(TypeError):
        cat.add_product(None)


# ===== ПРОВЕРКА ОБРАТНОЙ СОВМЕСТИМОСТИ =====


def test_old_product_functionality():
    """Проверка старой функциональности Product"""
    p = Product("Ноутбук", "Игровой", 75000.0, 5)
    assert p.name == "Ноутбук"
    assert p.description == "Игровой"
    assert p.price == 75000.0
    assert p.quantity == 5
    assert str(p) == "Ноутбук, 75000.0 руб. Остаток: 5 шт."


def test_old_category_functionality():
    """Проверка старой функциональности Category"""
    p = Product("Ноутбук", "Игровой", 75000.0, 5)
    cat = Category("Электроника", "Техника", [p])
    assert len(cat.products) == 1
    assert str(cat) == "Электроника, количество продуктов: 5 шт."


def test_old_add_product():
    """Проверка старого метода add_product"""
    cat = Category("Электроника", "Техника")
    p1 = Product("A", "D", 10.0, 1)
    p2 = Product("B", "E", 20.0, 2)

    cat.add_product(p1)
    cat.add_product(p2)

    assert len(cat.products) == 2
    assert Category.product_count == 2


def test_old_products_str():
    """Проверка старого products_str"""
    p1 = Product("A", "D", 10.0, 1)
    p2 = Product("B", "E", 20.0, 2)
    cat = Category("Test", "Desc", [p1, p2])

    expected = "A, 10.0 руб. Остаток: 1 шт.\nB, 20.0 руб. Остаток: 2 шт."
    assert cat.products_str == expected


# ===== ДОПОЛНИТЕЛЬНЫЕ ТЕСТЫ =====


def test_isinstance_checks():
    """Проверка работы isinstance()"""
    p = Product("A", "B", 100, 1)
    phone = Smartphone("A", "B", 100, 1, "A17", "15", "256GB", "Черный")
    grass = LawnGrass("A", "B", 100, 1, "РФ", "7 дней", "Зеленый")

    # Все являются Product или его наследниками
    assert isinstance(p, Product)
    assert isinstance(phone, Product)
    assert isinstance(grass, Product)

    # Проверка типов наследников
    assert isinstance(phone, Smartphone)
    assert isinstance(grass, LawnGrass)

    # Они не являются друг другом
    assert not isinstance(phone, LawnGrass)
    assert not isinstance(grass, Smartphone)


def test_type_checks():
    """Проверка работы type()"""
    p = Product("A", "B", 100, 1)
    phone = Smartphone("A", "B", 100, 1, "A17", "15", "256GB", "Черный")
    grass = LawnGrass("A", "B", 100, 1, "РФ", "7 дней", "Зеленый")

    # Точное совпадение типов
    assert type(p) is Product
    assert type(phone) is Smartphone
    assert type(grass) is LawnGrass

    # Они не равны
    assert type(p) is not type(phone)
    assert type(phone) is not type(grass)
    assert type(p) is not type(grass)
