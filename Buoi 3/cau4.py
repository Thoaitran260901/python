n=int(input("Nhập N: "))
def is_prime(n):
    if(n<=1):
        return False
    for i in range(2,n//2+1):
        if(n%i==0):
            return False
    else:
        return True
if(is_prime(n)):
    print(f"{n} là số nguyên tố")
else:
    print(f"{n} không là số nguyên tố")