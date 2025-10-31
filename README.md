# Product and Category Project

## Описание
Этот проект демонстрирует:
- Создание классов `Product` и `Category`.
- **Наследование**: классы `Smartphone` и `LawnGrass` наследуют от `Product`.
- Автоматический подсчет общего числа категорий и товаров через атрибуты класса.
- Загрузку данных из JSON-файла с помощью функции `load_data_from_json`.
- Полный набор юнит-тестов для проверки функциональности.
- Реализацию магических методов `__str__` и `__add__` для удобной работы с товарами.

## Структура проекта
```
homr14/
├── data/
│   └── products.json         # Исходные данные категорий и товаров
├── src/
│   ├── __init__.py           # Пакет src
│   ├── product.py            # Класс Product и его наследники
│   ├── category.py           # Класс Category
│   └── utils.py              # Функция загрузки данных из JSON
├── tests/
│   ├── test_test_utils.py    # тесты 
│   ├── test_product.py       # Тесты для Product
│   ├── test_category.py      # Тесты для Category
│   └── test_inheritance.py   # Тесты для наследования
├── main.py                   # Пример использования и демонстрация загрузки
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

6. Продемонстрируйте загрузку и работу в `main.py`:
   ```bash
   python main.py
   ```

## Класс Product

Файл: `src/product.py`

### Базовый класс для всех товаров

- **Конструктор**
  ```python
  p = Product(name: str, description: str, price: float, quantity: int)
  ```

- **Приватный атрибут цены**
  ```python
  self.__price = price
  ```

- **Геттер `price`**  
  Возвращает текущее значение приватного атрибута `__price`.

- **Сеттер `price`**  
  Проверяет новое значение:
  - Если `value` > 0, присваивает `__price = value`
  - Иначе выводит сообщение об ошибке

- **Класс-метод `new_product`**  
  Создает товар из словаря с ключами: `"name"`, `"description"`, `"price"`, `"quantity"`

- **Магический метод `__str__`**  
  Возвращает строковое представление товара:
  ```
  Название продукта, {price} руб. Остаток: {quantity} шт.
  ```

- **Магический метод `__add__`**  
  Складывает два товара **ОДИНАКОВОГО типа**:
  ```
  результат = (цена1 × количество1) + (цена2 × количество2)
  ```
  **Использует `type() is not type()` для проверки точного совпадения типов**
  - ✅ Product + Product = работает
  - ✅ Smartphone + Smartphone = работает
  - ✅ LawnGrass + LawnGrass = работает
  - ❌ Product + Smartphone = TypeError
  - ❌ Smartphone + LawnGrass = TypeError

## Классы-наследники Product

### Класс Smartphone

**Дополнительные свойства:**
- `efficiency` — производительность (например, "A17")
- `model` — модель (например, "15 Pro")
- `memory` — объем встроенной памяти (например, "512GB")
- `color` — цвет (например, "Черный")

**Пример создания:**
```python
from src.product import Smartphone

phone = Smartphone(
    name="iPhone 15 Pro",
    description="Флагманский смартфон Apple",
    price=120000.0,
    quantity=5,
    efficiency="A17",
    model="15 Pro",
    memory="256GB",
    color="Титановый синий"
)
```

### Класс LawnGrass

**Дополнительные свойства:**
- `country` — страна-производитель (например, "Нидерланды")
- `germination_period` — срок прорастания (например, "7-14 дней")
- `color` — цвет (например, "Темно-зеленый")

**Пример создания:**
```python
from src.product import LawnGrass

grass = LawnGrass(
    name="Газон 'Изумруд'",
    description="Элитная газонная трава",
    price=1500.0,
    quantity=20,
    country="Нидерланды",
    germination_period="7-14 дней",
    color="Темно-зеленый"
)
```

## Класс Category

Файл: `src/category.py`

- **Конструктор**  
  ```python
  cat = Category(name: str, description: str, products: list[Product] | None)
  ```

- **Класс-атрибуты для подсчета**
  - `category_count` — общее число категорий
  - `product_count` — общее число товаров

- **Приватный список товаров**  
  ```python
  self.__products = []
  ```

- **Метод `add_product(product: Product)`**  
  Добавляет товар в категорию. **Использует `isinstance()` для проверки**
  - ✅ Добавляет Product, Smartphone, LawnGrass
  - ❌ Выбрасывает TypeError для строк, чисел, словарей и т.д.

- **Свойство `products`**  
  Возвращает список объектов `Product` категории.

- **Свойство `products_str`**  
  Возвращает строку со списком товаров в формате:
  ```
  Название продукта1, {price1} руб. Остаток: {quantity1} шт.
  Название продукта2, {price2} руб. Остаток: {quantity2} шт.
  ```

- **Магический метод `__str__`**  
  Возвращает строковое представление категории:
  ```
  Название категории, количество продуктов: {сумма_количеств} шт.
  ```

## Утилиты

Файл: `src/utils.py`

- **Функция `load_data_from_json(path: str) -> list[dict]`**  
  Читает JSON-файл по пути и возвращает список словарей с полями:
  - `"category"` — название категории
  - `"name"` — название товара
  - `"description"` — описание товара
  - `"price"` — цена товара
  - `"quantity"` — количество в наличии

  Пример `data/products.json`:
  ```json
  [
    {
      "category": "Electronics",
      "name": "Smartphone",
      "description": "Latest model",
      "price": 500.0,
      "quantity": 10
    }
  ]
  ```

## Демонстрация в main.py

```python
from src.utils import load_data_from_json
from src.product import Product, Smartphone, LawnGrass
from src.category import Category

