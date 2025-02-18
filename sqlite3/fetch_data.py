import sqlite3



conn = sqlite3.connect("mydb.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()  # Fetch all rows

for row in rows:
    print(row)
