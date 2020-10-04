import math
def body_mass_index(m,h):
    BMI=m/math.pow((h**2),2)
    return BMI
def bmi_information(m,h):
    bmi=body_mass_index(m,h)
    if bmi > 30:
        print("Beo phi")
        return True
    elif bmi >=25:
        print("Thua can")
        return True
    elif bmi >=18.5:
        print("Binh thuong")
        return True
    else:
        print("Gay")
        return False
m=float(input("Nhap can nang: "))
h=float(input("Nhap chieu cao: "))
while m<0 or h<0:
    print("Du lieu khong hop le\n Nhap lai")
    print("can nang la: ",end="")
    m=float(input())
    print("Chieu cao la: ",end="")
    h=float(input())
bmi_information(m,h)