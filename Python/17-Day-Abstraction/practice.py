from abc import ABC,abstractmethod

class Destination(ABC):

    @abstractmethod
    def reached(self):
        pass

class Car(Destination):
    def reached(self):
        print("Reached by car")

class Bus(Destination):
    def reached(self):
        print("Reached by Bus")

Sources = [Car(),Bus()]

for s in Sources:
    s.reached()
    
