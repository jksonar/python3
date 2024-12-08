import time
import logging

def create_table(conn):
    try:
        query = """
        CREATE TABLE IF NOT EXISTS employees (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            age INTEGER,
            department VARCHAR(50)
        );
        """
        with conn.cursor() as cur:
            cur.execute(query)
            conn.commit()
            logging.info("Table 'employees' created successfully!")
    except Exception as e:
        logging.error(f"Error creating table: {e}")

def timed_query(conn, query):
    try:
        start_time = time.time()
        with conn.cursor() as cur:
            cur.execute(query)
            conn.commit()
        elapsed_time = time.time() - start_time
        logging.info(f"Query executed in {elapsed_time:.2f} seconds")
    except Exception as e:
        logging.error(f"Error executing query: {e}")
