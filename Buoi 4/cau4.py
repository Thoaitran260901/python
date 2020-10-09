chuoi=input("Nhập chuỗi: ")
def dau_duoi(chuoi):
    print(chuoi[0:2]+chuoi[-2:])
    if len(chuoi)<2:
        print("     ")
dau_duoi(chuoi)