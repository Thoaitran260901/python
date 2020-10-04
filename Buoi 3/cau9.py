print("Chuyen hoa thanh thuong va nguoc lai")
def change_upper_lower(str):
    str=str.swapcase()
    print(f"Chuoi sau khi chuyen: {str}")
str=input("Nhap chuoi muon chuyen: ")
change_upper_lower(str)