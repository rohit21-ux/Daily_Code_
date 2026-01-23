#Class is like a blueprint for creating a object.The class defines attributes and the behaviour of objects.

#To create a class we need the keyword class followed by the name and colon.Class name shuld be CamelCase.

#Example
class Person:
    pass
print(Person)

#creating object by calling the class 
p = Person()
print(p)

#'''CLASS CONSTRUCTOR - a class without a constructor is not really useful in real application.we have to use constructor to make our class more useful. python has inbuilt constructor function "init()" constructor function. The init() has "self" parameter which is reference to the current instance of the class'''

#Example:
class Employee:
    def __init__(self,name):
        #self allows to attach paramter to the class
        self.name = name

p = Employee('Rohit')
print(p.name)
print(p)

class Person:
    def __init__(self,firstname,lastname,age,city,country):
        self.firstname = firstname
        self.lastname = lastname
        self.age =age
        self.city = city
        self.country = country

p = Person('Rohit','Jagave',21,'Latur','India')
print(p.firstname)
print(p.lastname)
print(p.age)
print(p.city)
print(p.country)


        