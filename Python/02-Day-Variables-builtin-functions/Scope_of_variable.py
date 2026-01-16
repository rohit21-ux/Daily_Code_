# global and Local variables 
global_var = "I am a global variable"

def my_function():
    local_var = "I am a local Variable"
    print(local_var)
    print(global_var)  # accssing global variable inside function 

my_function()

print(global_var)  # accessing global variable outside function 

#print (local_var ) # this will raise an error as local_var is not accessible outside the function 