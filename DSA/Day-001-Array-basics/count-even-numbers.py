def even_numbers(arr):
    count = 0
    for n in arr:
        if n % 2 == 0:
            count += 1
    return count
    
print(even_numbers([1,2,5,6,8,19,10]))

    
# Time Complexity: O(n)

# Space Complexity: O(1)
    