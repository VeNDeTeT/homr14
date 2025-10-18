from src.product import Product

class Category:
    """Класс для представления категории товаров."""
    name: str
    description: str
    products: list
    # Атрибуты класса для подсчета общего количества категорий и товаров
    category_count = 0
    product_count = 0



    def __init__(self, name, description, products=None):

        """
         Инициализация категории.

         :param name: Название категории
         :param description: Описание категории
         :param products: Список товаров в категории
         """
        self.name = name
        self.description = description
        self.products = products if products is not None else []

        # Увеличиваем счетчик категорий при создании новой категории
        Category.category_count += 1

        # Увеличиваем счетчик товаров на количество товаров в этой категории
        Category.product_count += len(self.products)


# Тестируем создание объектов
if __name__ == "__main__":
    product1 = Product("Смартфон", "Высокотехнологичный смартфон", 50000.0, 10)
    product2 = Product("Ноутбук", "Производительный ноутбук для работы", 80000.0, 5)

    print(f"Товар 1: {product1.name}, цена: {product1.price}, количество: {product1.quantity}")
    print(f"Товар 2: {product2.name}, цена: {product2.price}, количество: {product2.quantity}")

    # Создаем категории
    category1 = Category("Электроника", "Категория электронных устройств", [product1, product2])
    category2 = Category("Бытовая техника", "Категория бытовой техники", [])

    print(f"\nКатегория 1: {category1.name}, товаров: {len(category1.products)}")
    print(f"Категория 2: {category2.name}, товаров: {len(category2.products)}")

    print(f"\nВсего категорий: {Category.category_count}")
    print(f"Всего товаров: {Category.product_count}")