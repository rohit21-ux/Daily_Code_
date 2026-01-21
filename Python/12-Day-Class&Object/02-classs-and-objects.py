class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says woof!")

my_dog = Dog("Buddy")
my_dog.bark()



class Person:
    def __init__(self,name):
        self.name=name

    def talk(self):
        print(f"{self.name} says hii")

my_person =Person("buddy")
my_person.talk()        


class car:
    def __init__(self,name):
        self.name=name

    def run(self):
        print(f"{self.name} sounds like ratattat")

my_car=car("Supra")
my_car.run()
        