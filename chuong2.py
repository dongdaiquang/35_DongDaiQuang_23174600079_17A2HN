#2.7
import json
json_data = '{"name": "John", "age": 30, "city": "New York"}'
python_obj = json.loads(json_data)
print("Dữ liệu JSON đã chuyển thành đối tượng Python:")
print(python_obj)

#2.8
from json.encoder import JSONEncoder
python_obj = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "occupation": "Engineer"
}
json_str=JSONEncoder().encode(python_obj)
print(json_str)
print(type(json_str))
#2.9
import json
from json.encoder import JSONEncoder
python_dict = {
    "name": "Alice",
    "age": 25,
    "city": "Hanoi",
    "job": "Engineer"
}
sorted_dict = dict(sorted(python_dict.items()))

json_data = JSONEncoder(indent=4).encode(sorted_dict)

print(json_data)
#2.10
import json
with open("data.json","r", encoding="utf-8") as f:
    data=json.load(f)
ten_cong_ty=data["company"]["name"]
dia_chi=data["company"]["address"]
employees=data["employees"]
tong_nhan_vien=len(employees)
unit_counts={}
for employee in employees:
    unit=employee["unit"]
    if unit in unit_counts:
        unit_counts[unit]+=1
    else:
        unit_counts[unit]=1
print(f" ten cong ty:{ten_cong_ty}")
print(f" dia chi:{dia_chi}")
print("----Thống kê nhân viên theo đơn vị------")
for idx, (unit, count) in enumerate(unit_counts.items(), start=1):
    percentage=(count/tong_nhan_vien)
    print(f"{idx}./Tên đơn vị: {unit}. - Số nhân viên: {count} - Tỷ lệ: {percentage:.2f}%")
#2.12
import requests
response=requests.get('https://jsonplaceholder.typicode.com/posts')
if response.status_code==200:
    json_data=response.json()
    print(f"tong so bai post:{len(json_data)}/n")
    for post in json_data:
        print(f"userid:{post['userId']}")
        print(f"ID: {post['id']}")
        print(f"Title: {post['title']}")
        print(f"Body: {post['body']}")
        print("\n" + "-" * 30 + "\n")
else:
    print("yeu cau khong thanh.ma trang thai:",respon.status_code)
#2.13
import requests
response=requests.get('https://jsonplaceholder.typicode.com/comments?postId=1')
if response.status_code==200:
    json_data=response.json()
    print("danh sach nhung bai post noi bat")
    for post in json_data[:3]:
        print(f"ID: {comment['id']}")
        print(f"Tên: {comment['name']}")
        print(f"Email: {comment['email']}")
        print(f"Nội dung: {comment['body']}\n")
else:
    print("yeu cau khong thanh cong:",response.status_code)
        
    
    

