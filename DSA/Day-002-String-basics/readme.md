# Dsa Day 2 - strings & Duplicate Removal

## Topics Covered
- String traversal
- Removing duplicate characters
- order preservation
- Time Complexity analysis
- Dry run techniques
- Optimization using Hashing (set)


# Problem : Remove Duplicate characters

Input :  banana

code

Output: ban

code

# basic approach
def remove_duplicates(s):
 result = ""
    for ch in s:
        if ch not in result:
            result += ch
    return result

print(remove_duplicates("banana"))

# How it Works
1) start with empty string result
2) Traverse each other 
3) If character is not already in result, add it
4) Return final result

# Dry run  example 
code 

missisippi

step-by-step result 

code

m
mi
mis
mis
mis
mis
misp

Final output:
misp

Time complexity -
1) Loop runs n times
2) ch not in result takes O(n) time
3) Total Complexity = O(n^2)

# Optimized aprroach 

def remove_duplicate_optimized(s):
    result = ""
    seen = set()

    for ch in s:
        if ch not in seen:
            seen.add(ch)
            result += ch    
    return result

print(remove_duplicate_optimized("missisippi"))

# Why This is better :
1) set() lookup is O(1)
2) Loop runs n times
3) Total Complexity = O(n)

## Key concepts learned today 
- String Traversal
- Duplicate Removal
- Order Preservation
- Time Complexity (O(n^2) vs O(n))
- Introduction to Hashing (set)
- Dry Run Method





