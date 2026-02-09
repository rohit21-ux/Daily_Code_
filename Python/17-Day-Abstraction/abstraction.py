# abstraction - shows only what is needed , hide the rest 
# What a class must do not HOW it will do it 

from abc import ABC,abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass

class UPI(Payment):
    def pay(self):
        print("Paid using UPI")

class CARD(Payment):
    def pay(self):
        print("Paid using card")
    
Payments = [UPI(),CARD()]

for p in Payments:
    p.pay()  #object creation


