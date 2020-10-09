chuoi = input("nhap: ")
def thaydoichucaidau():
    s= "$"
    for i in range(1,len(chuoi)):
        if chuoi[i] == chuoi[0]:
            s+="$"
        else:
            s+=chuoi[i]
    return s
print(f"chuoi: {thaydoichucaidau()}")