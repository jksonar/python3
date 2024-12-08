import psycopg2

DB_CONFIG = {
    'host': 'localhost',
    'database': 'testdb',
    'user': 'postgres',
    'password': 'your_password',
    'port': 5432  # Default PostgreSQL port
}

try:
    conn = psycopg2.connect(**DB_CONFIG)
    print("Database connection successful!")
except psycopg2.Error as e:
    print("Error connecting to the database:", e)

def bulk_insert(conn, data):
    with conn.cursor() as cur:
        query = "INSERT INTO employees (name, age, department) VALUES %s"
        psycopg2.extras.execute_values(cur, query, data)
        conn.commit()

data = [("Anna", 29, "HR"), ("Brian", 35, "IT"), ("Cathy", 33, "Finance")]
bulk_insert(conn, data)
