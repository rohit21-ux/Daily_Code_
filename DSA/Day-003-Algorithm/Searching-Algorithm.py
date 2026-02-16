# Searching = Finding a value inside data 
# 1. Linear Search - Time Complexity = O(n)

def linear_search(arr , target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Works on sorted & unsorted data
# slow for big data sets


# 2. Binary Search - Time Complexity = O(log n)
# array must be sorted

#idea:
      # check middle
      # divide into 2 halves
      # Repeat 

def binary_search(arr , target):
    left = 0                 # initialize left pointer (initial index)
    right =  len(arr) - 1    # right pointer  (last index for search)

    while left <= right:
        mid = (left + right)  //2# find the middle index (splits the array into 2 halves)

        if arr[mid] == target:  # compare middle element with target (Found --> return next)
            return mid

        elif arr[mid] < target: # if middle element is less than target, then target must be in the right half 
            left =  mid + 1     # move left pointer to the right of middle index

        else:                   # if middle is bigger than target , then target must be in the left half
            right =  mid - 1

    return -1   # target doesnt exists 
print(binary_search([10,20,30,40,50],20)) 

