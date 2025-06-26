# setup_db.py
import os
import psycopg2
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise Exception("DATABASE_URL not found in .env file. Please set it up.")

# SQL commands to create table and insert data
commands = (
    """
    DROP TABLE IF EXISTS products;
    """,
    """
    CREATE TABLE products (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        category TEXT,
        price NUMERIC(10, 2),
        stock INTEGER
    );
    """,
    """
    INSERT INTO products (name, category, price, stock) VALUES
      ('Laptop Pro', 'Electronics', 1499.99, 50),
      ('Smart Watch', 'Electronics', 299.50, 120),
      ('Office Chair', 'Furniture', 175.00, 80),
      ('Project Planner', 'Office Supplies', 25.99, 200);
    """
)

conn = None
try:
    # Connect to the PostgreSQL server
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    # Execute each command
    for command in commands:
        cur.execute(command)
    # Close communication with the PostgreSQL database server
    cur.close()
    # Commit the changes
    conn.commit()
    print("Database setup complete. 'products' table created and populated.")
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()