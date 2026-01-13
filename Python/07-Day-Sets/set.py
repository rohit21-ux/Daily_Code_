'''
set is a collection of items .we use {} curly braces to define or store items in set .
we can store unique items in set . set is mutable type 
set has some operations like union, intersection , difference etc. 
'''

#empty set 
empty_set = set()

# set with items 
set1  = {'item1','item2','item3'}

# example 
numbers  = {1,2,3,4,5}
#length of set 
print(len(numbers))

#checking the item in set 
print('Does set has 3 :',3 in numbers ) #True
print('Does set has 9 :',9 in numbers ) #False 

#adding items in set numbers 
'''we use add() method to add single item into set '''
numbers  = {1,2,3,4,5}
numbers.add(6)
print('After adding 6 in set :',numbers)

''' we use update() method to add multiple items into set '''
numbers.update([7,8,9])
print('after adding multiple items in set :',numbers)

vegetables = {'carrot','potato','tomato'}
numbers.update(vegetables)
print(numbers)

''' we can remove items from set using remove() method.'''
numbers  = {1,2,3,4,5}
numbers.remove(5)
print(numbers)

''' we can use pop() method to remove an  random item from set .'''
numbers  = {1,2,3,4,5}
removed_item = numbers.pop()
print('Removed random item:',numbers)

''' we can clear all items from set using clear() method .'''
numbers  = {1,2,3,4,5}
numbers.clear()
print('After clearing all items :',numbers)

'''we can delete entire set using del keyword 
numbers  = {1,2,3,4,5}
del numbers
print('After deleting set :',numbers)  #this will raise an error as set is deleted'''

''' we can convert list to set and set to list . converting list to set removes duplicates items'''
list1 = [1,2,2,3,3,4,4,5,5]
print('Original list:',list1)

set1 = set(list1)  # converting list to set 
print('List to set conversion:',set1)

'''Joining two sets using union() method ,we can also join two sets using update() method and | operator'''

setA = {1,2,3}
setB = {4,5,6}
setC = setA.union(setB)  #using union() method 
print('Union of setA and setB:',setC)  

setA.update(setB)  #using update() method
print('After updating setA with setB:',setA)

setC = setA | setB  #using | operator 
print('Union using | operator :',setC)

setA = {1,2,3,5}
setB = {2,3,4,5,6}
setA.intersection_update(setB)
print('Intersection of setA and setB:',setA)


'''checking subset and superset 
   subset : issubset() method
   superset : issuperset() method
'''
str1 = {'a','b','c','d'}
str2 = {'b','d'}
print('is str2 is subset of str1:',str2.issubset(str1)) #True
print('is str1 superset of str2:',str1.issuperset(str2)) #True
print('is str2 superset of str1:',str2.issuperset(str1)) #False


'''difference between two sets '''
whole_numbers =  {0,1,2,3,4,5,6}
even_numbers = {0,2,4,6}
whole_numbers.difference_update(even_numbers)
print('difference between two sets :',whole_numbers)



