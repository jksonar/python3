import sqlite3

conn = sqlite3.connect("mydb.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER
)
""")

cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Jerry", 25))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 34))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Tom", 21))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Sam", 55))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Jack", 78))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("donald", 13))

conn.commit()  # Save (commit) changes

