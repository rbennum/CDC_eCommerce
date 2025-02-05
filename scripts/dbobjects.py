from collections import namedtuple

Product = namedtuple(
    "Product", 
    [
        "product_id", 
        "name", 
        "category", 
        "price", 
        "stock", 
        "created_at",
    ]
)

Customer = namedtuple(
    "Customer",
    [
        "customer_id",
        "name",
        "email",
        "created_at",
    ]
)