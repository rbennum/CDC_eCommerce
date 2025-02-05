import scripts.tablegen as tg
import scripts.customergen as cg
import scripts.productgen as pg
import scripts.ordergen as og
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--create-tables", action="store_true",
                        help="create database tables before generating data")
    parser.add_argument("--drop-tables", action="store_true",
                        help="drop the existing database tables")
    parser.add_argument("--gen-customers", type=int, metavar="N", 
                        help="Generate N customer records")
    parser.add_argument("--gen-products", type=int, metavar="N", help="Generate N product records")
    parser.add_argument("--gen-orders", type=int, metavar="N", help="Generate N order records")
    args = parser.parse_args()

    if args.create_tables:
        tg.generate_table()
    
    if args.drop_tables:
        tg.drop_tables()
    
    if args.gen_customers:
        for _ in range(args.gen_customers):
            cg.generate_customer()

    if args.gen_products:
        for _ in range(args.gen_products):
            pg.generate_product()

    if args.gen_orders:
        for _ in range(args.gen_orders):
            og.generate_order()
