# scan folder path for all files and add data to sqlit file
import os
import hashlib
import sqlite3
from pathlib import Path

# SQLite database file
DB_FILE = "file_md5.db"

def calculate_md5(file_path):
    """Calculate the MD5 checksum of a given file."""
    hash_md5 = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):  # Read file in chunks
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except Exception as e:
        print(f"Failed to calculate MD5 for {file_path}: {e}")
        return None

def initialize_database():
    """Initialize the SQLite database."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS files (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            file_path TEXT UNIQUE,
            md5sum TEXT,
            last_checked TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def store_md5_in_db(file_path, md5sum):
    """Store or update the MD5 checksum of a file in the SQLite database."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO files (file_path, md5sum) 
            VALUES (?, ?)
            ON CONFLICT(file_path) DO UPDATE SET 
                md5sum=excluded.md5sum, 
                last_checked=CURRENT_TIMESTAMP
        """, (file_path, md5sum))
        conn.commit()
    except Exception as e:
        print(f"Error inserting/updating DB for {file_path}: {e}")
    finally:
        conn.close()

def compare_md5_in_db(file_path, new_md5sum):
    """Compare the MD5 checksum of a file with the one in the database."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT md5sum FROM files WHERE file_path = ?", (file_path,))
        result = cursor.fetchone()
        if result:
            stored_md5 = result[0]
            if stored_md5 == new_md5sum:
                print(f"File '{file_path}' is unchanged.")
            else:
                print(f"File '{file_path}' has changed! (MD5 mismatch)")
        else:
            print(f"File '{file_path}' is new (not in database).")
    except Exception as e:
        print(f"Error comparing MD5 for {file_path}: {e}")
    finally:
        conn.close()

def scan_directory(target_directory):
    """Scan a directory and process all files."""
    target_directory = Path(target_directory).resolve()
    if not target_directory.is_dir():
        print(f"Error: '{target_directory}' is not a valid directory.")
        return
    
    print(f"Scanning directory: {target_directory}")
    for file in target_directory.rglob("*"):  # Recursively scan all files
        if file.is_file():
            print(f"Processing file: {file}")
            md5sum = calculate_md5(file)
            if md5sum:
                compare_md5_in_db(str(file), md5sum)
                store_md5_in_db(str(file), md5sum)

if __name__ == "__main__":
    # Initialize the database
    initialize_database()
    
    # Get directory input from user
    target_dir = input("Enter the directory to scan (e.g., C:\\path\\to\\folder or /home/user/folder): ")
    scan_directory(target_dir)
