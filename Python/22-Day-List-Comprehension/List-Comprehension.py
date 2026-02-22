# List comprehension reduce code length and make it more readable.
# Lambda funstion is used in sorting problems 

# syntax of list comprehension : [expression for item in iterable]


# Example 1: Create a list of squares of numbers from 0 to 9

sqaures = [i * i for i in range(0,10)]
print(sqaures)

# with condition
even = [i for i in range(0,10) if i % 2 == 0]
print(even)

# Lambda function : Function without name 

# normal function
def add(x,y):
    return x + y

# lambda function version
add = lambda x,y : x + y
print(add(5,10))

# Syntax : lambda arguments: expression

