import pytest
from src.product import BaseProduct, Product, Smartphone, LawnGrass, MixinLog
from src.category import Category


@pytest.fixture(autouse=True)
def reset_counters():
    """Сброс счётчиков перед каждым тестом"""
    Category.category_count = 0
    Category.product_count = 0


# ===== ТЕСТЫ АБСТРАКТНОГО КЛАССА =====


def test_cannot_instantiate_base_product():
    """Нельзя создать экземпляр абстрактного класса"""
    with pytest.raises(TypeError):
        BaseProduct()


def test_product_is_subclass_of_base_product():
    """Product наследует от BaseProduct"""
    assert issubclass(Product, BaseProduct)


def test_smartphone_is_subclass_of_base_product():
    """Smartphone наследует от BaseProduct через Product"""
    assert issubclass(Smartphone, BaseProduct)


def test_lawn_grass_is_subclass_of_base_product():
    """LawnGrass наследует от BaseProduct через Product"""
    assert issubclass(LawnGrass, BaseProduct)


# ===== ТЕСТЫ МИКСИНА ЛОГИРОВАНИЯ =====


def test_mixin_log_in_product(capfd):
    """Логирование при создании Product"""
    Product("Товар", "Описание", 100.0, 5)
    captured = capfd.readouterr()
    assert "Product" in captured.out
    assert "Товар" in captured.out


def test_mixin_log_in_smartphone(capfd):
    """Логирование при создании Smartphone"""
    Smartphone(
        "iPhone", "Смартфон", 100000.0, 1, "A17", "15", "256GB", "Черный"
    )
    captured = capfd.readouterr()
    assert "Smartphone" in captured.out
    assert "iPhone" in captured.out


def test_mixin_log_in_lawn_grass(capfd):
    """Логирование при создании LawnGrass"""
    LawnGrass("Газон", "Трава", 1000.0, 5, "РФ", "7 дней", "Зеленый")
    captured = capfd.readouterr()
    assert "LawnGrass" in captured.out
    assert "Газон" in captured.out


def test_repr_method_product():
    """Тест __repr__ для Product"""
    p = Product("A", "B", 100.0, 5)
    repr_str = p.__repr__()
    assert isinstance(repr_str, str)
    assert "A" in repr_str
    assert "B" in repr_str


def test_repr_method_smartphone():
    """Тест __repr__ для Smartphone"""
    phone = Smartphone("iPhone", "A", 100000.0, 1, "A17", "15", "256GB", "Черный")
    repr_str = phone.__repr__()
    assert "A17" in repr_str
    assert "256GB" in repr_str


def test_repr_method_lawn_grass():
    """Тест __repr__ для LawnGrass"""
    grass = LawnGrass("Газон", "A", 1000.0, 5, "РФ", "7 дней", "Зеленый")
    repr_str = grass.__repr__()
    assert "РФ" in repr_str
    assert "7 дней" in repr_str


def test_mixin_order():
    """Проверка порядка наследования (MRO)"""
    mro = Product.__mro__
    mixin_index = mro.index(MixinLog)
    base_index = mro.index(BaseProduct)
    # MixinLog должен быть перед BaseProduct
    assert mixin_index < base_index


# ===== ТЕСТЫ АБСТРАКТНОГО МЕТОДА =====


def test_get_total_price_product():
    """Тест метода get_total_price для Product"""
    p = Product("A", "B", 100.0, 5)
    assert p.get_total_price() == 500.0


def test_get_total_price_smartphone():
    """Тест метода get_total_price для Smartphone"""
    phone = Smartphone("iPhone", "A", 50000.0, 2, "A17", "15", "256GB", "Черный")
    assert phone.get_total_price() == 100000.0


def test_get_total_price_lawn_grass():
    """Тест метода get_total_price для LawnGrass"""
    grass = LawnGrass("Газон", "A", 1000.0, 10, "РФ", "7 дней", "Зеленый")
    assert grass.get_total_price() == 10000.0


# ===== ТЕСТЫ МНОЖЕСТВЕННОГО НАСЛЕДОВАНИЯ =====


def test_multiple_inheritance_mro():
    """Проверка метода разрешения порядка (MRO)"""
    mro = Product.__mro__
    # Проверяем, что оба родителя в цепочке
    assert MixinLog in mro
    assert BaseProduct in mro
    assert Product in mro


def test_product_is_instance_of_mixin():
    """Product является экземпляром MixinLog"""
    p = Product("A", "B", 100.0, 1)
    assert isinstance(p, MixinLog)


def test_product_is_instance_of_base():
    """Product является экземпляром BaseProduct"""
    p = Product("A", "B", 100.0, 1)
    assert isinstance(p, BaseProduct)


def test_smartphone_is_instance_of_all():
    """Smartphone является экземпляром всех классов"""
    phone = Smartphone("iPhone", "A", 100000.0, 1, "A17", "15", "256GB", "Черный")
    assert isinstance(phone, MixinLog)
    assert isinstance(phone, BaseProduct)
    assert isinstance(phone, Product)
    assert isinstance(phone, Smartphone)


# ===== ПРОВЕРКА СОВМЕСТИМОСТИ =====


def test_price_property():
    """Тест свойства price"""
    p = Product("A", "B", 100.0, 1)
    assert p.price == 100.0
    p.price = 150.0
    assert p.price == 150.0


def test_price_setter_invalid():
    """Тест сеттера price с невалидным значением"""
    p = Product("A", "B", 100.0, 1)
    p.price = -50
    # Цена не должна измениться
    assert p.price == 100.0


def test_add_same_type():
    """Тест сложения товаров одного типа"""
    p1 = Product("A", "D", 100.0, 5)
    p2 = Product("B", "E", 200.0, 3)
    assert p1 + p2 == 1100.0


def test_add_different_types():
    """Тест ошибки при сложении разных типов"""
    phone = Smartphone("iPhone", "A", 50000.0, 1, "A17", "15", "256GB", "Черный")
    grass = LawnGrass("Газон", "B", 1000.0, 1, "РФ", "7 дней", "Зеленый")
    with pytest.raises(TypeError):
        phone + grass


def test_new_product_classmethod():
    """Тест класс-метода new_product"""
    params = {"name": "Test", "description": "Desc", "price": 100.0, "quantity": 5}
    p = Product.new_product(params)
    assert p.name == "Test"
    assert p.price == 100.0


def test_str_method_product():
    """Тест __str__ для Product"""
    p = Product("Ноутбук", "Описание", 75000.0, 3)
    assert str(p) == "Ноутбук, 75000.0 руб. Остаток: 3 шт."


def test_str_method_smartphone():
    """Тест __str__ для Smartphone"""
    phone = Smartphone("iPhone", "A", 100000.0, 1, "A17", "15", "256GB", "Черный")
    result = str(phone)
    assert "iPhone" in result
    assert "A17" in result


def test_str_method_lawn_grass():
    """Тест __str__ для LawnGrass"""
    grass = LawnGrass("Газон", "A", 1000.0, 1, "РФ", "7 дней", "Зеленый")
    result = str(grass)
    assert "Газон" in result
    assert "РФ" in result
