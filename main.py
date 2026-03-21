from database import connect_db, reset_tables, create_tables, insert_data


if __name__ == "__main__":
    conn = connect_db()
    reset_tables(conn)
    create_tables(conn)
    insert_data(conn)

    print("Database ready with sample data.")

cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM warehouses")
print("Warehouses:", cursor.fetchone()[0])

cursor.execute("SELECT COUNT(*) FROM orders")
print("Orders:", cursor.fetchone()[0])

cursor.execute("SELECT COUNT(*) FROM deliveries")
print("Deliveries:", cursor.fetchone()[0])