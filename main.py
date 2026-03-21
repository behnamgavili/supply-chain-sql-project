from database import connect_db, reset_tables, create_tables, insert_data
from analysis import (analyze_delivery_companies,analyze_warehouses,analyze_seller_companies)


if __name__ == "__main__":
    conn = connect_db()
    reset_tables(conn)
    create_tables(conn)
    insert_data(conn)

    print("Database ready with sample data.")

    analyze_delivery_companies(conn)
    analyze_warehouses(conn)
    analyze_seller_companies(conn)