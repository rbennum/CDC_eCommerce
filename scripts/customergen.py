import psycopg
from faker import Faker

fake = Faker()

def generate_customer():
    name = fake.name()
    email = fake.email()

    with psycopg.connect("host=localhost dbname=ecomm_db user=postgres password=postgres port=5432") as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                    INSERT INTO customers (name, email) VALUES (%s, %s)
                """, 
                (name, email),
            )
            conn.commit()
