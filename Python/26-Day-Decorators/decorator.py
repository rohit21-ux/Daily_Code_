# A decorator:
#    - Wraps another function
#    - Adds extra behavior
#    - Without modifying original function

# Adding extra powers to a function.

def my_decorator(func):
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper

def say_hello():
    print("Hello!")

say_hello = my_decorator(say_hello)

say_hello()
