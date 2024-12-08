import psycopg2
import os


DB_CONFIG = {
    'dbname': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT'),
}

def fetch_paginated_data(conn, page, page_size):
    offset = (page - 1) * page_size
    query = f"SELECT * FROM employees LIMIT {page_size} OFFSET {offset};"
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

# Fetch page 2 with 5 records per page
conn = psycopg2.connect(**DB_CONFIG)
data = fetch_paginated_data(conn, page=2, page_size=5)
print(data)
