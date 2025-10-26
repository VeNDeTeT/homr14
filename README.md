# Product and Category Project

## Описание
Этот проект демонстрирует:
- Создание классов `Product` и `Category`.
- Автоматический подсчет общего числа категорий и товаров через атрибуты класса.
- Загрузку данных из JSON-файла с помощью функции `load_data_from_json`.
- Полный набор юнит-тестов для проверки функциональности.

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

- **Конструктор**  
  ```python
  p = Product(name: str, description: str, price: float, quantity: int)
  ```
- **Приватный атрибут цены**  
  ```python
  self.__price = price
  ```
- **Геттер и сеттер `price`**  
  ```python
  @property
  def price(self) -> float: ...
  
  @price.setter
  def price(self, value: float): ...
  ```
  При попытке задать значение ≤ 0 выводится предупреждение и цена не меняется.
- **Класс-метод `new_product`**  
  ```python
  @classmethod
  def new_product(cls, params: dict) -> Product
  ```
  Создает товар из словаря с ключами `"name"`, `"description"`, `"price"`, `"quantity"`.

## Класс Category

Файл: `src/category.py`

- **Конструктор**  
  ```python
  cat = Category(name: str, description: str, products: list[Product] | None)
  ```
- **Приватный список**  
  ```python
  self.__products = []
  ```
- **Метод `add_product(product: Product)`**  
  Добавляет товар и увеличивает `Category.product_count`.
- **Свойство `products`**  
  Возвращает список объектов `Product`.
- **Свойство `products_str`**  
  Возвращает строку со списком товаров в формате:  
  ```
  Название продукта, {price} руб. Остаток: {quantity} шт.
  ```

## Утилиты

Файл: `src/utils.py`

Функция `load_data_from_json(path: str) -> list[dict]`:

- Читает JSON-файл по пути.
- Возвращает список словарей с полями:
  - `"category"`
  - `"name"`
  - `"description"`
  - `"price"`
  - `"quantity"`

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

## Демонстрация в `main.py`

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
```

## Стиль и качество кода

- Соблюдение PEP8 проверяется с помощью flake8.
- Максимум 5 ошибок PEP8 допускается.

## Тестирование и покрытие

Цель — покрытие не менее 75%.  
Отчёт покрытия:
```bash
coverage run -m pytest
coverage report
coverage html
```

## Ветки и пул-реквесты

Создавайте новую ветку для фич:
```bash
git checkout -b feature/your-feature
```
После завершения — отправьте пул-реквест наставнику.