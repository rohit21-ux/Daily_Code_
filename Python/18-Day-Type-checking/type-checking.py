class ElectronicDevice:
    pass

class Computer(ElectronicDevice):
    pass

class Laptop(Computer):
    pass

class Pen:
    pass

l = Laptop()

print(isinstance(l,Laptop))
print(isinstance(l,Computer))
print(isinstance(l,ElectronicDevice))
print(isinstance(l,Pen))

print(issubclass(Laptop,Computer))
print(issubclass(Laptop,ElectronicDevice))
print(issubclass(Laptop,Pen))
print(issubclass(Pen,Laptop))

