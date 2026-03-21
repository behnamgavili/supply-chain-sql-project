import sqlite3
import os
import sqlite3
import os
import random
from datetime import datetime, timedelta


def connect_db():
    db_path = os.path.join(os.getcwd(), "supply_chain.db")
    conn = sqlite3.connect(db_path)
    return conn


def reset_tables(conn):
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS deliveries")
    cursor.execute("DROP TABLE IF EXISTS orders")
    cursor.execute("DROP TABLE IF EXISTS warehouses")
    conn.commit()


def create_tables(conn):
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS warehouses (
        warehouse_id INTEGER PRIMARY KEY,
        warehouse_name TEXT,
        city TEXT,
        capacity INTEGER)
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        order_id INTEGER PRIMARY KEY,
        product_name TEXT,
        quantity INTEGER,
        warehouse_id INTEGER,
        seller_company TEXT,
        order_date TEXT,
        FOREIGN KEY (warehouse_id) REFERENCES warehouses(warehouse_id))
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS deliveries (
        delivery_id INTEGER PRIMARY KEY,
        order_id INTEGER,
        delivery_company TEXT,
        delivery_time INTEGER,
        delivery_cost REAL,
        delay_flag INTEGER,
        FOREIGN KEY (order_id) REFERENCES orders(order_id))
    """)

    conn.commit()



def insert_data(conn):
    cursor = conn.cursor()

    # -------------------------
    # 1. Insert warehouses
    # -------------------------
    warehouses_data = [
        (1, "North Hub", "Milan", 5000),
        (2, "Central Hub", "Rome", 4000),
        (3, "West Hub", "Paris", 4500),
        (4, "East Hub", "Berlin", 4200)
    ]

    cursor.executemany("""
    INSERT INTO warehouses (warehouse_id, warehouse_name, city, capacity)
    VALUES (?, ?, ?, ?)
    """, warehouses_data)

    # -------------------------
    # 2. Insert orders
    # -------------------------
    products = ["Laptop", "Phone", "Tablet", "Monitor", "Printer"]
    seller_companies = ["Amazon", "TechStore", "ElectroWorld", "SmartShop"]
    warehouse_ids = [1, 2, 3, 4]

    start_date = datetime(2025, 1, 1)
    orders_data = []

    for order_id in range(1, 201):
        product_name = random.choice(products)
        quantity = random.randint(5, 300)
        warehouse_id = random.choice(warehouse_ids)
        seller_company = random.choice(seller_companies)

        order_date = start_date + timedelta(days=random.randint(0, 90))
        order_date = order_date.strftime("%Y-%m-%d")

        orders_data.append((
            order_id,
            product_name,
            quantity,
            warehouse_id,
            seller_company,
            order_date
        ))

    cursor.executemany("""
    INSERT INTO orders (
        order_id,
        product_name,
        quantity,
        warehouse_id,
        seller_company,
        order_date
    )
    VALUES (?, ?, ?, ?, ?, ?)
    """, orders_data)

    # -------------------------
    # 3. Insert deliveries
    # -------------------------
    delivery_companies = ["DHL", "UPS", "FedEx", "Maersk"]
    deliveries_data = []

    for delivery_id in range(1, 201):
        order_id = delivery_id
        delivery_company = random.choice(delivery_companies)
        delivery_time = random.randint(1, 7)
        delivery_cost = round(random.uniform(20, 300), 2)
        delay_flag = 1 if delivery_time > 4 else 0

        deliveries_data.append((
            delivery_id,
            order_id,
            delivery_company,
            delivery_time,
            delivery_cost,
            delay_flag
        ))

    cursor.executemany("""
    INSERT INTO deliveries (
        delivery_id,
        order_id,
        delivery_company,
        delivery_time,
        delivery_cost,
        delay_flag
    )
    VALUES (?, ?, ?, ?, ?, ?)
    """, deliveries_data)

    conn.commit()