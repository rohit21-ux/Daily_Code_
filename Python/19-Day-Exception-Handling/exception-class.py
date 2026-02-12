class InsufficientBalanceError(Exception):
    pass

def withdraw(balance,amount):
    if amount > balance:
        raise InsufficientBalanceError("Not Enough Balance!")
    return balance - amount

try:
    print(withdraw(30000,5000))
except InsufficientBalanceError as e:
    print("Transaction Failed",e)