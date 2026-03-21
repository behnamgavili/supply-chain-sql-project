import pandas as pd


def run_query(conn, query):
    return pd.read_sql_query(query, conn)


def analyze_delivery_companies(conn):
    query = """
    SELECT delivery_company,
           COUNT(*) AS num_deliveries,
           AVG(delivery_cost) AS avg_cost,
           AVG(delivery_time) AS avg_delivery_time,
           100.0 * AVG(delay_flag) AS delay_rate_percent
    FROM deliveries
    GROUP BY delivery_company
    ORDER BY delay_rate_percent DESC
    """

    df = run_query(conn, query)
    print("\nDelivery Company Performance")
    print(df)

def analyze_warehouses(conn):
    query = """
    SELECT w.warehouse_name,
           w.city,
           w.capacity,
           SUM(o.quantity) AS total_volume,
           AVG(d.delivery_time) AS avg_delivery_time,
           AVG(d.delivery_cost) AS avg_delivery_cost,
           100.0 * AVG(d.delay_flag) AS delay_rate_percent
    FROM warehouses w
    JOIN orders o
        ON w.warehouse_id = o.warehouse_id
    JOIN deliveries d
        ON o.order_id = d.order_id
    GROUP BY w.warehouse_id, w.warehouse_name, w.city, w.capacity
    ORDER BY total_volume DESC
    """

    df = run_query(conn, query)
    print("\nWarehouse Performance")
    print(df)

def analyze_seller_companies(conn):
    query = """
    SELECT o.seller_company,
           COUNT(*) AS num_orders,
           SUM(o.quantity) AS total_quantity,
           AVG(d.delivery_time) AS avg_delivery_time,
           AVG(d.delivery_cost) AS avg_delivery_cost,
           100.0 * AVG(d.delay_flag) AS delay_rate_percent
    FROM orders o
    JOIN deliveries d
        ON o.order_id = d.order_id
    GROUP BY o.seller_company
    ORDER BY total_quantity DESC
    """

    df = run_query(conn, query)
    print("\nSeller Company Performance")
    print(df)



def analyze_seller_companies(conn):
    query = """
    SELECT o.seller_company,
           COUNT(*) AS num_orders,
           SUM(o.quantity) AS total_quantity,
           AVG(d.delivery_time) AS avg_delivery_time,
           AVG(d.delivery_cost) AS avg_delivery_cost,
           100.0 * AVG(d.delay_flag) AS delay_rate_percent
    FROM orders o
    JOIN deliveries d
        ON o.order_id = d.order_id
    GROUP BY o.seller_company
    ORDER BY total_quantity DESC
    """

    df = run_query(conn, query)
    print("\nSeller Company Performance")
    print(df)