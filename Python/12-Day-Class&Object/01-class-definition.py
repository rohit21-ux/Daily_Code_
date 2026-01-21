class MyClass:
    def __init__(self, value):
        self.value = value

    def display(self):
        print(f"Value is: {self.value}")

if __name__ == "__main__":
    obj = MyClass("Example")
    obj.display()
