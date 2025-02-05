# CDC – e-commerce

## ER Diagram

```mermaid
erDiagram
    CUSTOMERS {
        int customer_id
        string name
        string email
    }
    PRODUCTS {
        int product_id
        string name
        string category
        int price
        int stocks
    }
    ORDERS {
        int order_id
        int customer_id
        int total_amount
    }
    ORDER_DETAILS {
        int order_id
        int product_id
        int quantity
        int unit_price
    }
    CUSTOMERS }|--o{ ORDERS : places
    ORDERS }o--o{ ORDER_DETAILS : contains
    ORDER_DETAILS }o--o{ PRODUCTS : links
```
