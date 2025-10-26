from src.product import Product


class Category:
    """Класс для представления категории товаров."""

    # Класс-атрибуты для подсчёта категорий и товаров
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list = None):
        """
        Инициализация категории.

        :param name: Название категории
        :param description: Описание категории
        :param products: Список объектов Product (по умолчанию None)
        """
        self.name = name
        self.description = description
        self.__products = []  # приватный список товаров

        Category.category_count += 1

        # Добавляем переданные продукты через метод add_product
        if products:
            for prod in products:
                self.add_product(prod)

    def add_product(self, product: Product) -> None:
        """
        Добавляет объект Product в категорию.

        :param product: экземпляр Product
        :raises TypeError: если передан не Product
        """
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product")
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> list:
        """
        Геттер для получения списка объектов Product.
        """
        return self.__products

    @property
    def products_str(self) -> str:
        """
        Геттер для получения списка товаров в формате строк.

        :return: Строка, где каждый продукт в формате:
                 "Название продукта, {price} руб. Остаток: {quantity} шт."
        """
        lines = []
        for prod in self.__products:
            lines.append(f"{prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт.")
        return "\n".join(lines)

    def __str__(self) -> str:
        """Строковое представление категории"""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."


if __name__ == "__main__":
    # Сброс счётчиков
    Category.category_count = 0
    Category.product_count = 0

    # Создание товаров
    p1 = Product("Товар1", "Описание1", 10.0, 1)
    p2 = Product("Товар2", "Описание2", 20.0, 2)

    # Создание категории и добавление товаров
    cat = Category("Тест", "Проверка")
    cat.add_product(p1)
    cat.add_product(p2)

    # Проверки с выводом
    print(f"Ожидаем категорий: 1, получено: {Category.category_count}")
    print(f"Ожидаем товаров: 2, получено: {Category.product_count}")

    expected = "Товар1, 10.0 руб. Остаток: 1 шт.\n" "Товар2, 20.0 руб. Остаток: 2 шт."
    print("\nВывод геттера products:")
    print(cat.products)
    print("\nОжидаемый вывод:")
    print(expected)
