class Product:
    """Класс для представления товара."""

    #
    name: str
    description: str
    price: int
    quantity: int

    def __init__(self, name, description, price, quantity):
        """
        Инициализация товара.

        :param name: Название товара
        :param description: Описание товара
        :param price: Цена товара
        :param quantity: Количество в наличии
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


# Тестируем создание объектов
if __name__ == "__main__":
    # Создаем товары
    product1 = Product("Смартфон", "Высокотехнологичный смартфон", 50000.0, 10)
    product2 = Product("Ноутбук", "Производительный ноутбук для работы", 80000.0, 5)

    print(
        f"Товар 1: {product1.name}, цена: {product1.price}, количество: {product1.quantity}"
    )
    print(
        f"Товар 2: {product2.name}, цена: {product2.price}, количество: {product2.quantity}"
    )
