# Product and Category Project

## Описание
Этот проект демонстрирует:
- **Создание классов** `Product`, `Smartphone` и `LawnGrass` с наследованием
- **Абстрактное программирование** с использованием `ABC` и `@abstractmethod`
- **Множественное наследование** и **миксины** для логирования
- **Проверка типов** при сложении товаров и добавлении в категории
- **Автоматический подсчет** категорий и товаров через атрибуты класса
- **Загрузка данных** из JSON-файла
- **Полный набор юнит-тестов** с покрытием 85%+

## Структура проекта
```
homr14/
├── data/
│   └── products.json         # Исходные данные категорий и товаров
├── src/
│   ├── __init__.py           # Пакет src
│   ├── product.py            # Классы Product, Smartphone, LawnGrass, BaseProduct, MixinLog
│   ├── category.py           # Класс Category
│   └── utils.py              # Функция загрузки данных из JSON
├── tests/
│   ├── test_product.py       # Тесты для Product
│   ├── test_category.py      # Тесты для Category
│   ├── test_inheritance.py   # Тесты для наследования
│   └── test_abstract.py      # Тесты для абстрактных классов и миксинов
├── main.py                   # Пример использования и демонстрация
├── conftest.py               # Настройка sys.path для pytest
├── requirements.txt          # Зависимости проекта
├── .flake8                   # Настройки flake8
└── README.md                 # Этот файл
```

## Установка и запуск

1. Клонируйте репозиторий и перейдите в каталог проекта:
   ```bash
   git clone https://github.com/username/homr14.git
   cd homr14
   ```

2. Создайте и активируйте виртуальное окружение:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux/macOS
   .\.venv\Scripts\activate    # Windows
   ```

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

4. Запустите тесты:
   ```bash
   pytest
   ```

5. Сформируйте отчет покрытия:
   ```bash
   coverage run -m pytest
   coverage report
   coverage html
   ```

6. Запустите демонстрацию:
   ```bash
   python main.py
   ```

---

## Ключевые компоненты

### 1. Абстрактный класс BaseProduct

```python
from abc import ABC, abstractmethod

class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов"""
    
    @abstractmethod
    def get_total_price(self) -> float:
        """Возвращает общую стоимость товара на складе"""
        pass
```

- Определяет интерфейс, который должны реализовать все продукты
- Требует реализации метода `get_total_price()`
- Нельзя создать экземпляр напрямую

### 2. Миксин MixinLog

```python
class MixinLog:
    """Миксин для логирования создания объектов"""
    
    def __init__(self, *args, **kwargs):
        """Логирует создание объекта"""
        print(f"{self.__class__.__name__}({self.__repr__()})")
    
    def __repr__(self):
        """Возвращает строковое представление для логирования"""
        # Возвращает параметры объекта
```

- Автоматически логирует создание каждого объекта
- Реализует `__repr__` для красивого вывода
- Используется множественное наследование: `Product(MixinLog, BaseProduct)`

### 3. Класс Product

```python
class Product(MixinLog, BaseProduct):
    """Класс для представления товара."""
    
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Инициализация товара"""
        self.name = name
        self.description = description
        self.__price = price  # Приватный атрибут
        self.quantity = quantity
        MixinLog.__init__(self)  # Логирование
    
    @property
    def price(self) -> float:
        """Геттер для цены"""
        return self.__price
    
    @price.setter
    def price(self, value: float) -> None:
        """Сеттер с проверкой"""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value
    
    def __add__(self, other):
        """Сложение товаров одинакового типа"""
        if type(self) is not type(other):  # Использование type()
            raise TypeError(f"Можно складывать только товары ОДИНАКОВОГО типа...")
        return self.price * self.quantity + other.price * other.quantity
    
    def get_total_price(self) -> float:
        """Реализация абстрактного метода"""
        return self.price * self.quantity
```

**Особенности:**
- ✅ Множественное наследование: `MixinLog` + `BaseProduct`
- ✅ Приватный атрибут `__price` с геттером/сеттером
- ✅ Магический метод `__add__` с проверкой типов через `type() is not type()`
- ✅ Реализует абстрактный метод `get_total_price()`
- ✅ Логирование при создании через `MixinLog`

### 4. Классы-наследники: Smartphone и LawnGrass

#### Smartphone
```python
class Smartphone(Product):
    """Класс для товара 'Смартфон'"""
    
    def __init__(self, name, description, price, quantity, 
                 efficiency, model, memory, color):
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        super().__init__(name, description, price, quantity)
```

**Дополнительные свойства:**
- `efficiency` — производительность (например, "A17")
- `model` — модель (например, "15 Pro")
- `memory` — объем встроенной памяти (например, "256GB")
- `color` — цвет

#### LawnGrass
```python
class LawnGrass(Product):
    """Класс для товара 'Трава газонная'"""
    
    def __init__(self, name, description, price, quantity, 
                 country, germination_period, color):
        self.country = country
        self.germination_period = germination_period
        self.color = color
        super().__init__(name, description, price, quantity)
