# A string is just a sequence of characters . 

name = "Rohit"

# indexing: think of it like an array of characters.
# R  o  h  i  t
# 0  1  2  3  4

print(name[0]) #R
print(name[-1]) #t
# Access time = O(1) constant time

# Traversing a string
r = "Python"

for ch in r:
    print(ch)
# if string length  = n --> loop runs n times --> O(n) linear time

# strings are immutable in python.
s = "Hello"
#s[0] = "b" # type error 

# IMPORTANT : for interviews

s  = "bello"
s = "h" + s[1:]
print(s)





