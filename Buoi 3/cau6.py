def is_pangram(str, alphabet):
    for char in alphabet:
         if char not in str.lower():
             return False
    return True
str=input("Nhap chuoi muon kiem tra: ")
alphabet="abcdefghijklmnopqrstuvwxyz"
if is_pangram(str,alphabet):
    print(f" \"{str}\" la chuoi pangram")
else:
    print(f" \"{str}\" khong la chuoi pangram")