```

**Дополнительные свойства:**
- `country` — страна-производитель (например, "Нидерланды")
- `germination_period` — срок прорастания (например, "7-14 дней")
- `color` — цвет

### 5. Класс Category

```python
class Category:
    """Класс для представления категории товаров"""
    
    category_count = 0
    product_count = 0
    
    def add_product(self, product):
        """Добавляет товар в категорию"""
        if not isinstance(product, Product):  # Использование isinstance()
            raise TypeError(f"Можно добавлять только объекты Product...")
        self.__products.append(product)
        Category.product_count += 1
```

**Особенности:**
- ✅ Проверка типов через `isinstance(product, Product)`
- ✅ Разрешены все наследники Product (Product, Smartphone, LawnGrass)
- ✅ Запрещены другие типы (строки, числа, словари и т.д.)
- ✅ Автоматический подсчет товаров

---

## Примеры использования

### Создание объектов (с логированием)

```python
from src.product import Product, Smartphone, LawnGrass

# При создании будет выведено в консоль:
product = Product("Ноутбук", "Игровой", 75000.0, 3)
# Product('Ноутбук', 'Игровой', 75000.0, 3)

phone = Smartphone("iPhone 15", "Смартфон", 100000.0, 5, 
                   "A17", "15 Pro", "256GB", "Черный")
# Smartphone('A17', '15 Pro', '256GB', 'Черный', 'iPhone 15', 'Смартфон', 100000.0, 5)
```

### Сложение товаров одного типа

```python
# ✅ Правильно: сложение смартфонов
phone1 = Smartphone("iPhone", "A", 50000.0, 2, "A17", "15", "256GB", "Черный")
phone2 = Smartphone("Samsung", "B", 40000.0, 3, "Snapdragon", "S24", "128GB", "Белый")
total = phone1 + phone2  # 50000*2 + 40000*3 = 220000

# ❌ Ошибка: сложение разных типов
try:
    result = phone1 + product
except TypeError as e:
    print(e)  # TypeError: Можно складывать только товары ОДИНАКОВОГО типа...
```

### Добавление товаров в категорию

```python
from src.category import Category

cat = Category("Электроника", "Техника")

# ✅ Правильно: добавляем любые Product и его наследников
cat.add_product(product)
cat.add_product(phone)
grass = LawnGrass("Газон", "Трава", 1000.0, 10, "РФ", "7 дней", "Зеленый")
cat.add_product(grass)

# ❌ Ошибка: добавляем что-то другое
try:
    cat.add_product("Not a product")
except TypeError as e:
    print(e)  # TypeError: Можно добавлять только объекты Product...
```

---

## Тестирование и покрытие

**Текущее покрытие: 85%+**

Запуск всех тестов:
```bash
pytest tests/ -v
```

Запуск тестов конкретного модуля:
```bash
pytest tests/test_abstract.py -v
pytest tests/test_category.py -v
```

Формирование подробного отчета:
```bash
coverage run -m pytest
coverage report -m
coverage html  # открыть htmlcov/index.html в браузере
```

---

## Требования к коду

- ✅ **PEP8** — проверка через `flake8 src/`
- ✅ **Type hints** — все функции и методы типизированы
- ✅ **Тесты** — минимум 75% покрытия (текущее: 85%+)
- ✅ **ABC и abstractmethod** — правильное использование абстрактных классов
- ✅ **Миксины** — реализация множественного наследования
- ✅ **type() vs isinstance()** — использование где требуется

---

## Ветки и пул-реквесты

Создание новой ветки для каждой фичи:
```bash
git checkout -b feature/your-feature-name
```

Проверка текущей ветки:
```bash
git branch
```

Отправка на сервер:
```bash
git push origin feature/your-feature-name
```

---

## Автор
Проект создан как учебное задание по объектно-ориентированному программированию на Python с использованием:
- Наследования и полиморфизма
- Абстрактных классов (ABC)
- Миксинов и множественного наследования
- Проверки типов (type(), isinstance())
- Магических методов (`__add__`, `__str__`, `__repr__`)
- Unit-тестирования (pytest)

## Лицензия
MIT
