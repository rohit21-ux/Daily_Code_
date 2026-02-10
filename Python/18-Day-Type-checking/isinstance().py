#isinsance() function is used to check if a variable or object belongs to a particular type or class.
# it returns True if the object matches the type/class you specify and false otherwise
#syntax : isinstance(object, classinfo)  object - the variable you want to check, classinfo - the type or even a tuple of multiple type/classes

class Vehicle:
    pass

class Bike(Vehicle):
    pass

class Dog:
    pass

b = Bike()

print(isinstance(b,Bike))   #True
print(isinstance(b,Vehicle))  #True - because of inheritance
print(isinstance(b,Dog)) #False 

