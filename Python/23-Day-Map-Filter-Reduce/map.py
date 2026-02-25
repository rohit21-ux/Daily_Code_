# map () is used to apply a function to every element in a list
# syntax: map(function, iterable)

nums  = [1,2,3,4]

cubes  =  list(map(lambda x:x * x * x, nums))
print(cubes)