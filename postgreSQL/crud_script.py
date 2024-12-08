import psycopg2
from psycopg2 import sql

# Database Configuration
DB_CONFIG = {
    'host': 'localhost',
    'database': 'testdb',
    'user': 'postgres',
    'password': 'your_password',
    'port': 5432  # Default PostgreSQL port
}

# Connect to PostgreSQL
def connect_db():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        print("Database connection successful!")
        return conn
    except psycopg2.Error as e:
        print("Error connecting to the database:", e)
        return None

# Create Table
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
            print("Table 'employees' created successfully!")
    except psycopg2.Error as e:
        print("Error creating table:", e)

# Insert Data
def insert_data(conn, name, age, department):
    try:
        query = """
        INSERT INTO employees (name, age, department)
        VALUES (%s, %s, %s) RETURNING id;
        """
        with conn.cursor() as cur:
            cur.execute(query, (name, age, department))
            employee_id = cur.fetchone()[0]
            conn.commit()
            print(f"Inserted employee with ID: {employee_id}")
    except psycopg2.Error as e:
        print("Error inserting data:", e)

# Read Data
def read_data(conn):
    try:
        query = "SELECT * FROM employees;"
        with conn.cursor() as cur:
            cur.execute(query)
            rows = cur.fetchall()
            print("Employee Records:")
            for row in rows:
                print(row)
    except psycopg2.Error as e:
        print("Error reading data:", e)

# Update Data
def update_data(conn, emp_id, name=None, age=None, department=None):
    try:
        fields = []
        values = []
        if name:
            fields.append("name = %s")
            values.append(name)
        if age:
            fields.append("age = %s")
            values.append(age)
        if department:
            fields.append("department = %s")
            values.append(department)
        values.append(emp_id)

        query = sql.SQL("UPDATE employees SET {} WHERE id = %s").format(
            sql.SQL(", ").join(map(sql.SQL, fields))
        )

        with conn.cursor() as cur:
            cur.execute(query, values)
            conn.commit()
            print(f"Updated employee ID: {emp_id}")
    except psycopg2.Error as e:
        print("Error updating data:", e)

# Delete Data
def delete_data(conn, emp_id):
    try:
        query = "DELETE FROM employees WHERE id = %s;"
        with conn.cursor() as cur:
            cur.execute(query, (emp_id,))
            conn.commit()
            print(f"Deleted employee ID: {emp_id}")
    except psycopg2.Error as e:
        print("Error deleting data:", e)

# Main Function
def main():
    conn = connect_db()
    if conn:
        create_table(conn)

        # Perform CRUD Operations
        insert_data(conn, "Alice", 30, "HR")
        insert_data(conn, "Bob", 25, "IT")
        insert_data(conn, "Charlie", 35, "Finance")

        print("\nBefore Update:")
        read_data(conn)

        update_data(conn, 2, name="Robert", age=26)
        print("\nAfter Update:")
        read_data(conn)

        delete_data(conn, 1)
        print("\nAfter Deletion:")
        read_data(conn)

        # Close Connection
        conn.close()
        print("Connection closed.")

if __name__ == "__main__":
    main()
