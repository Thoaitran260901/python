my_string = input("nhập chuỗi: ")
def thay_ki_tu():
    a= my_string[0]
    for i in range(1,len(my_string)):
        if my_string[i] == my_string[0]:
            a+="$"
        else:
            a+=my_string[i]
    return a
print(thay_ki_tu())
