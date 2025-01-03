import sqlite3

def create_database():
    """Tạo cơ sở dữ liệu và bảng product."""
    conn = sqlite3.connect("product.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS product (
            Id INTEGER PRIMARY KEY,
            Name TEXT NOT NULL,
            Price REAL NOT NULL,
            Amount INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def display_products():
    """Hiển thị danh sách sản phẩm."""
    conn = sqlite3.connect("product.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM product")
    products = cursor.fetchall()
    if products:
        print("\nDanh sách sản phẩm:")
        print("ID | Tên | Giá | Số lượng")
        for product in products:
            print(f"{product[0]} | {product[1]} | {product[2]} | {product[3]}")
    else:
        print("\nKhông có sản phẩm nào.")
    conn.close()

def add_product():
    """Thêm sản phẩm mới."""
    name = input("Nhập tên sản phẩm: ")
    price = float(input("Nhập giá sản phẩm: "))
    amount = int(input("Nhập số lượng sản phẩm: "))
    conn = sqlite3.connect("product.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO product (Name, Price, Amount) VALUES (?, ?, ?)", (name, price, amount))
    conn.commit()
    conn.close()
    print("\nĐã thêm sản phẩm thành công.")

def search_product():
    """Tìm kiếm sản phẩm theo tên."""
    name = input("Nhập tên sản phẩm cần tìm: ")
    conn = sqlite3.connect("product.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM product WHERE Name LIKE ?", (f"%{name}%",))
    products = cursor.fetchall()
    if products:
        print("\nKết quả tìm kiếm:")
        print("ID | Tên | Giá | Số lượng")
        for product in products:
            print(f"{product[0]} | {product[1]} | {product[2]} | {product[3]}")
    else:
        print("\nKhông tìm thấy sản phẩm nào.")
    conn.close()

def update_product():
    """Cập nhật thông tin sản phẩm."""
    product_id = int(input("Nhập ID sản phẩm cần cập nhật: "))
    new_price = float(input("Nhập giá mới: "))
    new_amount = int(input("Nhập số lượng mới: "))
    conn = sqlite3.connect("product.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE product SET Price = ?, Amount = ? WHERE Id = ?", (new_price, new_amount, product_id))
    conn.commit()
    conn.close()
    print("\nĐã cập nhật sản phẩm thành công.")

def delete_product():
    """Xóa sản phẩm."""
    product_id = int(input("Nhập ID sản phẩm cần xóa: "))
    conn = sqlite3.connect("product.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM product WHERE Id = ?", (product_id,))
    conn.commit()
    conn.close()
    print("\nĐã xóa sản phẩm thành công.")

def main_menu():
    """Menu chính của chương trình."""
    while True:
        print("\nQuản lý sản phẩm")
        print("1. Hiển thị danh sách sản phẩm")
        print("2. Thêm sản phẩm mới")
        print("3. Tìm kiếm sản phẩm theo tên")
        print("4. Cập nhật thông tin sản phẩm")
        print("5. Xóa sản phẩm")
        print("6. Thoát")
        choice = input("Chọn chức năng (1-6): ")

        if choice == "1":
            display_products()
        elif choice == "2":
            add_product()
        elif choice == "3":
            search_product()
        elif choice == "4":
            update_product()
        elif choice == "5":
            delete_product()
        elif choice == "6":
            print("\nThoát chương trình.")
            break
        else:
            print("\nLựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    create_database()
    main_menu()
