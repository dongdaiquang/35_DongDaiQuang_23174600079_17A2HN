#1
class hinhchunhat:
    def __init__(self, chieu_dai=0, chieu_rong=0):
        self.chieu_dai=chieu_dai
        self.chieu_rong=chieu_rong
    def nhap_du_lieu(self):
        self.chieu_dai=float(input("nhap chieu dai"))
        self.chieu_rong=float(input("nhap chieu rong"))
    def chu_vi(self):
        return 2*(self.chieu_dai+self.chieu_rong)
    def dien_tich(self):
        return self.chieu_dai*self.chieu_rong
    def in_thong_tin(self):
        tinh_chu_vi=self.chu_vi()
        tinh_dien_tich=self.dien_tich()
        print("chieu dai:", self.chieu_dai)
        print("chieu rong:", self.chieu_rong)
        print("chu vi", tinh_chu_vi)
        print("dien_tich", tinh_dien_tich)
if __name__ == "__main__":
    hcn=hinhchunhat()
    hcn.nhap_du_lieu()
    hcn.in_thong_tin()

#3
import math
class phanso:
    def __init__(self, tu_so=0, mau_so=0):
        self.tu_so=tu_so
        self.mau_so=mau_so
    def kiem_tra_hop_le(self):
        if self.mau_so == 0:
            return False
        return True
    def nhap_phan_so(self):
        self.tu_so=int(input("nhap tu so"))
        self.mau_so=int(input("nhap mau so"))
        while not self.kiem_tra_hop_le():
            print("nhap lai mau so")
            self.mau_so=int(input("nhap mau so"))
    def in_phan_so(self):
        if self.mau_so==1:
            print(f"Phân số: {self.tu_so}")
        elif self.tu_so==0:
            print("phan so bang 0")
        else:
            print(f"Phân số: {self.tu_so}/{self.mau_so}")
if __name__=="__main__":
    ps=phanso()
    ps.nhap_phan_so()
    ps.in_phan_so()
#10
import math
class diem:
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y
class elip(diem):
    def __init__(self, x=0, y=0, truc_lon=1, truc_nho=1):
        super().__init__(x,y)
        self.truc_lon=truc_lon
        self.truc_nho=truc_nho
    def dien_tich(self):
        return math.pi * self.truc_lon * self.truc_nho
class duong_tron(elip):
    def __init__(self, x=0, y=0, ban_kinh=1):
        super().__init__(x,y, ban_kinh, ban_kinh)
    def dien_tich(self):
        return math.pi*self.truc_lon*self.truc_lon
