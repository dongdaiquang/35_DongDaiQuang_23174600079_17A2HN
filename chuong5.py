#5.1
import sqlite3

def get_sqlite_version():
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute('SELECT SQLITE_VERSION()')
    version = cursor.fetchone()
    print("SQLite Version:", version[0])
    conn.close()

get_sqlite_version()
#5.2
import sqlite3
def connect_memory_db():
    conn=sqlite3.connect(':memory:')
    print("Kết nối thành công với cơ sở dữ liệu SQLite trong bộ nhớ")
    conn.close()
connect_memory_db()
#5.3
import sqlite3
connection = sqlite3.connect("mydatabase.db")
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER
)
""")
print("Bảng 'students' đã được tạo thành công.")
connection.commit()
connection.close()
#5.4
import sqlite3
connection = sqlite3.connect("mydatabase.db")
cursor = connection.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Danh sách các bảng trong cơ sở dữ liệu:")
for table in tables:
    print(table[0])
connection.close()
#5.5
import sqlite3
connection=sqlite3.connect("mydatabase.db")
cursor=connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    position TEXT
)
""")
cursor.executemany("INSERT INTO employees (name, position) VALUES (?, ?)", 
                   [("Alice", "Manager"), ("Bob", "Engineer"), ("Charlie", "Clerk")])
print("Đã chèn các bản ghi vào bảng 'employees'.")
connection.commit()
connection.close()
#5.6
import sqlite3
connection=sqlite3.connect("mydatabase.db")
cursor=connection.cursor()
cursor.execute("SELECT COUNT(*) FROM employees")
count = cursor.fetchone()[0]
print(f"Số bản ghi trong bảng 'employees': {count}")
connection.close()
#5.7
import sqlite3
connection = sqlite3.connect("mydatabase.db")
cursor = connection.cursor()
cursor.execute("UPDATE employees SET position = 'Staff'")
print("Đã cập nhật tất cả giá trị trong cột 'position' thành 'Staff'.")
cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()
print("Dữ liệu sau khi cập nhật:")
for row in rows:
    print(row)
connection.commit()
connection.close()








