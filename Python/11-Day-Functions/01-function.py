''' Function is a reusable block of code that performs a specific task.to define a function in python provides the "def" Keyword followed by function name and paraentheses():'''

#Function can be declared without parameters 
def add():
    number_1 = 5
    number_2 = 2
    addition = number_1 + number_2
    print("Addition is:",addition)
add() #calling a function



'''Function returning a value
a function returns value back to the place where it was called .
we use keyword return followed by the variable we are returning.we can return any kind of data types from a function .'''
def sub():
    num_1 = 10
    num_2 = 5
    subtraction = num_1 - num_2
    return subtraction # returning a value 
print("Subtraction:",sub()) # calling a function



#Function can be declared with parameters (arguments) 

#Default parameters 
def greet (name = "friend"):
    print(name)

greet("Rohit") 


#one parameter
def greet(name):
    print("Hello",name)
#greet()  it will give error because argument is missing
greet("Rohit") #calling a function with argument

# Two parameters 
def multiply(a , b ):
    multiplication = a  * b
    print("Multiplication is:",multiplication)
multiply(b=3,a=5) #calling a function with two arguments


"""
*args - positional variable-length arguments
Collects multiple values into a tuple
"""
#Examples 
def add(*nums):
    return sum(nums)
print(add(2,4))
print(add(1,2,3,4))

'''Dictionary unpacking - we can call a functions which has named arguments using a dictionary with matching key names , we use "**" 
** - opens a dictionary and gives values to matching parametrs names '''

def greet(name,age,city):
    print("Name:",name,"Age:",age,"City:",city)

data = {
    "name": "Rohit",
    "age": 21,
    "city": "Latur"
}
greet(**data)

