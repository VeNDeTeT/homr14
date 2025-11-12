from src.product import Product, LawnGrass, Smartphone
from src.category import Category
from src.utils import load_data_from_json


def main():
    """Загрузка данных из JSON и демонстрация работы классов"""

    # ===== ЧАСТЬ 1: Загрузка данных из JSON =====
    print("=== Загрузка данных из JSON ===")
    json_path = "data/products.json"
    try:
        items = load_data_from_json(json_path)
        print(f"✓ Успешно загружено {len(items)} товаров из JSON\n")
    except FileNotFoundError as e:
        print(f"✗ Ошибка: {e}\n")

    # ===== ЧАСТЬ 2: Создание объектов вручную =====
    print("=== Создание объектов вручную ===")

    # Смартфоны
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый, 200MP",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )
    smartphone2 = Smartphone(
        "Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space"
    )
    smartphone3 = Smartphone(
        "Xiaomi Redmi Note 11",
        "1024GB, Синий",
        31000.0,
        14,
        90.3,
        "Note 11",
        1024,
        "Синий",
    )

    # Газонная трава
    grass1 = LawnGrass(
        "Газонная трава", "Элитная трава", 500.0, 20, "Россия", "7 дней", "Зеленый"
    )
    grass2 = LawnGrass(
        "Газонная трава 2",
        "Выносливая трава",
        450.0,
        15,
        "США",
        "5 дней",
        "Темно-зеленый",
    )

    # ===== ЧАСТЬ 3: Работа с категориями =====
    print("=== Работа с категориями ===\n")

    category_smartphones = Category(
        "Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2]
    )
    category_grass = Category(
        "Газонная трава", "Различные виды газонной травы", [grass1, grass2]
    )

    # Добавляем ещё товар в категорию смартфонов
    category_smartphones.add_product(smartphone3)

    print(f"Категория: {category_smartphones.name}")
    print(f"Товаров: {len(category_smartphones.products)}")
    print(f"Средняя цена: {category_smartphones.average_price():.2f} руб.\n")

    print(f"Категория: {category_grass.name}")
    print(f"Товаров: {len(category_grass.products)}")
    print(f"Средняя цена: {category_grass.average_price():.2f} руб.\n")

    # ===== ЧАСТЬ 4: Тестирование сложения товаров =====
    print("=== Тестирование сложения товаров ===")

    sum_smartphones = smartphone1 + smartphone2
    print(f"Сумма двух смартфонов: {sum_smartphones} руб.")

    sum_grass = grass1 + grass2
    print(f"Сумма двух газонов: {sum_grass} руб.")

    # Попытка сложить разные типы
    try:
        smartphone1 + grass1
    except TypeError as e:
        print(f"✓ Ошибка при сложении разных типов: {e}\n")

    # ===== ЧАСТЬ 5: Проверка добавления в категорию =====
    print("=== Проверка добавления в категорию ===")

    try:
        category_smartphones.add_product("Это не товар")
    except TypeError as e:
        print(f"✓ Ошибка при добавлении строки: {e}\n")

    # ===== ЧАСТЬ 6: Общая статистика =====
    print("=== Общая статистика ===")
    print(f"Всего категорий: {Category.category_count}")
    print(f"Всего товаров: {Category.product_count}")

    # ===== ЧАСТЬ 7: Демонстрация ValueError при quantity=0 =====
    print("\n=== Проверка ValueError при quantity=0 ===")
    try:
        Product("Товар с нулевым количеством", "Описание", 100.0, 0)
    except ValueError as e:
        print(f"✓ Ошибка при создании товара с quantity=0: {e}")


if __name__ == "__main__":
    main()
