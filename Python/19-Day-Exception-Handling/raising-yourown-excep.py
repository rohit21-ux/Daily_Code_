age  = int(input("Enter your age:"))

if age < 18:
    raise ValueError("You must be 18+")  # raise keyword is used to raise an exception with a custom error message
else:
    print("Welcome to the Website!")
