# Text-Processing-in-Python

Есть вот такой вот список покупок

purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]
    item — название товара,
    category — категория товара,
    price — цена за единицу товара,
    quantity — количество единиц, купленных за один раз.
    Вам нужно реализовать несколько функций для анализа данных:

Реализованны следующие функии
    total_revenue(purchases): Рассчитанна общая выручка 
    items_by_category(purchases): Возвращает словарь, где ключ — категория, а значение — список уникальных товаров в этой категории.
    expensive_purchases(purchases, min_price): Выводит все покупки, где цена товара больше или равна min_price.
    average_price_by_category(purchases): Рассчитывает среднюю цену товаров по каждой категории.
    most_frequent_category(purchases): Возвращает категорию, в которой куплено больше всего единиц товаров (учитывайте поле quantity).