x = 10 
y = 4.5
z = "300"

print("x:",type(x))   # <class 'int'>
print("y:",type(y))   # <class 'float'>
print("z:",type(z))   # <class 'str'>

# Type Conversion
num = int(y)  # convert float to integer
print(num,type(num)) # 4  <class 'int'>

str =  str(x)  # convert integer to string
print(str,type(str))  # 10 <class 'str'>

flt = float(z) # convert string to float
print(flt,type(flt))  # 300.0 <class 'float'>
