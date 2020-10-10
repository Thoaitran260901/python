chuoi=input("Nhập chuỗi: ")
def minmaxchuoi(chuoi):
    max=min=chuoi[0]
    for i in chuoi:
        if min>i:
            min=i
        if max<i:
            max=i
    print("Ki tu lon nhat la",max)
    print("ki tu nho nhat la",min)
minmaxchuoi(chuoi)
