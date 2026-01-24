class Person:
    def __init__(self,salary):
        self.salary = salary

    def spend(self, amount):
        self.salary -= amount
    
    def grocery(self,amount):
        self.salary -= amount

    def __str__(self): 
        return f"Remained salary after expenses:{self.salary}"
    
s1 = Person(70000)

s1.spend(5000)
s1.grocery(2000)

print(s1)
print(s1)

        