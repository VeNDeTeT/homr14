import json
from pathlib import Path
from src.product import Product
from src.category import Category

def load_data_from_json(json_path: str) -> list[Category]:
    """
    Читает JSON-файл по указанному пути, создаёт объекты Product и Category.
    Ожидаемый формат JSON:
    [
      {
        "name": "CategoryName",
        "description": "Category description",
        "products": [
          {
            "name": "Product1",
            "description": "Desc1",
            "price": 10.5,
            "quantity": 3
          },
          ...
        ]
      },
      ...
    ]
    """
    path = Path(json_path)
    if not path.exists():
        raise FileNotFoundError(f"Файл не найден: {json_path}")

    with path.open(encoding="utf-8") as f:
        data = json.load(f)

    categories: list[Category] = []
    # Сбросим счётчики перед загрузкой
    Category.category_count = 0
    Category.product_count = 0

    for cat_dict in data:
        products = []
        for prod_dict in cat_dict.get("products", []):
            product = Product(
                name=prod_dict["name"],
                description=prod_dict["description"],
                price=float(prod_dict["price"]),
                quantity=int(prod_dict["quantity"])
            )
            products.append(product)

        category = Category(
            name=cat_dict["name"],
            description=cat_dict["description"],
            products=products
        )
        categories.append(category)

    return categories
