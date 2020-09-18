print("----HÌNH TAM GIÁC----")
mang = int(input("nhap so luong: "))
for cdoc in range(mang):
 for cngang in range(mang):
     if cngang == range(mang) or cngang < cdoc or cngang == cdoc :
      print("*",end="")
 print()
