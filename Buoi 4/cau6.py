s = input("Nhập chuỗi: ")
def hoa(s):
    kq1=""
    for i in s:
        if i.islower():
            kq1+=i.upper()
        else:
            kq1+=i.lower()
    return kq1
print(f"Kết quả: {hoa(s)}")