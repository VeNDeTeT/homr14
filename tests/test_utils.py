import pytest
import json
from src.utils import load_data_from_json
from src.category import Category


def test_load_data_from_json_success(tmp_path):
    """Тест успешной загрузки данных из JSON"""
    # Создаём временный JSON файл
    test_data = [
        {
            "name": "Электроника",
            "description": "Товары электроники",
            "products": [
                {
                    "name": "Телефон",
                    "description": "Смартфон",
                    "price": 50000,
                    "quantity": 10,
                }
            ],
        }
    ]

    json_file = tmp_path / "test_products.json"
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(test_data, f, ensure_ascii=False)

    # Сброс счётчиков
    Category.category_count = 0
    Category.product_count = 0

    # Тест загрузки
    categories = load_data_from_json(str(json_file))

    assert len(categories) == 1
    assert categories[0].name == "Электроника"
    assert len(categories[0].products) == 1
    assert categories[0].products[0].name == "Телефон"


def test_load_data_from_json_file_not_found():
    """Тест обработки несуществующего файла"""
    with pytest.raises(FileNotFoundError):
        load_data_from_json("несуществующий_файл.json")


def test_load_data_from_json_empty_file(tmp_path):
    """Тест загрузки пустого JSON файла"""
    json_file = tmp_path / "empty.json"
    with open(json_file, "w") as f:
        json.dump([], f)

    Category.category_count = 0
    Category.product_count = 0

    categories = load_data_from_json(str(json_file))
    assert len(categories) == 0
