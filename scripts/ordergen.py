import psycopg
import random
from .dbobjects import Product, Customer

"""
Steps to create an order:
- find which customer to create an order (randomize)
- let n be a random integer, find n products from the table
- calculate the total amount for all selected products
- create order entity, return order_id
- using that order_id, create order details entities
"""

ORDER_STATUSES = [
    "PENDING",
    "PENDING_PAYMENT",
    "PAYMENT_RECEIVED",
    "ORDER_CONFIRMED",
    "FAILED",
    "EXPIRED",
    "AWAITING_FULFILLMENT",
    "AWAITING_SHIPMENT",
    "ON_HOLD",
    "SHIPPED",
    "PARTIALLY_SHIPPED",
    "AWAITING_PICKUP",
    "COMPLETED",
    "CANCELED",
    "DECLINED",
    "REFUNDED",
    "PARTIALLY_REFUNDED",
    "DISPUTED"
]

def generate_order():
    total_selected_products = random.randint(a=1, b=10)

    with psycopg.connect("host=localhost dbname=ecomm_db user=postgres password=postgres port=5432") as conn:
        with conn.cursor() as cur:
            # randomize a stored customer
            cur.execute("SELECT * FROM customers")
            selected_customer = Customer(*(random.choice(cur.fetchall())))

            # randomize n products to buy
            cur.execute("SELECT * FROM products")
            selected_products = [Product(*row) for row in random.choices(cur.fetchall(), k=total_selected_products)]

            # calculate the total amount
            total_amount = sum([product.price for product in selected_products])

            # create order entity while returning the order_id
            order_status = random.choice(ORDER_STATUSES)
            cur.execute("""
                    INSERT INTO orders (customer_id, order_status, total_amount)
                    VALUES (%s, %s, %s)
                    RETURNING order_id
                """,
                (selected_customer.customer_id, order_status, total_amount)
            )
            order_id = str(*cur.fetchone())
            
            # create order details using order_id as the base
            for product in selected_products:
                prod_id = product.product_id
                quantity = random.randint(5, 22)
                unit_price = product.price
                cur.execute("""
                        INSERT INTO order_items (order_id, product_id, quantity, unit_price)
                        VALUES (%s, %s, %s, %s)
                    """,
                    (order_id, prod_id, quantity, unit_price)
                )
            conn.commit()
