# reduce(): used to reduce a list into single value.

# reduce() is inside the functools module, so we need to import it first.
# syntax: reduce(function, iterable)readme
from functools import reduce

nums = [1,2,3,4]

total = reduce(lambda x, y: x + y , nums)
print(total)
