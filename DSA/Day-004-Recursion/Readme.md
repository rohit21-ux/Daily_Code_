# A function calling itself to solve a smaller version of the same problem.
# It breaks a big problem into smaller problems

Basic Structure of Recursion

1. Base case - When to stop
2. Recursive case - call itself with smaller input 

if no base case ---> infinite recursion

# Example 1:

def print_numbers(n):
    if n == 0:   # base case
       return 

    print(n)
    print_numbers(n - 1)   # Recursive call
print_numbers(5)

Output :

5
4
3
2
1

# Dry run (n == 3)
print_numbers(3)
 → print(3)
 → print_numbers(2)
    → print(2)
    → print_numbers(1)
       → print(1)
       → print_numbers(0)
          → stop

          