#an instance method is a function inside a class that works on instance variables .
# It always has self as a first parameter
# same method but different per object 
#self = the object that is calling the method 

#example

class BankAccount:
    def __init__(self,balance):
        self.balance = balance  #instance variable

    def deposit(self,amount):
        self.balance += amount   #update balance
        return self.balance
    
    def withdraw(self,amount):
        self.balance -= amount  # update balance
        return self.balance

    def show_balance(self):
        print("Balance:",self.balance)
    
a1 = BankAccount(2100)
a2 = BankAccount(1200)

print("Balance after deposit:",a1.deposit(200) ) 
print("Balance after deposit:",a2.deposit(500))

print("Balance after withdraw:",a1.withdraw(300))
print("Balance after withdraw:",a2.withdraw(200))



a1.show_balance()
a2.show_balance()




         