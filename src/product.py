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
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        """Геттер для приватного атрибута цены."""
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        """
        Сеттер для приватного атрибута цены.
        Проверяет, что значение положительное.
        """
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

    @classmethod
    def new_product(cls, params: dict):
        """
        Класс-метод для создания товара из словаря params:
        ключи 'name', 'description', 'price', 'quantity'.
        """
        return cls(
            params["name"], params["description"], params["price"], params["quantity"]
        )

    def __str__(self) -> str:
        """Строковое представление товара"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Сложение двух товаров"""
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты класса Product")
        return self.price * self.quantity + other.price * other.quantity


# Тестируем создание объектов
# if __name__ == "__main__":
#     # Простейшая проверка
#
#     # Создание через __init__
#     p1 = Product("Чайник", "Электрический чайник", 1500.0, 3)
#     print(f"{p1.name=}, {p1.description=}, {p1.price=}, {p1.quantity=}")
#
#     # Попытка установки некорректной цены
#     print("\nПроверка сеттера price:")
#     p1.price = -100.0  # должно напечатать предупреждение
#     print(f"Цена осталась: {p1.price}")
#
#     # Создание через класс-метод new_product
#     params = {
#         "name": "Тостер",
#         "description": "Двухслотовый тостер",
#         "price": 2500.0,
#         "quantity": 5,
#     }
#     p2 = Product.new_product(params)
#     print(
#         "\nnew_product создал:",
#         f"{p2.name=}, {p2.description=}, {p2.price=}, {p2.quantity=}",
#     )
#     # Тестирование __str__
#     p1 = Product("Ноутбук", "Игровой ноутбук", 75000.0, 5)
#     p2 = Product("Мышь", "Беспроводная мышь", 1500.0, 20)
#
#     print("Тест __str__ для Product:")
#     print(p1)  # автоматически вызовет __str__
#     print(p2)
#     print("\nПрямой вызов str():")
#     print(str(p1))
#
#     # Тестирование __str__
#     p1 = Product("Ноутбук", "Игровой ноутбук", 100.0, 10)
#     p2 = Product("Мышь", "Беспроводная мышь", 200.0, 2)
#
#     print("Тест __str__ для Product:")
#     print(p1)
#     print(p2)
#
#     print("\nТест __add__ для Product:")
#     total = p1 + p2
#     print(f"Товар A: {p1.name}, цена={p1.price}, количество={p1.quantity}")
#     print(f"Товар B: {p2.name}, цена={p2.price}, количество={p2.quantity}")
#     print(f"Общая стоимость на складе: {total} руб.")
#     print(f"Расчет: {p1.price} × {p1.quantity} + {p2.price} × {p2.quantity} = {total}")
