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

## Установка и Запуск

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/username/homr14.git
   cd homr14
   ```

2. Создайте и активируйте виртуальное окружение (Windows):
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\activate
   ```

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

4. Запуск тестов:
   ```bash
   pytest
   ```

5. Демонстрация загрузки из JSON:
   ```bash
   python main.py
   ```

## Кодирование и Стиль

- Соблюдены рекомендации PEP8 с помощью flake8.
- Не более 5 ошибок PEP8 при проверке.

## Покрытие тестами

Покрытие кода тестами более 75%. Для отчета о покрытии:
```bash
coverage run -m pytest
coverage report
coverage html
```
