#BT: Tim so nghich dao
# def nghichdao(n):
#     s=str(n)[::-1]
#     print(f"So nghich dao cua n: {s}")
# n=int(input("Nhap n:"))
# nghichdao(n)

#BT: Tinh giai thua
# def giaithua(n):
#     print(f"Giai thua {n}:{math.factorial(n)}")
# n=int(input("Nhap n:"))
# giaithua(n)

#BT: Tinh tong mu 3
# def tongmu3(n):
#     s=0
#     for i in range(1,n,):
#         s+=math.pow(i,3)
#     print(f"Tong mu 3: {s}")
# n=int(input("Nhap n:"))
# tongmu3(n)

#BT: Tinh tong cac so le
# def tongle(n):
#     s=0
#     for i in range(1,n):
#         if i%2!=0:
#             s+=i
#     print(f"Tong cac so le tu 0 toi n: {s}")
# n=int(input("Nhap n:"))
# tongle(n)

#BT: Tinh tong cac so chan
# def tongchan(n):
#     s=0
#     for i in range(1,n):
#         if i%2==0:
#             s+=i
#     print(f"Tong cac so chan tu 0 toi n: {s}")
# n=int(input("Nhap n:"))
# tongchan(n)

#BT: Xac dinh so nguyen to
# def snt(n):
#     if n<2:
#         return 0
#     for i in range (2,int(math.sqrt(n))+1):
#         if n%i==0:
#             return 0
#     return 1
# n=int(input("Nhap n:"))
# if snt(n)==0:
#     print(f"{n} khong phai snt")
# else:
#     print(f"{n} la snt")

#BT: Xac dinh so chinh phuong
# def sochinhphuong(n):
#     if n<0:
#         return False
#     if math.sqrt(n)%1==0:
#         return True
#     else: 
#         return False
# n=int(input("Nhap n:"))
# print(sochinhphuong(n))

#BT: Tinh tong so nguyen to
# def tongsnt(n):
#     return sum(i for i in range(1,n+1) if snt(i)==1)
# n=int(input("Nhap n:"))
# print(tongsnt(n))

#BT: Lap bang cuu chuong thu n
# def bang9chuong(n):
#     for i in range(1,11):
#         print(f"{i}*{n}={i*n}")
# n=int(input("Nhap n:"))
# bang9chuong(n)

# BT: Tinh so fibonacci thu n
# def fibo(n):
#     "Ham tinh so fibonacci"
#     if n==1 or n==2:
#         return 1
#     return fibo(n-1) + fibo(n-2)
# n=int(input("Nhap n:"))
# print(f"So fibo thu {n}: {fibo(n)}")