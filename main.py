import scripts.tablegen as tg
import scripts.customergen as cg
import scripts.productgen as pg
import scripts.ordergen as og

if __name__ == "__main__":
    tg.generate_table()
    for _ in range(2):
        cg.generate_customer()
    for _ in range(5):
        pg.generate_product()
    og.generate_order()
