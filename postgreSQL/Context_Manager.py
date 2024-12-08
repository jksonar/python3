import psycopg2

# Database Configuration
DB_CONFIG = {
    'host': 'localhost',
    'database': 'testdb',
    'user': 'postgres',
    'password': 'your_password',
    'port': 5432  # Default PostgreSQL port
}

def safe_query():
    try:
        with psycopg2.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM employees;")
                print(cur.fetchall())
    except Exception as e:
        print("Error:", e)
