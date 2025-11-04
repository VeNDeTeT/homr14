from abc import ABC, abstractmethod


class MixinLog:
    """Миксин для логирования создания объектов"""

    def __init__(self, *args, **kwargs):
        """Логирует создание объекта"""
        # НЕ вызываем super().__init__() здесь!
        # Просто логируем
        if hasattr(self, "__dict__"):
            print(f"{self.__class__.__name__}({self.__repr__()})")

    def __repr__(self):
        """Возвращает строковое представление для логирования"""
        attrs = []
        for key, value in self.__dict__.items():
            if not key.startswith("_"):
                if isinstance(value, str):
                    attrs.append(f"'{value}'")
                else:
                    attrs.append(f"{value}")
        return ", ".join(attrs)


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов"""

    @abstractmethod
    def get_total_price(self) -> float:
        """Возвращает общую стоимость товара на складе"""
        pass


class Product(MixinLog, BaseProduct):
    """Класс для представления товара."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
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
        # Логируем ДО вызова super()
        MixinLog.__init__(self)

    @property
    def price(self) -> float:
        """Геттер для цены."""
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        """Сеттер для цены."""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

    @classmethod
    def new_product(cls, params: dict):
        """Создание товара из словаря."""
        return cls(
            params["name"], params["description"], params["price"], params["quantity"]
        )

    def __str__(self):
        """Строковое представление товара."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Сложение товаров одинакового типа."""
        if type(self) is not type(other):
            raise TypeError(
                f"Можно складывать только товары ОДИНАКОВОГО типа. "
                f"Попытка сложить {type(self).__name__} и {type(other).__name__}"
            )
        return self.price * self.quantity + other.price * other.quantity

    def get_total_price(self) -> float:
        """Возвращает общую стоимость товара на складе"""
        return self.price * self.quantity


class Smartphone(Product):
    """Класс для товара 'Смартфон'."""

    def __init__(
        self, name, description, price, quantity, efficiency, model, memory, color
    ):
        """Инициализация смартфона."""
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        super().__init__(name, description, price, quantity)

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
    """Класс для товара 'Трава газонная'."""

    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ):
        """Инициализация газонной травы."""
        self.country = country
        self.germination_period = germination_period
        self.color = color
        super().__init__(name, description, price, quantity)

    def __str__(self):
        """Строковое представление газонной травы."""
        base = super().__str__()
        return (
            f"{base}\n"
            f"Страна-производитель: {self.country}, "
            f"Срок прорастания: {self.germination_period}, "
            f"Цвет: {self.color}"
        )
