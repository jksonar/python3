import psycopg2

# Database Configuration
DB_CONFIG = {
    'host': 'localhost',
    'database': 'testdb',
    'user': 'postgres',
    'password': 'your_password',
    'port': 5432  # Default PostgreSQL port
}

try:
    conn = psycopg2.connect(**DB_CONFIG)
except psycopg2.OperationalError as e:
    print("Connection failed:", e)
except psycopg2.DatabaseError as e:
    print("Database error:", e)
finally:
    if conn:
        conn.close()
