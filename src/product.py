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
        if type(self) is not type(other):
            raise TypeError(
                f"Можно складывать только товары ОДИНАКОВОГО типа. "
                f"Попытка сложить {type(self).__name__} и {type(other).__name__} невозможно."
            )
        return self.price * self.quantity + other.price * other.quantity


# ===== КЛАССЫ-НАСЛЕДНИКИ =====
class Smartphone(Product):
    """Класс для представления товара 'Смартфон'."""

    def __init__(
        self, name, description, price, quantity, efficiency, model, memory, color
    ):
        """Инициализация смартфона."""
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        """Строковое представление смартфона."""
        base = super().__str__()
        return (
            f"{base}\n"
            f"Производительность: {self.efficiency}, "
            f"Модель: {self.model}, "
            f"Память: {self.memory}, "
            f"Цвет: {self.color}"
        )


class LawnGrass(Product):
    """Класс для представления товара 'Трава газонная'."""

    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ):
        """Инициализация газонной травы."""
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        """Строковое представление газонной травы."""
        base = super().__str__()
        return (
            f"{base}\n"
            f"Страна-производитель: {self.country}, "
            f"Срок прорастания: {self.germination_period}, "
            f"Цвет: {self.color}"
        )


# p = Product("A", "B", 100, 1)
# phone = Smartphone("A", "B", 100, 1, "A17", "15", "256GB", "Черный")
#
# # type() возвращает точный класс объекта
# print(type(p))  # <class 'src.product.Product'>
# print(type(phone))  # <class 'src.smartphone.Smartphone'>
#
# # Сравнение типов
# print(type(p) == type(p))  # True (одинаковые типы)
# print(type(phone) == type(phone))  # True (одинаковые типы)
# print(type(p) == type(phone))  # False (разные типы)
#
# # Это отличается от isinstance (который проверяет наследование)
# print(isinstance(phone, Smartphone))  # True
# print(isinstance(phone, Product))  # True (потому что Smartphone наследует Product)
# print(type(phone) == Smartphone)  # True
# print(type(phone) == Product)  # False (type() не смотрит на наследование)

# # Смартфон + Газонная трава
# phone = Smartphone("iPhone", "A", 100000.0, 1, "A17", "15", "256GB", "Черный")
# grass = LawnGrass("Газон", "B", 1000.0, 1, "РФ", "7 дней", "Зеленый")
#
# try:
#     total = phone + grass
# except TypeError as e:
#     print(e)
#     # TypeError: Можно складывать только товары ОДИНАКОВОГО типа.
#     # Попытка сложить Smartphone и LawnGrass
