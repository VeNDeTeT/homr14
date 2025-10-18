import pytest
from src.product import Product
from src.category import Category


@pytest.fixture
def reset_counters():
    """Фикстура для сброса счетчиков перед каждым тестом"""
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def sample_products():
    """Фикстура с образцами продуктов"""
    return [
        Product("Apple", "Fresh red apple", 1.5, 10),
        Product("Banana", "Yellow banana", 1.0, 5),
        Product("Orange", "Juicy orange", 2.0, 8)
    ]


def test_category_initialization(reset_counters, sample_products):
    """Тест инициализации категории"""
    category = Category("Fruits", "Fresh fruits", sample_products)
    assert category.name == "Fruits"
    assert category.description == "Fresh fruits"
    assert len(category.products) == 3


def test_category_empty_products_list(reset_counters):
    """Тест категории с пустым списком продуктов"""
    category = Category("Empty", "No products", [])
    assert len(category.products) == 0
    assert Category.product_count == 0


def test_single_category_count(reset_counters, sample_products):
    """Тест подсчета одной категории"""
    category = Category("Electronics", "Electronic devices", sample_products)
    assert Category.category_count == 1


def test_multiple_categories_count(reset_counters):
    """Тест подсчета нескольких категорий"""
    p1 = Product("Book", "Fiction", 15.0, 5)
    p2 = Product("Pen", "Blue pen", 2.0, 20)
    p3 = Product("Notebook", "A4 notebook", 5.0, 10)

    cat1 = Category("Books", "Literature", [p1])
    cat2 = Category("Stationery", "Office supplies", [p2, p3])

    assert Category.category_count == 2


def test_product_count_single_category(reset_counters, sample_products):
    """Тест подсчета продуктов в одной категории"""
    category = Category("Fruits", "Fresh fruits", sample_products)
    assert Category.product_count == 3


def test_product_count_multiple_categories(reset_counters):
    """Тест подсчета продуктов в нескольких категориях"""
    p1 = Product("Apple", "Red apple", 1.5, 10)
    p2 = Product("Banana", "Yellow", 1.0, 5)
    cat1 = Category("Fruits", "Fresh", [p1, p2])

    p3 = Product("Carrot", "Orange", 0.8, 7)
    p4 = Product("Potato", "Brown", 0.5, 15)
    p5 = Product("Onion", "Red", 0.6, 12)
    cat2 = Category("Vegetables", "Fresh veg", [p3, p4, p5])

    assert Category.product_count == 5


def test_category_products_list_content(reset_counters):
    """Тест содержимого списка продуктов категории"""
    p1 = Product("Laptop", "Gaming", 1500.0, 2)
    p2 = Product("Mouse", "Wireless", 50.0, 10)

    category = Category("Tech", "Technology", [p1, p2])

    assert category.products[0].name == "Laptop"
    assert category.products[1].name == "Mouse"
    assert len(category.products) == 2


def test_category_with_single_product(reset_counters):
    """Тест категории с одним продуктом"""
    p = Product("Monitor", "4K Monitor", 500.0, 3)
    category = Category("Displays", "Monitors", [p])

    assert Category.category_count == 1
    assert Category.product_count == 1
    assert len(category.products) == 1


def test_categories_accumulate_counts(reset_counters):
    """Тест накопления счетчиков при создании категорий"""
    p1 = Product("Item1", "Desc1", 10.0, 1)
    cat1 = Category("Cat1", "First", [p1])

    assert Category.category_count == 1
    assert Category.product_count == 1

    p2 = Product("Item2", "Desc2", 20.0, 2)
    p3 = Product("Item3", "Desc3", 30.0, 3)
    cat2 = Category("Cat2", "Second", [p2, p3])

    assert Category.category_count == 2
    assert Category.product_count == 3


def test_category_attributes_types(reset_counters, sample_products):
    """Тест типов атрибутов категории"""
    category = Category("Test", "Test category", sample_products)

    assert isinstance(category.name, str)
    assert isinstance(category.description, str)
    assert isinstance(category.products, list)
    assert isinstance(Category.category_count, int)
    assert isinstance(Category.product_count, int)
