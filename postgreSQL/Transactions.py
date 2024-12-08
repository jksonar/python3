import psycopg2

def transaction_example():
    try:
        conn = psycopg2.connect(
            dbname='testdb',
            user='postgres',
            password='your_password',
            host='localhost',
            port=5432
        )
        with conn:
            with conn.cursor() as cur:
                # Begin transaction
                cur.execute("INSERT INTO employees (name, age, department) VALUES (%s, %s, %s)", ("Dave", 40, "Marketing"))
                cur.execute("INSERT INTO employees (name, age, department) VALUES (%s, %s, %s)", ("Eva", 28, "HR"))
                # Commit transaction automatically
                print("Transaction committed.")
    except Exception as e:
        print("Error occurred, transaction rolled back:", e)

transaction_example()
