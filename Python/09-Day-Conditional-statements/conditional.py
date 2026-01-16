'''conditional statements in python are used to perform different actions based on certain conditions . the most common statements are if, elif, and else .'''



'''if conditional statement- the keyword if is used to test a specific condition.if the condition is true, the block of code within the if statement is executed.remember to use a colon : after condition and reember the indetation . '''

#syntax of if statement
#if condition:
    #this is the block of code to be executed if the condition is true 

#Example 
age = 18 
if age >=18:
    print("You are eligible for getting a driving licence.")


'''as we can see in above example the age is equal to 18 thats why the condition is true and then the the code block is executed 
'''
#Example 2
number = 7
if number % 2 == 0:
    print(f"{number} is an even number.")
#in this example the number is 7 which is not an even number so the condition is false and the code block is not executed ,thats why there is no output tpo print

''' if-else statement - the if-else statement is used to execute a block of code if the condition is true and another block of code if the condition is false
'''

#Syntax of if-else statement
'''if condition:
       #this block of code is executes if the true condition 
   
    else:
       #this block of code is executes for  the  false condition

    '''

#example 
age = int(input("Enter your age:"))
if age >= 18:
    
    print("You are eligible for getting a driving license")

else:
    print("You are not eligible for getting a driving license")



''' if elif else staement-  we use elif when we have multiple conditions to check .'''

#Synatx for if elif else statements 
''' if condition1:
        #this block of code executes if condition1 is true.

    elif condition2:
        #this block executes when condition2 is true 

    elif condition3:
        #this block executes when condition3 is true
    
    else:
        #this block executes when all the above conditions are false

        
'''

#Example 
marks =int(input("Enter your marks:"))

if marks >=90:
    print("Grade A !!")

elif marks >= 80:
    print("Grade B!!")

elif marks >= 70:
    print("Grade C!!")

else:
    print("Failed!! Better luck next time.")

# just short way to write if-else statement in single line
a  = 4
print("A is positive") if a>=0 else print("A is negative")


#Nested conditons
''' if else statements inside another if else statement is called nested if else statements .'''

a = int(input("Enter a number:"))
if a > 0:

    if a % 2 == 0:
        print(f"{a} is a positive even number")

    else:
        print(F"{a} is a positive number.")
else:
    print(f"{a} is a negative number.")

