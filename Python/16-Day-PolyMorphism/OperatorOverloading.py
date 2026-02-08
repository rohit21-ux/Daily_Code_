# operators are just methods with symbol

class Number:
    def __init__(self,value):
        self.value = value

    def __add__(self,other):
        return self.value + other.value

a = Number(4)
b = Number(3)

print(a + b)


        