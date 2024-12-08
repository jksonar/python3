def advanced_queries(conn):
    with conn.cursor() as cur:
        # Example: Inner Join
        cur.execute("""
        SELECT e.name, e.age, d.department_name 
        FROM employees e 
        INNER JOIN departments d 
        ON e.department = d.id;
        """)
        for row in cur.fetchall():
            print(row)

        # Example: Subquery
        cur.execute("""
        SELECT name 
        FROM employees 
        WHERE age = (SELECT MAX(age) FROM employees);
        """)
        print("Oldest employee:", cur.fetchone())
