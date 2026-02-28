# Generator : produce values one by one 
# Does not store everything
# uses yield 
# Used to save memory spaces and RAM usage 
 
# normal function:
def numbers():
    return [1,2,3]

print(numbers())

# Using Generator:
def numbers():
    yield 1
    yield 2
    yield 3

for num in numbers():
    print(num)


def even(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

for num in even(21):
    print(num)

# Generator Expression
# List comprehension: []
nums = [x*3 for x in range(6)]
print("Cubes:",nums)


# Generator expression: ()

nums = (x*3 for x in range(6))

for n in nums:
    print("Cubes:",n)


# next() is a built in function that gets the next value from an iterator, moves the iterator forward, remembers its position
nums = (x*3 for x in range(6))

print(next(nums))
print(next(nums))



