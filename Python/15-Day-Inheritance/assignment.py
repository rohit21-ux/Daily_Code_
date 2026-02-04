class Person:
    def __init__(self,name,age):
        self.name =  name
        self.age = age
        
class Employee(Person):
    def __init__(self, name, age,salary):
        super().__init__(name, age)
        self.salary = salary
    
    def introduction(self):
        print(f"My name is {self.name},I'm {self.age} years old")


class Manager(Employee):
    def __init__(self, name, age, salary,bonus):
        super().__init__(name, age, salary)
        self.bonus = bonus

    def gift(self):
        print(f"Bonus:{self.bonus}")



m = Manager("Rohit",21,30000,10000)
m.introduction()
m.gift()

    
