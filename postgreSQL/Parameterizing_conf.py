# pip install python-dotenv
# Create a .env file:
# DB_NAME=testdb
# DB_USER=postgres
# DB_PASSWORD=your_password
# DB_HOST=localhost
# DB_PORT=5432

import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    'dbname': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT'),
}

def connect_with_env():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        print("Connected using .env configuration!")
    except Exception as e:
        print("Connection error:", e)

connect_with_env()
