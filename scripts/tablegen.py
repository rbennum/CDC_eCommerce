import psycopg

def generate_table():
    with psycopg.connect("host=localhost dbname=ecomm_db user=postgres password=postgres port=5432") as conn:
        with conn.cursor() as cur:
            # create a customer table
            cur.execute("""
                CREATE TABLE IF NOT EXISTS customers (
                    customer_id INT GENERATED ALWAYS AS IDENTITY,
                    name TEXT,
                    email TEXT,
                    created_at TIMESTAMP DEFAULT NOW(),
                    PRIMARY KEY(customer_id)
                );
                """)

            # create an order table
            cur.execute("""
                CREATE TABLE IF NOT EXISTS orders (
                    order_id INT GENERATED ALWAYS AS IDENTITY,
                    customer_id INT,
                    order_status TEXT,
                    total_amount INT,
                    created_at TIMESTAMP DEFAULT NOW(),
                    PRIMARY KEY(order_id),
                    CONSTRAINT fk_customer FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
                );
                """)

            # create a product table
            cur.execute("""
                CREATE TABLE IF NOT EXISTS products (
                    product_id INT GENERATED ALWAYS AS IDENTITY,
                    name TEXT,
                    category TEXT,
                    price INT,
                    stock INT,
                    created_at TIMESTAMP DEFAULT NOW(),
                    PRIMARY KEY(product_id)
                );
                """)

            # create an order item table
            cur.execute("""
                CREATE TABLE IF NOT EXISTS order_items (
                    order_id INT,
                    product_id INT,
                    quantity INT,
                    unit_price INT,
                    CONSTRAINT fk_order FOREIGN KEY(order_id) REFERENCES orders(order_id),
                    CONSTRAINT fk_product FOREIGN KEY(product_id) REFERENCES products(product_id)
                );
                """)
            conn.commit()

def drop_tables():
    with psycopg.connect("host=localhost dbname=ecomm_db user=postgres password=postgres port=5432") as conn:
        with conn.cursor() as cur:
            cur.execute("DROP TABLE IF EXISTS order_items CASCADE")
            cur.execute("DROP TABLE IF EXISTS orders CASCADE")
            cur.execute("DROP TABLE IF EXISTS products CASCADE")
            cur.execute("DROP TABLE IF EXISTS customers CASCADE")
            conn.commit()
