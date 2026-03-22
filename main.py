from database import connect_db, reset_tables, create_tables, insert_data
from analysis import (
    plot_delivery_delay,
    plot_warehouse_delivery_time,
    plot_cost_vs_delay,
    analyze_delivery_companies,
    analyze_warehouses,
    analyze_seller_companies,
    analyze_warehouse_throughput,
)

if __name__ == "__main__":
    conn = connect_db()
    reset_tables(conn)
    create_tables(conn)
    insert_data(conn)

    print("Database ready with sample data.")

    analyze_delivery_companies(conn)
    analyze_warehouses(conn)
    analyze_seller_companies(conn)
    analyze_warehouse_throughput(conn)
    plot_delivery_delay(conn)
    plot_warehouse_delivery_time(conn)
    plot_cost_vs_delay(conn)