from psycopg2 import pool

# Create a connection pool
connection_pool = pool.SimpleConnectionPool(
    minconn=1,  # Minimum connections
    maxconn=10, # Maximum connections
    user='postgres',
    password='your_password',
    host='localhost',
    port=5432,
    database='testdb'
)

def use_pool():
    try:
        # Get a connection from the pool
        conn = connection_pool.getconn()
        if conn:
            print("Successfully received a connection from the pool!")
            with conn.cursor() as cur:
                cur.execute("SELECT version();")
                print("Database version:", cur.fetchone())
        # Return the connection back to the pool
        connection_pool.putconn(conn)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    use_pool()
    connection_pool.closeall()  # Close all connections in the pool
