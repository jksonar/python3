The `sqlite3` module in Python 3 is used to interact with SQLite databases. SQLite is a lightweight, file-based database that does not require a separate server process, making it ideal for small to medium applications.

---

## **Basic Steps to Use `sqlite3` in Python**

### 1. **Import the Module**
```python
import sqlite3
```

### 2. **Connect to a Database**
- If the database file exists, it connects to it.
- If not, it creates a new database file.

```python
conn = sqlite3.connect("my_database.db")  # Creates or opens a database file
```
> You can also use `":memory:"` instead of a filename to create a temporary in-memory database.

```python
conn = sqlite3.connect(":memory:")  # Temporary in-memory database
```

### 3. **Create a Cursor Object**
A **cursor** is used to execute SQL commands.

```python
cursor = conn.cursor()
```

### 4. **Create a Table**
Use `cursor.execute()` to run SQL commands.

```python
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER
)
""")
```

### 5. **Insert Data**
```python
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 25))
conn.commit()  # Save (commit) changes
```
> `?` placeholders are used to prevent SQL injection.

### 6. **Fetch Data**
```python
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()  # Fetch all rows

for row in rows:
    print(row)
```
Alternatively, you can fetch one row at a time:
```python
row = cursor.fetchone()  # Fetch next row
print(row)
```

### 7. **Update Data**
```python
cursor.execute("UPDATE users SET age = ? WHERE name = ?", (30, "Alice"))
conn.commit()
```

### 8. **Delete Data**
```python
cursor.execute("DELETE FROM users WHERE name = ?", ("Alice",))
conn.commit()
```

### 9. **Close the Connection**
Always close the connection when done.
```python
conn.close()
```

---

## **Additional Features of `sqlite3`**

### 1. **Using a `with` Statement (Auto Close)**
```python
with sqlite3.connect("my_database.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    print(cursor.fetchall())  # Auto closes connection after block execution
```

### 2. **Row Factory for Dictionary-like Access**
By default, SQLite returns tuples. You can make it return dictionaries.
```python
conn.row_factory = sqlite3.Row
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
row = cursor.fetchone()
print(dict(row))  # {'id': 1, 'name': 'Alice', 'age': 30}
```

### 3. **Using `executemany()` for Bulk Inserts**
```python
users = [("Bob", 28), ("Charlie", 22)]
cursor.executemany("INSERT INTO users (name, age) VALUES (?, ?)", users)
conn.commit()
```

### 4. **Handling Errors with `try-except`**
```python
try:
    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM non_existing_table")  # This will cause an error
except sqlite3.Error as e:
    print("SQLite error:", e)
finally:
    conn.close()
```

---

## **Why Use SQLite with Python?**
✅ **Lightweight & Fast** – No need for a separate database server.  
✅ **Easy to Use** – Uses simple SQL syntax.  
✅ **Integrated into Python** – No need to install extra dependencies.  
✅ **Cross-Platform** – Works on Linux, Windows, and macOS.

