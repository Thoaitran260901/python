s=input("Nhập chuỗi: ")
m=int(input("Nhập m: "))
def xoakitu(s,m):
    while(m<0):
        print("Nhập lại!!!")
        m=int(input("Nhập m: "))
    s = s[:m] + s[(m+1):]
    print(s)
xoakitu(s,m)