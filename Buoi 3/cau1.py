# Max,min
def max_min(*numbers):
    print("giá trị truyền vào: ", numbers)
    return max(numbers), min(numbers)
max,min=max_min(1,2,3,4,5,6,7,8,10)
print(f"Max: {max}, Min: {min}")
