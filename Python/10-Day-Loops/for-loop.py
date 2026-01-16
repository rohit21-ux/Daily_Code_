''' for  is keyword used to make a for loop , loop is used to iterate over a  sequence (like a list ,dict,a set or string)
'''

#Using For loop on list
num = [0,1,2,3,4,5]
for n in num :    # n is temporary reference variable 
    print("Number is:",n) 


# Using for loop on string
name  = "Rohit"
for letter in name :
    print("Letter is:",letter)
    
for i in range (len(name)):
               print(name[i])

#Using For loop on tuple
tuple1 = (10,20,30,40,50)
for numbers in tuple1:
        print("Number in tuple is:",numbers)

#Using for loop on dictionary
dict1 = {'a':1,'b':2,'c':3}
for key in dict1:
        print("Key is:",key,"Value is:",dict1[key]) 

# Using break and continue statement in for loop
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break

# Continue statement\
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end")
print('outside the loop')
