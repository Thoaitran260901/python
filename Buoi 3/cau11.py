print("Tim day Fibonacci")
#Tim day Fibonacci theo de quy
def fibo_dequy(n):
    if n==1 or n==2:
        return 1
    return fibo_dequy(n-1) + fibo_dequy(n-2)
#Tim day Fibonacci khong de quy
def fibo_thuong(n):
    n1=0
    n2=1
    for i in range(n-1):
        temp=n1+n2
        n1=n2
        n2=temp
    return temp
n=int(input("Nhap so fibo thu: "))
while n<=0:
    print("So khong hop le\n Nhap lai")
    n=int(input("Nhap so fibo thu: "))
print(f"De quy: {fibo_dequy(n)}")
print(f"Khong de quy: {fibo_thuong(n)}")