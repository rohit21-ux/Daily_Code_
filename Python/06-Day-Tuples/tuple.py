'''tuple is a collection of different data types which is oredered and unchangeable (immutable).Tuples are written with round brackets  ().'''

'''since Tuples are immutable we can not use add,insert ,remove methods in tuple because it is not mutable or changeble.'''

'''tuple methhods :
  1.tuple(): to create any empty tuple
  2.count(): to count the number of specified item in tuple
  3.index(): tp find the index of a specified item in a tuple
'''


#creating a tuple 
empty_tuple = ()

# using tuple constructor 
empty_tuple = tuple()

#initial values 
tpl1 = ('item1','item2','item3')
fruits  = ('apple','banana','cherry','mango')

'''we use len() method to get the length of a tuple '''

fruits  = ('apple','banana','cherry','mango')
print('Length of tuple:',len(fruits))


fruits  = ('apple','banana','cherry','mango')
print('First item:',(fruits[0])) #fruits[-4]
print('Last item:',(fruits[-1]))  #mango

#Slicing tuple 
''' 

we can slice out a sub-tuple by specifying a range of indexers where to start and where to end in the tuple ,the return value will be new tuple with the specified items.

'''

#Syntax 
tpl = ('item1','item2','item3')
all_items = tpl[0:3]
all_items = tpl[0:]
print('all_items:',all_items)

fruits  = ('apple','banana','cherry','mango','orange','kiwi','melon','papaya')
print('sliced fruits:',fruits[0:5])


#negative indexes
fruits  = ('apple','banana','cherry','mango','orange','kiwi','melon','papaya')
print('sliced fruits with negative index:',fruits[-5:-1])

#changing tuples to lists 
''' we can change tuples to lists and lists to tuples .Tuple is immutable if we wwant to change or modify a tuple we can convert it to list and then make the changes and aagain convert it back to tuple '''
fruits  = ('apple','banana','cherry','mango')

#convert tuple to list
fruits = list(fruits)
fruits[0] = 'orange' #update firts item
fruits.append('grape') #update by adding new item at last 
print('Modified list:',fruits)

#convert list back to tuple 
fruits = tuple(fruits)
print('Modified tuple:',fruits)

#check if item exists in tuple 
'papaya'in fruits 
print('is papaya presemt in tuple fruits ?:','papaya' in fruits )

#checking index of tuple item
print(fruits.index('orange'))

#joining of tuples 
'''we can join two or more tuples by using + operator only '''

tuple1 = ('a','b','c')
tuple2 = (1,2,3,4)
tuple3 = tuple1 + tuple2
print('Joined tuple :',tuple3)

#deleting tuples 
''' it is not possible to delete items from a tuple but we can delete the entire tuples using "del" keyword '''

tuple1 = ('a','b','c')
del tuple1
print(tuple1)   #this will raise an error because the tuple no longer exists


