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
tpl = ('')

