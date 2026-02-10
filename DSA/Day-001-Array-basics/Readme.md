Data structure & Algorithm  - Day 1

Topic: Arrays & Time complexity 

This Document covers the foundation of Dsa
What is DSA 

# Dsa(Data structure and algorithm)
    - How data is stored (Data Structure)
    - How Problems are solved efficiently(Algorithm)

It helps in -
    - Writing optimized code
    - solving problems logically
    - Clearing technical interviews

# A dara structure is a way to store and organize data.

example:
       1) single value  - Variable
       2) multiple value -  Array (List in Python)
       3) key-value Pairs - Dictionarry
    
On Day 1, We focus on array

# What is An Algorithm?  -
     - Adding all elements in an array
     - Counting even numbers
     - Finding Maximum value
    
# Time Complexity (Big-O Notation)

Time complexity tells us how fats an algorithm runs as input size increases

1) O(1) - Constant Time
        - Execution time does not change with input size.

Example -  x = 10
           print(x)

2) O(n) - Linear Time
        - Execution time increases linearly with input size

Example:  for x in arr:
          print(x)

if array size is n, loops runs n times .

3) O(n²) - Quadratic Time
         - Execution time increases rapidly due to nested loops.

Example: for i in range(n):
             for j in range(n):
             print(i,j)


# ARRAYS (Python List):
 - An array stores multiple values of same type.

 Example: arr = [10,20,30,40]

# Common Operations and Time Complexity

Operation                     Example                       Time

 Access                        arr[0]                        0(1)
 Traversal                    for x in arr                   0(n)
 Append                       arr.append(50)                 0(1)



Key Learnings from Day 1:

1) Arrays are the base of all DSA concepts
2) Time complexity helps choose better solutions
3) Even simple Problems teach optimization thinking
