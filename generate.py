import os
import csv
import random
import string
from datetime import datetime

# Настройки генерации
NUM_SHOPS = 5  # Количество магазинов
NUM_CASHES = 3  # Количество касс в каждом магазине
NUM_DOCS = 100   # Количество чеков в каждой кассе
NUM_ITEMS = 5   # Количество товаров в чеке

# Категории товаров
CATEGORIES = [
    "бытовая химия",
    "текстиль",
    "посуда",
    "продукты питания",
    "товары для дома",
    "канцелярия"
]

# Товары
ITEMS = [
    "стиральный порошок",
    "полотенце",
    "сковорода",
    "молоко",
    "утюг",
    "ручка"
]


# Создаем директорию для выгрузок
os.makedirs('data', exist_ok=True)

def generate_doc_id():
    """Генерация уникального ID чека"""
    return f"DOC-{datetime.now().strftime('%Y%m%d%H%M%S')}-{''.join(random.choices(string.digits, k=4))}"

def generate_random_price():
    """Генерация случайной цены"""
    return round(random.uniform(50, 5000), 2)

def generate_random_discount(price):
    """Генерация случайной скидки"""
    return round(price * random.uniform(0, 0.3), 2)

def generate_csv(shop_num, cash_num):
    """Генерация CSV файла для конкретной кассы"""
    filename = f"data/{shop_num}_{cash_num}.csv"
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['doc_id', 'item', 'category', 'amount', 'price', 'discount'])
        
        for _ in range(NUM_DOCS):
            doc_id = generate_doc_id()
            for _ in range(random.randint(1, NUM_ITEMS)):
                item = random.choice(ITEMS)
                category = random.choice(CATEGORIES)
                amount = random.randint(1, 5)
                price = generate_random_price()
                discount = generate_random_discount(price)
                writer.writerow([doc_id, item, category, amount, price, discount])

# Генерируем выгрузки для всех магазинов и касс
for shop in range(1, NUM_SHOPS + 1):
    for cash in range(1, NUM_CASHES + 1):
        generate_csv(shop, cash)