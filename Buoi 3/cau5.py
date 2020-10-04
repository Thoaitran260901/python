str="Hom Nay Troi Dep Lam"
def count_upper_lower(str):
    upper=0
    lower=0
    for i in str:
        if(i.isupper()):
            upper+=1
        elif(i.islower()):
            lower+=1
    print("Chữ hoa: ",upper)
    print("Chữ thường: ", lower)
print(str)
count_upper_lower(str)