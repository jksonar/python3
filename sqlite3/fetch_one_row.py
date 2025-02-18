import sqlite3

conn = sqlite3.connect("mydb.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM users")

row = cursor.fetchone()  # Fetch next row
print(row)
