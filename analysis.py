import pandas as pd
import matplotlib.pyplot as plt

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

def analyze_warehouse_throughput(conn):
    query = """
    WITH time_window AS (
        SELECT 
            JULIANDAY(MAX(order_date)) - JULIANDAY(MIN(order_date)) + 1 AS num_days
        FROM orders
    )
    SELECT w.warehouse_name,
           w.city,
           w.capacity,
           SUM(o.quantity) AS total_volume,
           ROUND(1.0 * SUM(o.quantity) / tw.num_days, 2) AS avg_daily_throughput,
           ROUND(100.0 * (SUM(o.quantity) / tw.num_days) / w.capacity, 2) AS daily_throughput_percent,
           AVG(d.delivery_time) AS avg_delivery_time,
           100.0 * AVG(d.delay_flag) AS delay_rate_percent
    FROM warehouses w
    JOIN orders o
        ON w.warehouse_id = o.warehouse_id
    JOIN deliveries d
        ON o.order_id = d.order_id
    CROSS JOIN time_window tw
    GROUP BY w.warehouse_id, w.warehouse_name, w.city, w.capacity, tw.num_days
    ORDER BY daily_throughput_percent DESC
    """

    df = run_query(conn, query)
    print("\nWarehouse Daily Throughput")
    print(df)



def plot_delivery_delay(conn):
    query = """
    SELECT delivery_company,
           100.0 * AVG(delay_flag) AS delay_rate_percent
    FROM deliveries
    GROUP BY delivery_company
    ORDER BY delay_rate_percent DESC
    """

    df = run_query(conn, query)

    # Plot
    plt.figure()
    plt.bar(df["delivery_company"], df["delay_rate_percent"])
    plt.xlabel("Delivery Company")
    plt.ylabel("Delay Rate (%)")
    plt.title("Delay Rate by Delivery Company")

    plt.show()

def plot_warehouse_delivery_time(conn):
    query = """
    SELECT w.warehouse_name,
           AVG(d.delivery_time) AS avg_delivery_time
    FROM warehouses w
    JOIN orders o
        ON w.warehouse_id = o.warehouse_id
    JOIN deliveries d
        ON o.order_id = d.order_id
    GROUP BY w.warehouse_name
    ORDER BY avg_delivery_time DESC
    """

    df = run_query(conn, query)

    import matplotlib.pyplot as plt

    plt.figure()
    plt.bar(df["warehouse_name"], df["avg_delivery_time"])
    plt.xlabel("Warehouse")
    plt.ylabel("Average Delivery Time")
    plt.title("Average Delivery Time by Warehouse")
    plt.xticks(rotation=45)

    plt.show()


def plot_cost_vs_delay(conn):
    query = """
    SELECT delivery_company,
           AVG(delivery_cost) AS avg_delivery_cost,
           100.0 * AVG(delay_flag) AS delay_rate_percent
    FROM deliveries
    GROUP BY delivery_company
    """

    df = run_query(conn, query)

    import matplotlib.pyplot as plt

    plt.figure()
    plt.scatter(df["avg_delivery_cost"], df["delay_rate_percent"])

    for i, txt in enumerate(df["delivery_company"]):
        plt.annotate(txt, (df["avg_delivery_cost"][i], df["delay_rate_percent"][i]))

    plt.xlabel("Average Delivery Cost")
    plt.ylabel("Delay Rate (%)")
    plt.title("Delivery Cost vs Delay Rate by Company")

    plt.show()