# Загрузка из JSON
items = load_data_from_json("data/products.json")

# Группировка товаров по категориям
categories: dict[str, Category] = {}
for item in items:
    prod = Product.new_product(item)
    cat_name = item["category"]
    if cat_name not in categories:
        categories[cat_name] = Category(cat_name, f"Category {cat_name}")
    categories[cat_name].add_product(prod)

# Вывод информации
for cat in categories.values():
    print(f"\nКатегория: {cat.name}")
    print(cat.products_str)
    print(f"Итого: {cat}")
```

## Ключевые концепции

### Наследование (Inheritance)
```python
class Smartphone(Product):
    """Класс Smartphone наследует от Product"""
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        # ... остальные свойства
```

### Проверка типов (type() is not type())
```python
def __add__(self, other):
    if type(self) is not type(other):
        raise TypeError("Можно складывать только товары ОДИНАКОВОГО типа")
    return self.price * self.quantity + other.price * other.quantity
```

### Проверка экземпляра (isinstance())
```python
def add_product(self, product):
    if not isinstance(product, Product):
        raise TypeError("Можно добавлять только объекты Product или его наследников")
    self.__products.append(product)
```

## Тестирование и покрытие

Цель — покрытие не менее **75%** кода тестами. **Текущее покрытие: 88%**

Запуск всех тестов:
```bash
pytest
```

Запуск тестов с выводом имён:
```bash
pytest -v
```

Формирование отчета покрытия:
```bash
coverage run -m pytest
coverage report
coverage html
```

Файл `htmlcov/index.html` содержит детальный отчет покрытия.

## Требования к коду

- Соблюдение **PEP8** проверяется с помощью `flake8`
- Максимум **5 ошибок PEP8** допускается
- Использование **type hints** для всех функций и методов
- Полное покрытие тестами не менее **75%**

## Ветки и пул-реквесты

Создавайте новую ветку для каждой фичи:
```bash
git checkout -b feature/your-feature-name
```

После завершения работы — отправьте пул-реквест для обзора.

## Примеры использования

### Создание товаров и категорий
```python
from src.product import Product, Smartphone, LawnGrass
from src.category import Category

# Создание товаров
phone = Smartphone("iPhone 15", "Смартфон", 100000, 5, "A17", "15", "256GB", "Черный")
grass = LawnGrass("Газон", "Трава", 1000, 10, "РФ", "7 дней", "Зеленый")
product = Product("Ноутбук", "Компьютер", 75000, 3)

# Создание категории
cat = Category("Электроника", "Техника и растения")

# Добавление товаров
cat.add_product(phone)
cat.add_product(grass)
cat.add_product(product)

# Вывод информации
print(cat)  # Электроника, количество продуктов: 18 шт.
print(cat.products_str)
```

### Сложение товаров
```python
# Сложение товаров одного типа
phone1 = Smartphone("A", "D", 50000, 2, "A17", "15", "256GB", "Черный")
phone2 = Smartphone("B", "E", 40000, 3, "Snapdragon", "S24", "128GB", "Белый")
total = phone1 + phone2  # 50000*2 + 40000*3 = 220000
print(total)  # 220000.0

# Ошибка при сложении товаров разных типов
try:
    result = phone1 + grass
except TypeError as e:
    print(e)  # Можно складывать только товары ОДИНАКОВОГО типа...
```

### Проверка типов
```python
# isinstance() проверяет наследование
print(isinstance(phone, Product))      # True
print(isinstance(phone, Smartphone))   # True
print(isinstance(phone, LawnGrass))    # False

# type() проверяет точный тип
print(type(phone) is Smartphone)       # True
print(type(phone) is Product)          # False
```

## Автор
Проект создан как учебное задание по объектно-ориентированному программированию на Python.

## Лицензия
MIT
