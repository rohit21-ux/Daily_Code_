#object is the instance for a class.we can create a object by calling class .

# object methods - Objects can have methods .The methods are functions which belongs to the object .

#example:
class Person:
    def __init__(self,firstname,lastname,age,country):
        self.firstname =firstname
        self.lastname = lastname
        self.age = age
        self.country = country

    def person_info(self):
            return f'{self.firstname} { self.lastname} {self.age} years old.He lives in {self.country}'

#creating a object        
p = Person(firstname= "Rohit",
          lastname= "Jagave",
          age= 21,
          country= "India"
          )
#calling a object with method
print(p.person_info())


#Object default method - deault values for your object methods .
class Person:
    def __init__(self,firstname='Rohit',lastname='Jagave',age=21,country='India'):

        self.firstname =firstname
        self.lastname = lastname
        self.age = age
        self.country = country

    def person_info(self):
            return f'{self.firstname} { self.lastname} {self.age} years old.He lives in {self.country}'
p = Person()
print(p.person_info)

        