x = float(input("Nhập tọa độ x của tâm elip: "))
y = float(input("Nhập tọa độ y của tâm elip: "))
truc_lon=float(input("nhap toa do truc lon cua elip:"))
truc_nho=float(input("nhap toa do truc nho cua elip:"))
ban_kinh=float(input("nhap toa do ban kin"))
print("dien tich elip", elip(x, y,truc_nho, truc_lon).dien_tich())
print("dien tich hinh tron", duong_tron(x,y,ban_kinh).dien_tich())
#11
import math
class tamgiac:
    def __init__(self, a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def kiem_tra_hop_lẹ(self):
        return self.a+self.b>self.c and self.b+self.c>self.a and self.a+self.c>self.b
    def chu_vi(self):
        if self.kiem_tra_hop_le():
            return self.a+self.b+self.c
        else:
            return"tam giac khong hop le"
class tamgiacvuong(tamgiac):
    def kiem_tra_vuong(self):
        return self.a**2+self**b==self.c**2 or self.a**2+self.c**2==self.b**2 or self.b**2+self.c**2==self.a**2
    def kiem_tra_hop_le(self):
        return super.kiem_tra_hop_le() and kiem_tra_vuong()
class tamgiaccan(tamgiac):
    def __init__(self,a,b):
        super().__init__(a,a,b)
    def kiem_tra_hop_le(self):
        return super().kiem_tra_hop_le()
#9
import math
class DaGiac:
    def __init__(self, so_canh):
        self.so_canh=so_canh
class HinhBinhHanh(DaGiac):
    def __init__(self,day,chieu_cao):
        super().__init__(so_canh=4)
        self.day=day
        self.chieu_cao=chieu_cao
    def chu_vi(self):
        return 2*(self.day+self.chieu_cao)
    def dien_tich(self):
        return self.day*self.chieu_cao
class HinhChuNhat(HinhBinhHanh):
    def __init__(self, chieu_dai, chieu_rong):
        super().__init__(day=chieu_dai,chieu_cao=chieu_rong)
    def chu_vi(self):
        return (self.day+self.chieu_cao)*2
    def dien_tich(self):
        return self.day*self.chieu_cao
class HinhVuong(HinhChuNhat):
    def __init__(self, canh):
        super().__init__(chieu_dai=canh,chieu_rong=canh)
    def chu_vi(self):
        return self.day*4
    def dien_tich(self):
        return self.day**2
hinh_binh_hanh=HinhBinhHanh(5,3)
print(f"chuvi hbh: {hinh_binh_hanh.chu_vi()}")
print(f"dien tich hbh: {hinh_binh_hanh.dien_tich()}")
hinh_chu_nhat = HinhChuNhat(5, 3)
print(f"Hình chữ nhật - Chu vi: {hinh_chu_nhat.chu_vi()}, Diện tích: {hinh_chu_nhat.dien_tich()}")
hinh_vuong = HinhVuong(4)
print(f"Hình vuông - Chu vi: {hinh_vuong.chu_vi()}, Diện tích: {hinh_vuong.dien_tich()}")
#7
class Date:
    def __init__(self,ngay=1,thang=1,nam=2000):
        self.ngay=ngay
        self.thang=thang
        self.nam=nam
    def display(self):
        print(f"ngay:{self.ngay:02}/{self.thang:02}/{self.nam}")
    def next(self):
        ngay_trong_thang=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.ngay+=1
        if self.ngay>ngay_trong_thang[self.ngay-1]:
            self.ngay=1
            self.thang+=1
        if self.thang>12:
            self.thang=1
            self.nam+=1
#2
class TS:
    def __init__(self,ho_ten,diem_toan,diem_ly,diem_hoa):
        self.ho_ten=ho_ten
        self.diem_toan=diem_toan
        self.diem_ly=diem_ly
        self.diem_hoa=diem_hoa
    def in_thong_tin(self):
        print(f"Họ tên: {self.ho_ten}")
        print(f"Điểm Toán: {self.diem_toan}")
        print(f"Điểm Lý: {self.diem_ly}")
        print(f"Điểm Hoá: {self.diem_hoa}")
        print(f"Tổng điểm: {self.tinh_tong_diem()}")
    def tinh_tong_diem(self):
        return self.diem_toan+self.diem_ly+self.diem_hoa
def nhap_danh_sach_thi_sinh():
    danh_sach=[]
    so_luong=int(input("nhap so luong thi sinh:"))
    for i in range(so_luong):
        print(f"nhap thong tin thi sinh thu {i+1}:")
        ho_ten=input("ho ten:")
        diem_toan=float(input("diem toan:"))
        diem_ly=float(input("diem ly"))
        diem_hoa=float(input("diem hoa"))
        ts=TS(ho_ten,diem_toan,diem_ly,diem_hoa)
        danh_sach.append(ts)
    return danh_sach
def in_danh_sach_trung_tuyen(danh_sach, diem_chuan=20):
    danh_sach_trung_tuyen = [ts for ts in danh_sach if ts.tinh_tong_diem() >= diem_chuan]
    danh_sach_trung_tuyen.sort(key=lambda ts: ts.tinh_tong_diem(), reverse=True)
    print("\nDanh sach thi sinh trung tuyen (diem chuan >=20):")
    for ts in danh_sach_trung_tuyen:
        ts.in_thong_tin()
def main():
    danh_sach_thi_sinh=nhap_danh_sach_thi_sinh()
    in_danh_sach_trung_tuyen(danh_sach_thi_sinh)
if __name__ == "__main__":
    main()
#4
class Stack:
    def __init__(self, kich_thuoc):
        self.kich_thuoc=kich_thuoc
        self.Stack=[0.0]*kich_thuoc
        self.top=-1
    def isEmpty(self):
        return self.top == -1
    def isFull(self):
        return self.top==self.kich_thuoc-1
    def __del__(self):
        del self.stack
    
    


    
        
    
    
        
    


        
    
        
