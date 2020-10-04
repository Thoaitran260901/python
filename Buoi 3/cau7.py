n=int(input("Mời nhâp n: "))
m=int(input("Mời nhâp m: "))
def create_matrix(n, m):
    for i in range(1,n+1):
        for j in range(1,m+1):
            print(i*j,end="\t")
        print()
create_matrix(n,m)