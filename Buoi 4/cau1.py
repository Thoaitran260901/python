chuoi = input("nhập chuỗi: ")
def thaythe():
    a= chuoi[0]
    for i in range(1,len(chuoi)):
        if chuoi[i] == chuoi[0]:
            a+="$"
        else:
            a+=chuoi[i]
    return a
print(thaythe())
