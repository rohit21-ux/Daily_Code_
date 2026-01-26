# Inheritance = inheriting features from one class to another class .
# Parent class features to child class .
# Inheritance helps to reuse the code 

'''syntax:

class Parent:
    pass
     
class Child(Parent): # inheritance complete
    pass
    
'''
class Person:   # parent class
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old")

class Student(Person):
    pass  # even with pass ,Student already has all features of class Person

s1 = Student("Rohit",21)
s1.introduce()
