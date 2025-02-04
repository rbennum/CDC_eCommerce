import psycopg
import random
from faker import Faker

fake = Faker()

CATEGORIES = [
    "Books",
    "Movies",
    "Music",
    "Games",
    "Electronics",
    "Computers",
    "Home",
    "Garden",
    "Tools",
    "Grocery",
    "Health",
    "Beauty",
    "Toys",
    "Kids",
    "Baby",
    "Clothing",
    "Shoes",
    "Jewelery",
    "Sports",
    "Outdoors",
    "Automotive",
    "Industrial"
]

MATERIALS = [
    "Steel",
    "Wooden",
    "Concrete",
    "Plastic",
    "Cotton",
    "Granite",
    "Rubber",
    "Metal",
    "Soft",
    "Fresh",
    "Frozen"
]

PRODUCT_DATA = {
    'material': MATERIALS,
    'product': [
        "Chair",
        "Car",
        "Computer",
        "Keyboard",
        "Mouse",
        "Bike",
        "Ball",
        "Gloves",
        "Pants",
        "Shirt",
        "Table",
        "Shoes",
        "Hat",
        "Towels",
        "Soap",
        "Tuna",
        "Chicken",
        "Fish",
        "Cheese",
        "Bacon",
        "Pizza",
        "Salad",
        "Sausages",
        "Chips"
    ],
    'adjective': [
        "Small",
        "Ergonomic",
        "Rustic",
        "Intelligent",
        "Gorgeous",
        "Incredible",
        "Fantastic",
        "Practical",
        "Sleek",
        "Awesome",
        "Generic",
        "Handcrafted",
        "Handmade",
        "Licensed",
        "Refined",
        "Unbranded",
        "Tasty",
        "New",
        "Gently Used",
        "Used",
        "For repair"
    ]
}

def __generateProductName():
    product = random.choice(PRODUCT_DATA["product"])
    adjective = random.choice(PRODUCT_DATA["adjective"])
    material = random.choice(PRODUCT_DATA["material"])
    return " ".join([adjective, material, product])

def generate_product():
    name = __generateProductName()
    category = random.choice(CATEGORIES)
    price = random.randint(100, 9_999_999)
    stock = random.randint(2, 800)

    with psycopg.connect("host=localhost dbname=ecomm_db user=postgres password=postgres port=5432") as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                    INSERT INTO products (name, category, price, stock) 
                    VALUES (%s, %s, %s, %s)
                """, 
                (name, category, price, stock),
            )
            conn.commit()
