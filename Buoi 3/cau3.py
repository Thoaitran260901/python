n=int(input("Nhập N: "))
def is_perfect(n):
    sum=0
    for i in range(1,n//2+1):
        if(n%i==0):
            sum+=i
    if(n<=0):
        return False
    if(sum==n):
        return True
    else:
        return False
if(is_perfect(n)):
    print(f"{n} là số hoàn hảo")
else:
    print(f"{n} không là số hoàn hảo")