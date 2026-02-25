# Normal way :
nums = [1, 2, 3, 4, 5, 6]

even = []
for n in nums:
    if n % 2 == 0:
        even.append(n)

print(even)

# with filter () : Used to filter elements based on a condition.
# syntax : filter(function, iterable)
nums = [1,2,3,4,5,6,7,8,9,11]

even = list(filter(lambda x: x % 2 == 0,nums))
print(even)
