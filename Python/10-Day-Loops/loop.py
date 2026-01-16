''' loop is used to do repetitive tasks in programm
    Python provides two types of loops:
    1. while loop - repeats a block of code as long as a condition is true 
    2. for loop- used to do some tasks for a fixes number of times 
'''
#while loop in python
''' we use reserved word 'While' to create a while loop 
     it is used to execute a block of code repeatedly until a given condition is true  or satisfied . when the condtion become false the lines of code after the loop will be executed '''

#EXample 
count = 0
while count < 5:
    print("The count is :", count )
    count = count + 1
print("While loop is ended")

# we uses else statement with while loop to executes false condition
count = 0
while count < 5:
    print("Count is:",count)
    count = count + 1

else:
    print("statement is false now count is :",count)

''' above loop condition is false when count become 5 so else block executes and 5 prints'''

#Break and continue statement in while loop
''' Break staement is used to get out or dtop the loop 
'''
count = 0
while count < 6:
    print("count is:",count)
    count = count + 1
    if count == 3:
        break
''' above while loop only prints 0,1,2  but when it reaches 3 it stops the loop '''

#Continue statement is used to skip the current iteration and continue with the next.
count = 0
while count < 5:
    if count == 3:
        count = count +1
        continue
    print("Count is :",count)
    count  = count + 1



