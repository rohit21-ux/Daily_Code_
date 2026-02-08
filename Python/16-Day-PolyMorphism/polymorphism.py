# Polymorphism means same name different behaviour 
# polymorphism lets different objects respond to the same method name in their own way 

# method overrriding 
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog:
    def speak(self):
        print("Dog barks")

class Cat:
    def speak(self):
        print("cat meows")

animals = [Dog(),Cat(),Animal()]

for a in animals:
    a.speak()

# same method name speak()
# different outputs
# Thats runtime polymorphism
 