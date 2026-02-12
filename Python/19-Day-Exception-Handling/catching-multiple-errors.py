try:
    a = int(input("Number 1:"))
    b = int(input("Number 2:"))
    print(a/b)
except(ValueError, ZeroDivisionError) as e:
    print("An error ocuurred:",e)