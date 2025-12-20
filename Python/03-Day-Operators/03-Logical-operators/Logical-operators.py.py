'''
Logical operators uses keywords and ,or ,not to combine conditional statements.
operatr                   Name                       Example
and                    Logical AND              x<5 and x<10  
or                    Logical OR               x<5 or x<40
not                   Logical NOT              not(x<5 and x<10)

and -operator returns True if both statements are true 
or - operator returns true if one of the statemenets is true 
not - operator returns false if the result is true ,reverse the result 
'''

print("Logical operators in python \n")
print(3>2 and 4>3)  #True - both statements are true 
print(3>2 and 4<3)  #True - second statements is false
print(3 <2 and 4<3) #False - both statements are false
print("\n")

print(3>2 or 4>3)  #True - both statements are true 
print(3>2 or 4<3)  #True - first statements is true 
print(3<2 or 4<3)  #False - both statements are false
print("\n")

print(not 3>2) #false -reverse the true
print(not 3<2) #true - reverse the false
print("\n")