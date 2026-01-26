# Super() lets the child class use the parents constructor or methods
# or Super() is the way for the child class to call the  parent class.

# Parent class
class Animal:
    def __init__(self,species,age):   # instance variable
        self.species = species
        self.age = age

# child class
class Dog(Animal):
    def __init__ (self,species,age,breed):
        super().__init__(species,age)  # calling parent constructor
        self.breed = breed
    
    def identification(self):
        print(self.species,self.age,self.breed)

#object creation
d = Dog("canis",2,"German Shehpard")
d.identification()

# If child class has __init__, use super() to call parent __init__
       