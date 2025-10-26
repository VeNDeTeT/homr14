# Product and Category Project

## Описание
Этот проект демонстрирует:
- Создание классов `Product` и `Category`.
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
│   ├── product.py            # Класс Product
│   ├── category.py           # Класс Category
│   └── utils.py              # Функция загрузки данных из JSON
├── tests/
│   ├── test_product.py       # Тесты для Product
│   └── test_category.py      # Тесты для Category
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
   .\.venv\Scripts\activate  # Windows
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

- **Конструктор**  
  ```python
  p = Product(name: str, description: str, price: float, quantity: int)
  ```
- **Приватный атрибут цены**  
  ```python
  self.__price = price
  ```
- **Геттер `price`**  
  Метод возвращает текущее значение приватного атрибута `__price`.
  ```python
  @property
  def price(self) -> float:
      return self.__price
  ```
- **Сеттер `price`**  
  Метод проверяет новое значение:
  - Если `value` > 0, присваивает `__price = value`.
  - Иначе выводит сообщение:
    ```
    Цена не должна быть нулевая или отрицательная
    ```
  И не меняет текущее значение.
  ```python
  @price.setter
  def price(self, value: float) -> None:
      if value <= 0:
          print("Цена не должна быть нулевая или отрицательная")
      else:
          self.__price = value
  ```
- **Класс-метод `new_product`**  
  Создает товар из словаря с ключами:
  - `"name"`
  - `"description"`
  - `"price"`
  - `"quantity"`
  ```python
  @classmethod
  def new_product(cls, params: dict) -> Product:
      return cls(
          params["name"],
          params["description"],
          params["price"],
          params["quantity"]
      )
  ```
- **Магический метод `__str__`**  
  Возвращает строковое представление товара в формате:
  ```
  Название продукта, {price} руб. Остаток: {quantity} шт.
  ```
  Пример:
  ```python
  p = Product("Ноутбук", "Игровой", 75000.0, 5)
  print(p)  # "Ноутбук, 75000.0 руб. Остаток: 5 шт."
  ```
- **Магический метод `__add__`**  
  Складывает два товара и возвращает общую стоимость на складе:
  ```
  результат = (цена1 × количество1) + (цена2 × количество2)
  ```
  Пример:
  ```python
  p1 = Product("A", "D", 100.0, 10)
  p2 = Product("B", "D", 50.0, 2)
  total = p1 + p2  # 100*10 + 50*2 = 1100
  ```

## Класс Category

Файл: `src/category.py`

- **Конструктор**  
  ```python
  cat = Category(name: str, description: str, products: list[Product] | None)
  ```
- **Класс-атрибуты для подсчета**
  ```python
  category_count = 0  # Общее число категорий
  product_count = 0   # Общее число товаров
  ```
- **Приватный список товаров**  
  ```python
  self.__products = []
  ```
- **Метод `add_product(product: Product)`**  
  Добавляет товар в категорию и увеличивает счетчик `Category.product_count`.
  ```python
  cat = Category("Техника", "Электроника")
  p = Product("Монитор", "4K", 500.0, 3)
  cat.add_product(p)
  ```
- **Свойство `products`**  
  Возвращает список объектов `Product` категории.
  ```python
  for product in cat.products:
      print(product.name)
  ```
- **Свойство `products_str`**  
  Возвращает строку со списком товаров в формате:
  ```
  Название продукта1, {price1} руб. Остаток: {quantity1} шт.
  Название продукта2, {price2} руб. Остаток: {quantity2} шт.
  ```
  Пример:
  ```python
  print(cat.products_str)
  ```
- **Магический метод `__str__`**  
  Возвращает строковое представление категории:
  ```
  Название категории, количество продуктов: {сумма_количеств} шт.
  ```
  Пример:
  ```python
  cat = Category("Электроника", "Техника", [p1, p2, p3])
  print(cat)  # "Электроника, количество продуктов: 25 шт."
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
    },
    {
      "category": "Home",
      "name": "Vacuum Cleaner",
      "description": "Powerful suction",
      "price": 150.0,
      "quantity": 5
    }
  ]
  ```

## Демонстрация в main.py

```python
from src.utils import load_data_from_json
from src.product import Product
from src.category import Category

items = load_data_from_json("data/products.json")

categories: dict[str, Category] = {}
for item in items:
    prod = Product.new_product(item)
    cat_name = item["category"]
    if cat_name not in categories:
        categories[cat_name] = Category(cat_name, f"Category {cat_name}")
    categories[cat_name].add_product(prod)

for cat in categories.values():
    print(f"\nКатегория: {cat.name}")
    print(cat.products_str)
    print(f"Итого: {cat}")
```

## Тестирование и покрытие

Цель — покрытие не менее **75%** кода тестами.

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

## Автор
Проект создан как учебное задание по объектно-ориентированному программированию на Python.
