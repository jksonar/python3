import logging
import os
import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
from crud_script import * 

# Load environment variables
load_dotenv()

# Configure Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

# Database Configuration
DB_CONFIG = {
    'dbname': os.getenv('DB_NAME', 'testdb'),
    'user': os.getenv('DB_USER', 'postgres'),
    'password': os.getenv('DB_PASSWORD', 'your_password'),
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': os.getenv('DB_PORT', 5432)
}

# Connect to PostgreSQL
def connect_db():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        logging.info("Database connection successful!")
        return conn
    except psycopg2.Error as e:
        logging.critical("Error connecting to the database:", exc_info=True)
        return None

# CRUD functions here (reuse from earlier examples)

# Main Function
def main():
    try:
        conn = connect_db()
        if conn:
            create_table(conn)
            insert_data(conn, "Alice", 30, "HR")
            read_data(conn)
            conn.close()
    except Exception as e:
        logging.critical(f"Unexpected error: {e}", exc_info=True)

if __name__ == "__main__":
    main()
