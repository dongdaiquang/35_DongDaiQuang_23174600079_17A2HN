#7.1
import tkinter as tk
window = tk.Tk()
window.title("Cửa sổ đầu tiên")
window.mainloop()
#7.2
import tkinter as tk
window = tk.Tk()
window.title("Cửa sổ có nhãn")
label = tk.Label(window, text="Đây là một nhãn")
label.pack()
window.mainloop()
#7.3
import tkinter as tk
from tkinter import font
window = tk.Tk()
window.title("Cửa sổ với nhãn có kiểu chữ tùy chỉnh")
custom_font = font.Font(family="Arial", size=16, weight="bold")
label = tk.Label(window, text="Nhãn với kiểu chữ Arial, đậm, cỡ 16", font=custom_font)
label.pack()
window.mainloop()
#7.4
import tkinter as tk
from tkinter import messagebox
def submit_action():
    name = entry_name.get()
    student_id = entry_id.get()
    password = entry_password.get()
    messagebox.showinfo("Thông báo", f"Tên: {name}\nID: {student_id}\nMật khẩu: {password}")
window = tk.Tk()
window.title("Thông tin sinh viên")
tk.Label(window, text="Tên sinh viên:").pack()
entry_name = tk.Entry(window)
entry_name.pack()
tk.Label(window, text="ID sinh viên:").pack()
entry_id = tk.Entry(window)
entry_id.pack()
tk.Label(window, text="Mật khẩu:").pack()
entry_password = tk.Entry(window, show="*")
entry_password.pack()
submit_button = tk.Button(window, text="Gửi", command=submit_action)
submit_button.pack()
window.mainloop()
#7.5
import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

root = tk.Tk()
root.title("Chương trình xem ảnh")
image_path = "Otto.png" 
img = Image.open(image_path)
photo = ImageTk.PhotoImage(img)
label = tk.Label(root, image=photo)
label.pack()
root.mainloop()

root = tk.Tk()
root.title("Chương trình xem ảnh từ URL")
url = "https://example.com/image.png"
response = requests.get(url)
img = Image.open(BytesIO(response.content))
photo = ImageTk.PhotoImage(img)
label = tk.Label(root, image=photo)
label.pack()
root.mainloop()
#7.7
import tkinter as tk

window = tk.Tk()

window.title("Tieu de cua so")

checkbutton = tk.Checkbutton(window, text="Chon")

checkbutton.pack()

label = tk.Label(window, text="Trang thai: Khong chon")

label.pack()

def on_change_checkbutton():
    state = checkbutton.instate(["selected"])

    if state:
        label.config(text="Trang thai: Chon")
    else:
        label.config(text="Trang thái: Khong chon")

checkbutton.config(command=on_change_checkbutton)

window.mainloop()

#7.8
def liet_ke_uoc(N):
    uoc = []
    for i in range(1, N + 1):
        if N % i == 0:
            uoc.append(i)
    return uoc
try:
    N = int(input("Nhập số nguyên N: "))
    if N > 0:
        print("Các ước của số N là:", liet_ke_uoc(N))
    else:
        print("Vui lòng nhập một số nguyên dương!")
except ValueError:
    print("Đầu vào không hợp lệ! Vui lòng nhập số nguyên.")
import tkinter as tk
from tkinter import messagebox

def liet_ke_uoc(N):
    return [i for i in range(1, N + 1) if N % i == 0]

def hien_thi_uoc():
    try:
        N = int(entry.get())
        if N > 0:
            uoc = liet_ke_uoc(N)
            messagebox.showinfo("Kết quả", f"Các ước của {N} là: {', '.join(map(str, uoc))}")
        else:
            messagebox.showerror("Lỗi", "Vui lòng nhập một số nguyên dương!")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập một số nguyên hợp lệ!")
root = tk.Tk()
root.title("Liệt kê các ước của số N")
tk.Label(root, text="Nhập số nguyên N:").grid(row=0, column=0, padx=10, pady=10)
entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=10, pady=10)

tk.Button(root, text="Hiển thị các ước", command=hien_thi_uoc).grid(row=1, column=0, columnspan=2, pady=10)
root.mainloop()
#7.9
import tkinter as tk
from tkinter import messagebox
import math

def calculate():
    try:
        m = int(entry_m.get())
        n = int(entry_n.get())
        if selected_function.get() == "GCD":
            result = math.gcd(m, n)
            result_label.config(text=f"GCD({m}, {n}) = {result}")
        elif selected_function.get() == "LCM":
            result = abs(m * n) // math.gcd(m, n)
            result_label.config(text=f"LCM({m}, {n}) = {result}")
        else:
            messagebox.showerror("Error", "Please select a function (GCD or LCM)")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid integers for m and n")

window = tk.Tk()
window.title("GCD and LCM Calculator")

label_m = tk.Label(window, text="Enter value of m:")
label_m.grid(row=0, column=0, padx=10, pady=5)
entry_m = tk.Entry(window)
entry_m.grid(row=0, column=1, padx=10, pady=5)

label_n = tk.Label(window, text="Enter value of n:")
label_n.grid(row=1, column=0, padx=10, pady=5)
entry_n = tk.Entry(window)
entry_n.grid
#7.10
import tkinter as tk
from tkinter import simpledialog, messagebox
root = tk.Tk()
root.withdraw() 
name = simpledialog.askstring("Nhập tên", "Xin vui lòng nhập tên của bạn:")
age = simpledialog.askinteger("Nhập tuổi", "Xin vui lòng nhập tuổi của bạn:")
if age >= 18:
    message = f"{name} – Bạn đã trưởng thành!"
else:
    message = f"{name} – Bạn còn nhỏ tuổi!"
messagebox.showinfo("Thông báo", message)
root.mainloop()




