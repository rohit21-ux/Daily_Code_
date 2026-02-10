#Array - python list

def sum_of_array(arr):
    total = 0
    for num in arr:
        total += num
    return total

# example usage 
array = [4, 6, 9, 4]
print(sum_of_array(array))
print(sum_of_array([1,2,3,4]))


print("size of array:",len(array))

# Time Complexity : O(n) 
# where n - numbers of elements in the array 

# Space Complexity : O(1) 

        