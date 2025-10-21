from src.product import Product
from src.category import Category
from src.utils import load_data_from_json


def main():
    """Загрузка данных из JSON и демонстрация работы классов"""
    # Загрузка из JSON
    json_path = "data/products.json"
    try:
        categories = load_data_from_json(json_path)
        print("=== Данные из JSON ===")
        for cat in categories:
            print(f"{cat.name}: {len(cat.products)} товаров")
    except FileNotFoundError as e:
        print(f"Ошибка: {e}")

    # Демонстрация создания объектов вручную
    print("\n=== Создание объектов вручную ===")
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(f"Категория: {category1.name}")
    print(f"Описание: {category1.description}")
    print(f"Количество товаров: {len(category1.products)}")

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром",
        [product4],
    )

    print(f"\nКатегория: {category2.name}")
    print(f"Количество товаров: {len(category2.products)}")

    print(f"\nВсего категорий: {Category.category_count}")
    print(f"Всего товаров: {Category.product_count}")


if __name__ == "__main__":  # pragma: no cover
    main()
